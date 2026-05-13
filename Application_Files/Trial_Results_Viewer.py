from __future__ import annotations

"""
Trial results browser for saved JSON logs.

The viewer is intentionally read-only: it scans a selected Trial_Logs folder,
loads experiment JSON files, and lets the user drill down from trial folder to
configuration to individual patient report. Body-map annotations are redrawn on
the same image used during logging, and clicking a mark jumps to that mark's
notes.
"""

import json
import traceback
from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets


class ResultsFolderDialog(QtWidgets.QDialog):
    """Small dialog that asks the user which Trial_Logs folder to inspect."""

    def __init__(self, default_folder: Path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Trial Results")
        self.resize(650, 160)
        self.selected_folder = Path(default_folder)

        title = QtWidgets.QLabel("Please Locate Results Folder")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.folder_edit = QtWidgets.QLineEdit(str(self.selected_folder))
        self.folder_edit.setReadOnly(True)

        browse_button = QtWidgets.QPushButton("Browse")
        browse_button.clicked.connect(self.browse)

        open_button = QtWidgets.QPushButton("Open Results")
        open_button.clicked.connect(self.accept)

        cancel_button = QtWidgets.QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        folder_row = QtWidgets.QHBoxLayout()
        folder_row.addWidget(self.folder_edit, 1)
        folder_row.addWidget(browse_button)

        button_row = QtWidgets.QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(cancel_button)
        button_row.addWidget(open_button)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(title)
        layout.addLayout(folder_row)
        layout.addLayout(button_row)

    def browse(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Please Locate Results Folder",
            str(self.selected_folder),
        )
        if folder:
            self.selected_folder = Path(folder)
            self.folder_edit.setText(str(self.selected_folder))

    def accept(self):
        """Only close successfully when the chosen path is a real directory."""
        self.selected_folder = Path(self.folder_edit.text())
        if not self.selected_folder.exists() or not self.selected_folder.is_dir():
            QtWidgets.QMessageBox.warning(
                self,
                "Folder Not Found",
                "Please select a valid results folder.",
            )
            return
        super().accept()


class ResultsImageView(QtWidgets.QGraphicsView):
    """Graphics view with mouse-wheel zoom for the body-map image."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._zoom = 0
        self.setRenderHints(
            QtGui.QPainter.Antialiasing
            | QtGui.QPainter.SmoothPixmapTransform
            | QtGui.QPainter.TextAntialiasing
        )
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            factor = 1.15
            self._zoom += 1
        else:
            factor = 1 / 1.15
            self._zoom -= 1

        if self._zoom < -10:
            self._zoom = -10
            return

        self.scale(factor, factor)


class ClickableAnnotationMarker(QtWidgets.QGraphicsEllipseItem):
    """Clickable body-map dot that jumps to the matching text note."""

    def __init__(self, rect: QtCore.QRectF, viewer, annotation_index: int, parent=None):
        super().__init__(rect, parent)
        self.viewer = viewer
        self.annotation_index = annotation_index
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setAcceptedMouseButtons(QtCore.Qt.LeftButton)

    def mousePressEvent(self, event):
        self.viewer.select_annotation_note(self.annotation_index)
        event.accept()


class ClickableAnnotationLabel(QtWidgets.QGraphicsTextItem):
    """Clickable number label next to a body-map dot."""

    def __init__(self, text: str, viewer, annotation_index: int, parent=None):
        super().__init__(text, parent)
        self.viewer = viewer
        self.annotation_index = annotation_index
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.setAcceptedMouseButtons(QtCore.Qt.LeftButton)

    def mousePressEvent(self, event):
        self.viewer.select_annotation_note(self.annotation_index)
        event.accept()


class TrialResultsViewer(QtWidgets.QDialog):
    """Four-column trial results browser plus body-map/notes detail view."""

    def __init__(self, results_folder: Path, image_path: Path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Trial Results Viewer")
        self.resize(1450, 850)

        self.results_folder = Path(results_folder)
        self.image_path = Path(image_path)
        self._folder_records = {}
        self._active_trial_logs = []
        self._active_reports = []

        self.trial_list = QtWidgets.QListWidget()
        self.config_list = QtWidgets.QListWidget()
        self.log_list = QtWidgets.QListWidget()

        self.scene = QtWidgets.QGraphicsScene(self)
        self.image_view = ResultsImageView()
        self.image_view.setScene(self.scene)
        self.notes_text = QtWidgets.QTextEdit()
        self.notes_text.setReadOnly(True)

        # Used to expire old highlight timers when the user clicks marks quickly.
        self._selected_annotation_index = None
        self._highlight_generation = 0

        self._build_layout()
        self._connect_signals()
        self.load_results_folder()

    def _build_layout(self):
        """Build the left-to-right drill-down layout."""
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(self._panel("Trials", self.trial_list))
        splitter.addWidget(self._panel("Configurations", self.config_list))
        splitter.addWidget(self._panel("Logs", self.log_list))
        splitter.addWidget(self._detail_panel())
        splitter.setSizes([260, 300, 240, 650])

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(splitter)

    def _panel(self, title: str, widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
        box = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(box)
        label = QtWidgets.QLabel(title)
        label.setStyleSheet("font-weight: bold;")
        layout.addWidget(label)
        layout.addWidget(widget, 1)
        return box

    def _detail_panel(self) -> QtWidgets.QWidget:
        box = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(box)

        image_label = QtWidgets.QLabel("Body Map")
        image_label.setStyleSheet("font-weight: bold;")
        notes_label = QtWidgets.QLabel("Log Notes")
        notes_label.setStyleSheet("font-weight: bold;")

        layout.addWidget(image_label)
        layout.addWidget(self.image_view, 3)
        layout.addWidget(notes_label)
        layout.addWidget(self.notes_text, 2)
        return box

    def _connect_signals(self):
        self.trial_list.currentItemChanged.connect(self.on_trial_selected)
        self.config_list.currentItemChanged.connect(self.on_config_selected)
        self.log_list.currentItemChanged.connect(self.on_log_selected)

    def load_results_folder(self):
        """Find experiment folders containing JSON files with trial_logs."""
        self.trial_list.clear()
        self.config_list.clear()
        self.log_list.clear()
        self.clear_detail("Select a trial folder to begin.")
        self._folder_records.clear()

        folders = [
            path for path in sorted(self.results_folder.iterdir(), key=lambda p: p.name.lower())
            if path.is_dir()
        ]

        for folder in folders:
            json_paths = sorted(folder.glob("*.json"))
            records = []
            for json_path in json_paths:
                try:
                    with open(json_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if isinstance(data, dict) and isinstance(data.get("trial_logs"), list):
                        records.append({"path": json_path, "data": data})
                except Exception:
                    # A bad file should not prevent browsing the rest of the results.
                    traceback.print_exc()

            if not records:
                continue

            item = QtWidgets.QListWidgetItem(folder.name)
            item.setData(QtCore.Qt.UserRole, folder)
            self.trial_list.addItem(item)
            self._folder_records[str(folder)] = records

        if self.trial_list.count() == 0:
            self.clear_detail("No experiment JSON logs were found in the selected folder.")

    def on_trial_selected(self, current, _previous):
        """Populate configurations for the selected experiment folder."""
        self.config_list.clear()
        self.log_list.clear()
        self.clear_detail("Select a configuration.")
        self._active_trial_logs = []
        self._active_reports = []

        if current is None:
            return

        folder = current.data(QtCore.Qt.UserRole)
        records = self._folder_records.get(str(folder), [])

        for record in records:
            json_name = record["path"].name
            for trial_log in record["data"].get("trial_logs", []):
                self._active_trial_logs.append(trial_log)
                config_number = len(self._active_trial_logs)
                order_number = trial_log.get("order_number", config_number)
                item = QtWidgets.QListWidgetItem(
                    f"{config_number}. {self._format_condition(trial_log.get('condition', {}))}"
                )
                item.setData(QtCore.Qt.UserRole, trial_log)
                item.setToolTip(f"{json_name}\nOrder number: {order_number}")
                self.config_list.addItem(item)

    def on_config_selected(self, current, _previous):
        """Populate patient reports/logs for the selected configuration."""
        self.log_list.clear()
        self.clear_detail("Select an intensity log.")
        self._active_reports = []

        if current is None:
            return

        trial_log = current.data(QtCore.Qt.UserRole) or {}
        reports = trial_log.get("patient_reports", [])
        if not isinstance(reports, list):
            reports = []
        if not reports:
            self.clear_detail("This configuration has no saved patient logs.")
            return

        for index, report in enumerate(reports, start=1):
            self._active_reports.append(report)
            intensity = report.get("current_intensity_ma", "")
            time_text = self._short_time(report.get("current_time", ""))
            item = QtWidgets.QListWidgetItem(f"{index}. {intensity} mA    {time_text}")
            item.setData(QtCore.Qt.UserRole, report)
            self.log_list.addItem(item)

    def on_log_selected(self, current, _previous):
        if current is None:
            return
        self.show_report(current.data(QtCore.Qt.UserRole) or {})

    def show_report(self, report: dict):
        """Render one patient report's annotations and note text."""
        annotations = (
            report.get("patient_log", {}).get("annotations", [])
            if isinstance(report.get("patient_log"), dict)
            else []
        )
        if not isinstance(annotations, list):
            annotations = []
        self.draw_annotations(annotations)
        self.notes_text.setPlainText(self._format_report_notes(report, annotations))
        self.notes_text.setExtraSelections([])
        self._selected_annotation_index = None

    def draw_annotations(self, annotations: list[dict]):
        """Draw clickable annotation marks on top of the body-map image."""
        self.scene.clear()

        pixmap = QtGui.QPixmap(str(self.image_path))
        if pixmap.isNull():
            self.scene.addText(f"Could not load image:\n{self.image_path}")
            return

        pixmap_item = self.scene.addPixmap(pixmap)
        self.scene.setSceneRect(pixmap_item.boundingRect())

        for index, annotation in enumerate(annotations, start=1):
            try:
                x = float(annotation.get("x", 0))
                y = float(annotation.get("y", 0))
            except (TypeError, ValueError):
                continue

            motor = bool(annotation.get("motor_threshold_reached", False))
            color = QtGui.QColor("#7b1fa2" if motor else "#d32f2f")

            # Keep dot and label separate so either one can be clicked.
            marker = ClickableAnnotationMarker(
                QtCore.QRectF(x - 7, y - 7, 14, 14),
                viewer=self,
                annotation_index=index,
            )
            marker.setPen(QtGui.QPen(QtCore.Qt.white, 2))
            marker.setBrush(QtGui.QBrush(color))
            marker.setToolTip(self._format_annotation_summary(annotation))
            self.scene.addItem(marker)

            text = ClickableAnnotationLabel(str(index), viewer=self, annotation_index=index)
            text.setDefaultTextColor(QtCore.Qt.white)
            text.setPos(x + 8, y - 14)
            text.setToolTip("Click to jump to this mark's notes")
            self.scene.addItem(text)

        QtCore.QTimer.singleShot(0, lambda: self.image_view.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio))

    def select_annotation_note(self, annotation_index: int):
        """Jump the notes pane to the selected mark and briefly highlight it."""
        plain_text = self.notes_text.toPlainText()
        start = plain_text.find(f"Mark {annotation_index}\n")
        if start < 0:
            start = plain_text.find(f"Mark {annotation_index}")
        if start < 0:
            return

        end = plain_text.find("\nMark ", start + 1)
        if end < 0:
            end = len(plain_text)
        else:
            # Trim the blank line before the next mark so only this block glows.
            while end > start and plain_text[end - 1] == "\n":
                end -= 1

        # Put the live cursor at the start of the block. If we selected the
        # whole block here, QTextEdit would often scroll to the selection end.
        cursor = QtGui.QTextCursor(self.notes_text.document())
        cursor.setPosition(start)
        self.notes_text.setTextCursor(cursor)
        self.scroll_notes_to_cursor_top(cursor)

        highlight = QtWidgets.QTextEdit.ExtraSelection()
        highlight.cursor = QtGui.QTextCursor(self.notes_text.document())
        highlight.cursor.setPosition(start)
        highlight.cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
        highlight.format.setBackground(QtGui.QColor("#fff3a3"))
        highlight.format.setProperty(QtGui.QTextFormat.FullWidthSelection, True)
        self.notes_text.setExtraSelections([highlight])
        self._selected_annotation_index = annotation_index
        self._highlight_generation += 1
        highlight_generation = self._highlight_generation
        self.notes_text.setFocus(QtCore.Qt.OtherFocusReason)
        QtCore.QTimer.singleShot(
            600,
            lambda: self.clear_annotation_highlight(annotation_index, highlight_generation),
        )

    def scroll_notes_to_cursor_top(self, cursor: QtGui.QTextCursor):
        """Scroll so the selected mark heading starts near the top of the view."""
        self.notes_text.ensureCursorVisible()

        # cursorRect is relative to the visible viewport after ensureCursorVisible.
        cursor_rect = self.notes_text.cursorRect(cursor)
        scroll_bar = self.notes_text.verticalScrollBar()
        top_padding = 4
        scroll_bar.setValue(scroll_bar.value() + cursor_rect.top() - top_padding)

    def clear_annotation_highlight(self, annotation_index: int, highlight_generation: int):
        """Clear only the still-current transient highlight."""
        if self._selected_annotation_index != annotation_index:
            return
        if self._highlight_generation != highlight_generation:
            return

        self.notes_text.setExtraSelections([])
        cursor = self.notes_text.textCursor()
        cursor.clearSelection()
        self.notes_text.setTextCursor(cursor)
        self._selected_annotation_index = None

    def clear_detail(self, message: str = ""):
        """Reset the body-map/notes detail area between selections."""
        self.scene.clear()
        if message:
            self.scene.addText(message)
        self.notes_text.setPlainText(message)
        self.notes_text.setExtraSelections([])
        self._selected_annotation_index = None
        self._highlight_generation += 1

    def _format_condition(self, condition: dict) -> str:
        """Build the compact configuration label shown in the middle column."""
        if not isinstance(condition, dict):
            condition = {}

        parts = [
            condition.get("electrode_config", ""),
            condition.get("waveform", ""),
            condition.get("polarity", ""),
        ]
        text = " | ".join(str(part) for part in parts if part not in (None, ""))
        return text or "Configuration"

    def _short_time(self, value) -> str:
        """Show only HH:MM:SS when the JSON contains an ISO timestamp."""
        text = str(value or "")
        if "T" in text:
            return text.split("T", 1)[1].split(".", 1)[0]
        return text

    def _format_report_notes(self, report: dict, annotations: list[dict]) -> str:
        """Convert one patient report into readable notes grouped by mark."""
        lines = [
            f"Current Intensity: {report.get('current_intensity_ma', '')} mA",
            f"Log Time: {report.get('current_time', '')}",
            f"Annotations: {len(annotations)}",
            "",
        ]

        if not annotations:
            lines.append("No body-map annotations were saved for this log.")
            return "\n".join(lines)

        for index, annotation in enumerate(annotations, start=1):
            lines.append(f"Mark {index}")
            lines.append(f"  Feeling: {annotation.get('sensation', '') or 'Not recorded'}")
            lines.append(f"  Intensity: {annotation.get('intensity', '') or 'Not recorded'}")
            lines.append(f"  Consistency: {annotation.get('temporal_quality', '') or 'Not recorded'}")
            lines.append(f"  Bilateral: {'Yes' if annotation.get('bilateral', False) else 'No'}")
            lines.append(f"  Motor threshold: {'Yes' if annotation.get('motor_threshold_reached', False) else 'No'}")
            lines.append(f"  Motor intensity: {annotation.get('motor_intensity', '') or 'Not recorded'}")
            lines.append(f"  Motor quality: {annotation.get('motor_quality', '') or 'Not recorded'}")
            lines.append(f"  Motor consistency: {annotation.get('motor_temporal_quality', '') or 'Not recorded'}")
            lines.append(f"  Notes: {annotation.get('additional_notes', '') or 'None'}")
            lines.append("")

        return "\n".join(lines).rstrip()

    def _format_annotation_summary(self, annotation: dict) -> str:
        """Tooltip text for a body-map mark."""
        return "\n".join(
            [
                f"Feeling: {annotation.get('sensation', '') or 'Not recorded'}",
                f"Intensity: {annotation.get('intensity', '') or 'Not recorded'}",
                f"Consistency: {annotation.get('temporal_quality', '') or 'Not recorded'}",
                f"Notes: {annotation.get('additional_notes', '') or 'None'}",
            ]
        )
