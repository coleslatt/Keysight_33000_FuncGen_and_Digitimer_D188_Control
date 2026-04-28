from __future__ import annotations
import random
import datetime
import numpy as np
import pandas as pd
from FuncGen_Selector_Function_2 import func_gen_control, func_gen_control_stateful
from dataclasses import dataclass, field
from datetime import datetime
import traceback
import os
from dataclasses import asdict

from PySide6.QtWidgets import (
    QGraphicsEllipseItem,
    QListWidgetItem,
    QGraphicsItem,
    QGraphicsScene,
    QGraphicsView,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QPushButton,
    QMenu,
    QFileDialog,
    QMessageBox,
    QLabel,
    QComboBox,
    QTextEdit,
    QGroupBox,
    QRadioButton,
    QButtonGroup,
    QDialogButtonBox,
    QApplication,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

from PySide6.QtGui import QBrush, QPixmap, QWheelEvent, QCursor
from PySide6.QtCore import Qt, QTimer

import json
import csv

from pathlib import Path


SENSATION_OPTIONS = [
    "",
    "Buzzing",
    "Tingling",
    "Pulsing",
    "Pressure",
    "Warmth",
    "Sharp",
    "Electric",
    "Itching",
    "Numbness",
]

TEMPORAL_QUALITY_OPTIONS = [
    "",
    "Brief",
    "Consistent",
    "Momentary",
    "Transient",
    "Intermittent",
    "Continuous",
    "Rhythmic",
    "Fluctuating",
]

MOTOR_QUALITY = [
    "",
    "Twitch",
    "Brief contraction",
    "Sustained contraction",
    "Jerking",
    "Rhythmic movement",
    "Visible activation",
    "Strong contraction",
]

@dataclass
class TrialCondition:
    electrode_config: str = ""
    waveform: str = ""
    polarity: str = ""

@dataclass
class PatientBodyLog:
    annotations: list[BodyAnnotation] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class PatientReport:
    current_intensity_ma: float = 0.0
    patient_log: PatientBodyLog | None = None
    current_time: datetime = field(default_factory=datetime.now)

@dataclass
class TrialLogEntry:
    current_time: datetime = field(default_factory=datetime.now)
    condition: TrialCondition = field(default_factory=TrialCondition)
    displayed_status: str = ""
    patient_reports: list[PatientReport] = field(default_factory=list)
    order_number: int = 0
    total_trial_time_seconds: int = 0

@dataclass
class IntensityChangeEvent:
    current_time: datetime = field(default_factory=datetime.now)
    trial_index: int = 0
    order_number: int = 0
    electrode_config: str = ""
    waveform: str = ""
    previous_intensity_ma: float = 0.0
    new_intensity_ma: float = 0.0
    increment_ma: float = 0.0
    direction: str = ""

@dataclass
class ExperimentLog:
    start_time: datetime = field(default_factory=datetime.now)
    trial_logs: list[TrialLogEntry] = field(default_factory=list)
    intensity_change_events: list[IntensityChangeEvent] = field(default_factory=list)
    patient_first_name: str = ""
    patient_last_name: str = ""
    patient_id: str = ""
    total_experiment_time_seconds: int = 0

# Dataclasses for body annotations on the body map

@dataclass
class BodyAnnotation:
    x: float
    y: float

    # Sensation
    intensity: int = 0
    sensation: str = ""
    temporal_quality: str = ""
    bilateral: bool = False

    # Motor
    motor_threshold_reached: bool = False
    motor_intensity: int = 0
    motor_quality: str = ""
    motor_temporal_quality: str = ""

    # Free text
    additional_notes: str = ""

    created_at: datetime = field(default_factory=datetime.now)


def annotation_color(annotation: BodyAnnotation):
    return Qt.darkMagenta if annotation.motor_threshold_reached else Qt.red


# class ToggleRadioButton(QRadioButton):
#     def __init__(self, text="", group=None, parent=None):
#         super().__init__(text, parent)
#         self._button_group = group
#         self.pressed.connect(self._remember_pressed_state)
#         self._was_checked_on_press = False

#     def _remember_pressed_state(self):
#         self._was_checked_on_press = self.isChecked()

#     def mouseReleaseEvent(self, event):
#         super().mouseReleaseEvent(event)

#         if event.button() != Qt.LeftButton:
#             return

#         if not self.rect().contains(event.pos()):
#             return

#         if not self._was_checked_on_press:
#             return

#         try:
#             if self._button_group is not None:
#                 self._button_group.setExclusive(False)
#                 self.setChecked(False)
#                 self._button_group.setExclusive(True)
#             else:
#                 self.setAutoExclusive(False)
#                 self.setChecked(False)
#                 self.setAutoExclusive(True)
#         except Exception:
#             traceback.print_exc()

class ToggleRadioButton(QRadioButton):
    """
    A radio button that can be toggled off by clicking it again.
    """

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self._was_checked_on_press = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._was_checked_on_press = self.isChecked()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)

        if event.button() != Qt.LeftButton:
            return

        if not self.rect().contains(event.pos()):
            return

        if not self._was_checked_on_press:
            return

        try:
            group = self.group()
            if group is not None:
                group.setExclusive(False)
                self.setChecked(False)
                group.setExclusive(True)
            else:
                self.setAutoExclusive(False)
                self.setChecked(False)
                self.setAutoExclusive(True)
        except Exception:
            traceback.print_exc()

class AnnotationEditorDialog(QDialog):

    def __init__(self, annotation: BodyAnnotation | None = None, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Body Annotation")
        self.resize(500, 520)

        self._build_sensation_section()
        self._build_motor_section()
        self._build_notes_section()
        self._build_buttons()
        self._build_main_layout()
        self._connect_signals()

        self.clear_form()

        if annotation is not None:
            self.set_from_annotation(annotation)

        print("[AnnotationEditorDialog.__init__] constructed persistent editor")

    def _build_intensity_row(
        self,
        *,
        label_text: str,
        button_group_attr: str,
        buttons_attr: str,
    ) -> QHBoxLayout:
        row = QHBoxLayout()
        row.addWidget(QLabel(label_text))

        button_group = QButtonGroup(self)
        button_group.setExclusive(True)

        buttons = []
        for i in range(1, 11):
            btn = ToggleRadioButton(str(i))
            button_group.addButton(btn, i)
            buttons.append(btn)
            row.addWidget(btn)

        row.addStretch()

        setattr(self, button_group_attr, button_group)
        setattr(self, buttons_attr, buttons)

        return row

    def _build_sensation_section(self):
        self.sensation_group_box = QGroupBox("Sensation")
        layout = QVBoxLayout(self.sensation_group_box)

        layout.addLayout(
            self._build_intensity_row(
                label_text="Intensity:",
                button_group_attr="intensity_group",
                buttons_attr="intensity_buttons",
            )
        )

        sensation_type_row = QHBoxLayout()
        sensation_type_row.addWidget(QLabel("Sensation:"))
        self.sensation_combo = QComboBox()
        self.sensation_combo.addItems(SENSATION_OPTIONS)
        sensation_type_row.addWidget(self.sensation_combo)
        layout.addLayout(sensation_type_row)

        temporal_row = QHBoxLayout()
        temporal_row.addWidget(QLabel("Temporal Quality:"))
        self.temporal_combo = QComboBox()
        self.temporal_combo.addItems(TEMPORAL_QUALITY_OPTIONS)
        temporal_row.addWidget(self.temporal_combo)
        layout.addLayout(temporal_row)

        bilateral_row = QHBoxLayout()
        bilateral_row.addWidget(QLabel("Bilateral?"))

        self.bilateral_group = QButtonGroup(self)
        self.bilateral_group.setExclusive(True)

        self.bilateral_yes = QRadioButton("Yes")
        self.bilateral_no = QRadioButton("No")

        self.bilateral_group.addButton(self.bilateral_yes)
        self.bilateral_group.addButton(self.bilateral_no)

        self.bilateral_no.setChecked(True)

        bilateral_row.addWidget(self.bilateral_yes)
        bilateral_row.addWidget(self.bilateral_no)
        bilateral_row.addStretch()
        layout.addLayout(bilateral_row)

    def _build_motor_section(self):
        self.motor_group_box = QGroupBox("Motor")
        layout = QVBoxLayout(self.motor_group_box)

        threshold_row = QHBoxLayout()
        threshold_row.addWidget(QLabel("Motor threshold reached?"))

        self.motor_threshold_group = QButtonGroup(self)
        self.motor_threshold_group.setExclusive(True)

        self.motor_threshold_yes = QRadioButton("Yes")
        self.motor_threshold_no = QRadioButton("No")

        self.motor_threshold_group.addButton(self.motor_threshold_yes)
        self.motor_threshold_group.addButton(self.motor_threshold_no)

        self.motor_threshold_no.setChecked(True)

        threshold_row.addWidget(self.motor_threshold_yes)
        threshold_row.addWidget(self.motor_threshold_no)
        threshold_row.addStretch()
        layout.addLayout(threshold_row)

        layout.addLayout(
            self._build_intensity_row(
                label_text="Intensity:",
                button_group_attr="motor_intensity_group",
                buttons_attr="motor_intensity_buttons",
            )
        )

        motor_quality_row = QHBoxLayout()
        motor_quality_row.addWidget(QLabel("Quality:"))
        self.motor_quality_combo = QComboBox()
        self.motor_quality_combo.addItems(MOTOR_QUALITY)
        motor_quality_row.addWidget(self.motor_quality_combo)
        layout.addLayout(motor_quality_row)

        motor_temporal_row = QHBoxLayout()
        motor_temporal_row.addWidget(QLabel("Temporal Quality:"))
        self.motor_temporal_combo = QComboBox()
        self.motor_temporal_combo.addItems(TEMPORAL_QUALITY_OPTIONS)
        motor_temporal_row.addWidget(self.motor_temporal_combo)
        layout.addLayout(motor_temporal_row)

    def _build_notes_section(self):
        self.notes_group_box = QGroupBox("Additional Notes")
        layout = QVBoxLayout(self.notes_group_box)

        self.additional_notes_edit = QTextEdit()
        layout.addWidget(self.additional_notes_edit)

    def _build_buttons(self):
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

    def _build_main_layout(self):
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.sensation_group_box)
        main_layout.addWidget(self.motor_group_box)
        main_layout.addWidget(self.notes_group_box)
        main_layout.addWidget(self.button_box)

    def _connect_signals(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.motor_threshold_yes.toggled.connect(self.update_motor_controls_enabled_state)
        self.motor_threshold_no.toggled.connect(self.update_motor_controls_enabled_state)

    def update_motor_controls_enabled_state(self):
        enabled = self.motor_threshold_yes.isChecked()

        for btn in self.motor_intensity_buttons:
            btn.setEnabled(enabled)

        self.motor_quality_combo.setEnabled(enabled)
        self.motor_temporal_combo.setEnabled(enabled)

        if not enabled:
            self.motor_intensity_group.setExclusive(False)
            for btn in self.motor_intensity_buttons:
                btn.setChecked(False)
            self.motor_intensity_group.setExclusive(True)

            self.motor_quality_combo.setCurrentIndex(0)
            self.motor_temporal_combo.setCurrentIndex(0)

    def set_from_annotation(self, annotation: BodyAnnotation):
        if 1 <= annotation.intensity <= 10:
            button = self.intensity_group.button(annotation.intensity)
            if button is not None:
                button.setChecked(True)

        idx = self.sensation_combo.findText(annotation.sensation)
        if idx >= 0:
            self.sensation_combo.setCurrentIndex(idx)

        idx = self.temporal_combo.findText(annotation.temporal_quality)
        if idx >= 0:
            self.temporal_combo.setCurrentIndex(idx)

        if getattr(annotation, "bilateral", False):
            self.bilateral_yes.setChecked(True)
        else:
            self.bilateral_no.setChecked(True)

        if annotation.motor_threshold_reached:
            self.motor_threshold_yes.setChecked(True)
        else:
            self.motor_threshold_no.setChecked(True)

        if 1 <= annotation.motor_intensity <= 10:
            button = self.motor_intensity_group.button(annotation.motor_intensity)
            if button is not None:
                button.setChecked(True)

        idx = self.motor_quality_combo.findText(annotation.motor_quality)
        if idx >= 0:
            self.motor_quality_combo.setCurrentIndex(idx)

        idx = self.motor_temporal_combo.findText(annotation.motor_temporal_quality)
        if idx >= 0:
            self.motor_temporal_combo.setCurrentIndex(idx)

        self.additional_notes_edit.setPlainText(annotation.additional_notes)
        self.update_motor_controls_enabled_state()

    def build_annotation(self, x: float, y: float, created_at: datetime | None = None) -> BodyAnnotation:
        return BodyAnnotation(
            x=x,
            y=y,
            intensity=self.intensity_group.checkedId() if self.intensity_group.checkedId() != -1 else 0,
            sensation=self.sensation_combo.currentText().strip(),
            temporal_quality=self.temporal_combo.currentText().strip(),
            bilateral=self.bilateral_yes.isChecked(),
            motor_threshold_reached=self.motor_threshold_yes.isChecked(),
            motor_intensity=self.motor_intensity_group.checkedId() if self.motor_intensity_group.checkedId() != -1 else 0,
            motor_quality=self.motor_quality_combo.currentText().strip(),
            motor_temporal_quality=self.motor_temporal_combo.currentText().strip(),
            additional_notes=self.additional_notes_edit.toPlainText().strip(),
            created_at=created_at or datetime.now(),
        )

    def update_annotation(self, annotation: BodyAnnotation):
        annotation.intensity = self.intensity_group.checkedId() if self.intensity_group.checkedId() != -1 else 0
        annotation.sensation = self.sensation_combo.currentText().strip()
        annotation.temporal_quality = self.temporal_combo.currentText().strip()
        annotation.bilateral = self.bilateral_yes.isChecked()

        annotation.motor_threshold_reached = self.motor_threshold_yes.isChecked()
        annotation.motor_intensity = self.motor_intensity_group.checkedId() if self.motor_intensity_group.checkedId() != -1 else 0
        annotation.motor_quality = self.motor_quality_combo.currentText().strip()
        annotation.motor_temporal_quality = self.motor_temporal_combo.currentText().strip()

        annotation.additional_notes = self.additional_notes_edit.toPlainText().strip()

    def clear_form(self):
        self.intensity_group.setExclusive(False)
        for btn in self.intensity_buttons:
            btn.setChecked(False)
        self.intensity_group.setExclusive(True)

        self.sensation_combo.setCurrentIndex(0)
        self.temporal_combo.setCurrentIndex(0)
        self.bilateral_yes.setChecked(False)
        self.bilateral_no.setChecked(True)

        self.motor_threshold_yes.setChecked(False)
        self.motor_threshold_no.setChecked(True)

        self.motor_intensity_group.setExclusive(False)
        for btn in self.motor_intensity_buttons:
            btn.setChecked(False)
        self.motor_intensity_group.setExclusive(True)

        self.motor_quality_combo.setCurrentIndex(0)
        self.motor_temporal_combo.setCurrentIndex(0)

        self.additional_notes_edit.clear()

        self.update_motor_controls_enabled_state()

    def load_annotation(self, annotation: BodyAnnotation | None):
        self.clear_form()

        if annotation is not None:
            self.set_from_annotation(annotation)

class AnnotationMarker(QGraphicsEllipseItem):
    def __init__(self, annotation, list_item=None, dialog=None, radius=6):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius)
        self.annotation = annotation
        self.list_item = list_item
        self.dialog = dialog

        self.setPos(annotation.x, annotation.y)
        self.refresh_brush()
        self.setFlags(
            QGraphicsItem.ItemIsMovable |
            QGraphicsItem.ItemIsSelectable |
            QGraphicsItem.ItemSendsGeometryChanges
        )

    def refresh_brush(self):
        self.setBrush(QBrush(annotation_color(self.annotation)))

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            pos = self.pos()
            self.annotation.x = pos.x()
            self.annotation.y = pos.y()

            if self.list_item is not None and self.dialog is not None:
                self.list_item.setText(
                    self.dialog.format_annotation_text(self.annotation)
                )

        return super().itemChange(change, value)

    def mouseDoubleClickEvent(self, event):
        if self.dialog is not None:
            self.dialog.edit_annotation(self)
        super().mouseDoubleClickEvent(event)

    def contextMenuEvent(self, event):
        if self.dialog is None:
            return

        menu = QMenu()
        update_action = menu.addAction("Update")
        delete_action = menu.addAction("Delete")

        chosen_action = menu.exec(event.screenPos())

        if chosen_action == update_action:
            self.dialog.edit_annotation(self)
        elif chosen_action == delete_action:
            self.dialog.delete_annotation(self)

class TrialStartReviewDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Review Trial Settings")
        self.resize(900, 650)

        self.title_label = QLabel("Please review the trial settings before starting.")
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.warning_label = QLabel(
            "Please make sure that DS5 Input and Output settings match the corresponding settings on the DS5 hardware."
        )
        self.warning_label.setWordWrap(True)
        self.warning_label.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")

        self.conditions_label = QLabel("Trial Conditions")
        self.conditions_label.setStyleSheet("font-weight: bold;")

        self.conditions_table = QTableWidget(0, 4)
        self.conditions_table.setHorizontalHeaderLabels([
            "Electrode Config",
            "Waveform",
            "Polarity",
            "D188 Channel",
        ])
        self.conditions_table.verticalHeader().setVisible(False)
        self.conditions_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.conditions_table.setSelectionMode(QTableWidget.NoSelection)
        self.conditions_table.setFocusPolicy(Qt.NoFocus)
        self.conditions_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.additional_settings_label = QLabel("Additional Settings")
        self.additional_settings_label.setStyleSheet("font-weight: bold;")

        self.ds5_input_label = QLabel("DS5 Input Voltage: ")
        self.ds5_output_label = QLabel("DS5 Output Current: ")
        self.starting_current_label = QLabel("Initial Current: ")
        self.current_increment_label = QLabel("Current Increment: ")

        # Make the text under "Additional Settings" bigger
        details_style = "font-size: 15px;"

        self.ds5_input_label.setStyleSheet(details_style)
        self.ds5_output_label.setStyleSheet(details_style)
        self.starting_current_label.setStyleSheet(details_style)
        self.current_increment_label.setStyleSheet(details_style)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.button(QDialogButtonBox.Ok).setText("Confirm")
        self.button_box.button(QDialogButtonBox.Cancel).setText("Cancel")
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.title_label)
        main_layout.addSpacing(8)
        main_layout.addWidget(self.warning_label)
        main_layout.addSpacing(12)
        main_layout.addWidget(self.conditions_label)
        main_layout.addWidget(self.conditions_table)
        main_layout.addSpacing(12)
        main_layout.addWidget(self.additional_settings_label)
        main_layout.addWidget(self.ds5_input_label)
        main_layout.addWidget(self.ds5_output_label)
        main_layout.addWidget(self.starting_current_label)
        main_layout.addWidget(self.current_increment_label)
        main_layout.addStretch()
        main_layout.addWidget(self.button_box)

    def populate(self, *, conditions: dict, ds5_input: str, ds5_output: str, starting_current, current_increment: str):
        self.conditions_table.setRowCount(0)

        sorted_rows = sorted(conditions.items(), key=lambda item: item[0])

        for _, settings in sorted_rows:
            row = self.conditions_table.rowCount()
            self.conditions_table.insertRow(row)

            electrode_config = str(settings.get("electrode_config", "") or "")
            waveform = str(settings.get("waveform", "") or "")
            polarity = str(settings.get("polarity", "") or "")
            channel = str(settings.get("channel", "") or "")

            self.conditions_table.setItem(row, 0, QTableWidgetItem(electrode_config))
            self.conditions_table.setItem(row, 1, QTableWidgetItem(waveform))
            self.conditions_table.setItem(row, 2, QTableWidgetItem(polarity))
            self.conditions_table.setItem(row, 3, QTableWidgetItem(channel))

        self.ds5_input_label.setText(f"DS5 Input Voltage: {ds5_input}")
        self.ds5_output_label.setText(f"DS5 Output Current: {ds5_output}")
        self.starting_current_label.setText(f"Initial Current: {starting_current}")
        self.current_increment_label.setText(f"Current Increment: {current_increment}")

        self.setResult(0)

class PatientBodyLogDialog(QDialog):
    def __init__(self, image_path, parent=None, controller=None):
        super().__init__(parent)
        self.setWindowTitle("Patient Body Log")
        self.resize(1100, 800)

        self.controller = controller
        self.image_path = str(image_path)
        self.annotations = []
        self._pending_annotation_pos = None
        self._annotation_open_scheduled = False

        self.view = ZoomableGraphicsView()
        self.scene = BodyMapScene(parent_dialog=self)
        self.view.setScene(self.scene)
        self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.body_pixmap_item = None
        self._load_body_map_image(self.image_path)

        self.annotation_list = QListWidget()

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        main_layout = QVBoxLayout(self)
        content_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        content_layout.addWidget(self.view, 3)
        content_layout.addWidget(self.annotation_list, 1)

        self.cancel_button.setMinimumSize(120, 40)
        self.ok_button.setMinimumSize(120, 40)

        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.ok_button)
        button_layout.addStretch()

        main_layout.addLayout(content_layout)
        main_layout.addLayout(button_layout)

    def _load_body_map_image(self, image_path: str):
        print(f"Image path: {image_path}")
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            raise FileNotFoundError(f"Could not load body map image: {image_path}")

        # Remove the old pixmap item if one exists
        if self.body_pixmap_item is not None:
            try:
                self.scene.removeItem(self.body_pixmap_item)
            except Exception:
                traceback.print_exc()

        self.body_pixmap_item = self.scene.addPixmap(pixmap)
        self.scene.setSceneRect(self.body_pixmap_item.boundingRect())

    def _clear_annotation_markers(self):
        try:
            items_to_remove = []
            for item in self.scene.items():
                if isinstance(item, AnnotationMarker):
                    items_to_remove.append(item)

            for item in items_to_remove:
                self.scene.removeItem(item)

        except Exception:
            traceback.print_exc()

    def _reset_view(self):
        try:
            self.view.resetTransform()
            self.view._zoom = 1.0
        except Exception:
            traceback.print_exc()

    def reset_for_new_session(self, image_path: str | None = None):
        """
        Clear all state so the dialog behaves like a fresh new body-log window.
        """
        try:
            print("[PatientBodyLogDialog.reset_for_new_session] start")

            if image_path is not None:
                image_path = str(image_path)
                if image_path != self.image_path:
                    self.image_path = image_path
                    self._load_body_map_image(self.image_path)

            self.annotations.clear()
            self.annotation_list.clear()
            self._clear_annotation_markers()

            self._pending_annotation_pos = None
            self._annotation_open_scheduled = False

            self._reset_view()

            # Reset dialog result so exec() behaves cleanly on reuse
            self.setResult(0)

            print("[PatientBodyLogDialog.reset_for_new_session] complete")

        except Exception as e:
            print(f"[PatientBodyLogDialog.reset_for_new_session] exception: {e}")
            traceback.print_exc()
            raise

    def format_annotation_text(self, annotation) -> str:
        parts = [
            f"[{annotation.created_at.strftime('%H:%M:%S')}]",
            f"({annotation.x:.1f}, {annotation.y:.1f})",
        ]

        # Sensation
        sensation_parts = []
        if annotation.intensity:
            sensation_parts.append(f"Sens Intensity {annotation.intensity}")
        if annotation.sensation:
            sensation_parts.append(annotation.sensation)
        if annotation.temporal_quality:
            sensation_parts.append(annotation.temporal_quality)
        if sensation_parts:
            parts.append("Sensation: " + ", ".join(sensation_parts))

        # Motor
        motor_parts = [f"Threshold {'Yes' if annotation.motor_threshold_reached else 'No'}"]
        if annotation.motor_intensity:
            motor_parts.append(f"Intensity {annotation.motor_intensity}")
        if annotation.motor_quality:
            motor_parts.append(annotation.motor_quality)
        if annotation.motor_temporal_quality:
            motor_parts.append(annotation.motor_temporal_quality)
        parts.append("Motor: " + ", ".join(motor_parts))

        # Notes
        if annotation.additional_notes:
            parts.append(f"Notes: {annotation.additional_notes}")

        return " | ".join(parts)

    def add_annotation(self, annotation):
        try:
            if annotation is None:
                raise ValueError("annotation is None")

            self.annotations.append(annotation)

            list_item = QListWidgetItem(self.format_annotation_text(annotation))
            self.annotation_list.addItem(list_item)

            marker = AnnotationMarker(
                annotation=annotation,
                list_item=list_item,
                dialog=self,
            )
            self.scene.addItem(marker)

        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(
                self,
                "Annotation Error",
                f"Failed to add annotation:\n{e}"
            )

    def edit_annotation(self, marker):
        try:
            if marker is None or getattr(marker, "annotation", None) is None:
                raise ValueError("Invalid annotation marker.")

            editor = self.get_annotation_editor()
            editor.load_annotation(marker.annotation)

            print("[PatientBodyLogDialog.edit_annotation] before editor.exec()")
            result = editor.exec()
            print(f"[PatientBodyLogDialog.edit_annotation] editor.exec() returned {result}")

            if result != QDialog.Accepted:
                return

            editor.update_annotation(marker.annotation)
            marker.refresh_brush()

            if marker.list_item is not None:
                marker.list_item.setText(
                    self.format_annotation_text(marker.annotation)
                )

        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(
                self,
                "Annotation Error",
                f"Failed to edit annotation:\n{e}"
            )

    def delete_annotation(self, marker):
        try:
            if marker is None:
                return

            if marker.annotation in self.annotations:
                self.annotations.remove(marker.annotation)

            if marker.list_item is not None:
                row = self.annotation_list.row(marker.list_item)
                if row >= 0:
                    item = self.annotation_list.takeItem(row)
                    del item

            self.scene.removeItem(marker)

        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(
                self,
                "Annotation Error",
                f"Failed to delete annotation:\n{e}"
            )

    def get_patient_log(self) -> PatientBodyLog:
        """
        Return the current annotations as a PatientBodyLog.

        We only copy the list container here, not each BodyAnnotation object,
        because the dialog is about to close and these annotation objects are no
        longer being edited afterward.
        """
        try:
            print("[PatientBodyLogDialog.get_patient_log] start")
            print(f"[PatientBodyLogDialog.get_patient_log] annotation count={len(self.annotations)}")

            result = PatientBodyLog(annotations=list(self.annotations))
            print("[PatientBodyLogDialog.get_patient_log] returning PatientBodyLog")
            return result

        except Exception as e:
            print(f"[PatientBodyLogDialog.get_patient_log] exception: {e}")
            traceback.print_exc()
            raise

    def queue_annotation_open(self, x: float, y: float):
        """
        Queue opening the annotation editor after the current mouse event is fully done.
        Prevent duplicate launches if multiple events arrive close together.
        """
        try:
            print(f"[PatientBodyLogDialog.queue_annotation_open] received ({x}, {y})")

            self._pending_annotation_pos = (x, y)

            if getattr(self, "_annotation_open_scheduled", False):
                print("[PatientBodyLogDialog.queue_annotation_open] already scheduled")
                return

            self._annotation_open_scheduled = True
            print("[PatientBodyLogDialog.queue_annotation_open] scheduling _open_pending_annotation")
            QTimer.singleShot(0, self._open_pending_annotation)

        except Exception as e:
            print(f"[PatientBodyLogDialog.queue_annotation_open] exception: {e}")
            traceback.print_exc()

    def _open_pending_annotation(self):
        """
        Called after the event loop returns from the graphics-scene mouse event.
        """
        self._annotation_open_scheduled = False

        try:
            pos = getattr(self, "_pending_annotation_pos", None)
            print(f"[PatientBodyLogDialog._open_pending_annotation] pos={pos}")

            if pos is None:
                print("[PatientBodyLogDialog._open_pending_annotation] no pending position")
                return

            x, y = pos
            self._pending_annotation_pos = None

            self.open_annotation_editor_for_xy(x, y)

        except Exception as e:
            print(f"[PatientBodyLogDialog._open_pending_annotation] exception: {e}")
            traceback.print_exc()
            QMessageBox.critical(
                self,
                "Annotation Error",
                f"Failed while opening pending annotation:\n{e}"
            )

    def get_annotation_editor(self) -> AnnotationEditorDialog:
        """
        Reuse the single persistent annotation editor created on the controller.
        """
        if self.controller is None:
            raise RuntimeError("PatientBodyLogDialog.controller is None")

        editor = getattr(self.controller, "annotation_editor", None)
        if editor is None:
            raise RuntimeError("Controller has no persistent annotation_editor")

        return editor

    def open_annotation_editor_for_xy(self, x: float, y: float):
        try:
            print(f"[PatientBodyLogDialog.open_annotation_editor_for_xy] start ({x}, {y})")

            editor = self.get_annotation_editor()
            editor.load_annotation(None)

            print("[PatientBodyLogDialog.open_annotation_editor_for_xy] before editor.exec()")
            result = editor.exec()
            print(f"[PatientBodyLogDialog.open_annotation_editor_for_xy] editor.exec() returned {result}")

            if result != QDialog.Accepted:
                print("[PatientBodyLogDialog.open_annotation_editor_for_xy] cancelled")
                return

            print("[PatientBodyLogDialog.open_annotation_editor_for_xy] building annotation")
            ann = editor.build_annotation(x=x, y=y)

            print("[PatientBodyLogDialog.open_annotation_editor_for_xy] adding annotation")
            self.add_annotation(ann)
            print("[PatientBodyLogDialog.open_annotation_editor_for_xy] done")

        except Exception as e:
            print(f"[PatientBodyLogDialog.open_annotation_editor_for_xy] exception: {e}")
            traceback.print_exc()
            QMessageBox.critical(
                self,
                "Annotation Error",
                f"Failed while setting a point:\n{e}"
            )

class BodyMapScene(QGraphicsScene):
    def __init__(self, parent_dialog=None):
        super().__init__()
        self.parent_dialog = parent_dialog

    def mousePressEvent(self, event):
        try:
            print("[BodyMapScene.mousePressEvent] entered")
            print(f"[BodyMapScene.mousePressEvent] button={event.button()} scenePos=({event.scenePos().x()}, {event.scenePos().y()})")

            if event.button() != Qt.LeftButton:
                print("[BodyMapScene.mousePressEvent] non-left click -> super")
                super().mousePressEvent(event)
                return

            if self.parent_dialog is None:
                print("[BodyMapScene.mousePressEvent] parent_dialog is None -> super")
                super().mousePressEvent(event)
                return

            views = self.views()
            print(f"[BodyMapScene.mousePressEvent] len(views)={len(views)}")
            if not views:
                print("[BodyMapScene.mousePressEvent] no views -> super")
                super().mousePressEvent(event)
                return

            view = views[0]
            print("[BodyMapScene.mousePressEvent] got first view")

            item = self.itemAt(event.scenePos(), view.transform())
            print(f"[BodyMapScene.mousePressEvent] item={item!r}")

            clicked_background = (
                item is None or
                item == getattr(self.parent_dialog, "body_pixmap_item", None)
            )
            print(f"[BodyMapScene.mousePressEvent] clicked_background={clicked_background}")

            if not clicked_background:
                print("[BodyMapScene.mousePressEvent] not background -> super")
                super().mousePressEvent(event)
                return

            x = float(event.scenePos().x())
            y = float(event.scenePos().y())
            print(f"[BodyMapScene.mousePressEvent] storing pending point ({x}, {y})")

            event.accept()
            self.parent_dialog.queue_annotation_open(x, y)
            print("[BodyMapScene.mousePressEvent] queued annotation open")
            return

        except Exception as e:
            print(f"[BodyMapScene.mousePressEvent] exception: {e}")
            traceback.print_exc()
            if self.parent_dialog is not None:
                QMessageBox.critical(
                    self.parent_dialog,
                    "Annotation Error",
                    f"Failed while setting a point:\n{e}"
                )
            event.accept()
            return
        
class ZoomableGraphicsView(QGraphicsView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.NoDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setCursor(QCursor(Qt.CrossCursor))
        self.viewport().setCursor(QCursor(Qt.CrossCursor))

        self._zoom = 1.0
        self._min_zoom = 1.0
        self._max_zoom = 8.0
        self._zoom_step = 1.15

    def wheelEvent(self, event: QWheelEvent):
        if event.angleDelta().y() > 0:
            factor = self._zoom_step
        else:
            factor = 1 / self._zoom_step

        new_zoom = self._zoom * factor

        if new_zoom < self._min_zoom:
            factor = self._min_zoom / self._zoom
            new_zoom = self._min_zoom
        elif new_zoom > self._max_zoom:
            factor = self._max_zoom / self._zoom
            new_zoom = self._max_zoom

        if abs(new_zoom - self._zoom) < 1e-12:
            event.accept()
            return

        self.scale(factor, factor)
        self._zoom = new_zoom
        event.accept()


def _journal_json_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def _body_annotation_to_dict(ann: BodyAnnotation) -> dict:
    return {
        "x": ann.x,
        "y": ann.y,
        "intensity": ann.intensity,
        "sensation": ann.sensation,
        "temporal_quality": ann.temporal_quality,
        "bilateral": ann.bilateral,
        "motor_threshold_reached": ann.motor_threshold_reached,
        "motor_intensity": ann.motor_intensity,
        "motor_quality": ann.motor_quality,
        "motor_temporal_quality": ann.motor_temporal_quality,
        "additional_notes": ann.additional_notes,
        "created_at": ann.created_at,
    }


def _patient_body_log_to_dict(patient_log: PatientBodyLog | None) -> dict | None:
    if patient_log is None:
        return None

    return {
        "created_at": patient_log.created_at,
        "annotations": [_body_annotation_to_dict(ann) for ann in patient_log.annotations],
    }


def _patient_report_to_dict(report: PatientReport) -> dict:
    return {
        "current_intensity_ma": report.current_intensity_ma,
        "current_time": report.current_time,
        "patient_log": _patient_body_log_to_dict(report.patient_log),
    }


def _intensity_change_event_to_dict(event: IntensityChangeEvent) -> dict:
    return {
        "current_time": event.current_time,
        "trial_index": event.trial_index,
        "order_number": event.order_number,
        "electrode_config": event.electrode_config,
        "waveform": event.waveform,
        "previous_intensity_ma": event.previous_intensity_ma,
        "new_intensity_ma": event.new_intensity_ma,
        "increment_ma": event.increment_ma,
        "direction": event.direction,
    }


def _trial_condition_to_dict(condition: TrialCondition | None) -> dict | None:
    if condition is None:
        return None

    return {
        "electrode_config": condition.electrode_config,
        "waveform": condition.waveform,
        "polarity": condition.polarity,
    }


def _trial_log_entry_to_dict(trial_entry: TrialLogEntry) -> dict:
    return {
        "current_time": trial_entry.current_time,
        "condition": _trial_condition_to_dict(trial_entry.condition),
        "displayed_status": trial_entry.displayed_status,
        "order_number": trial_entry.order_number,
        "total_trial_time_seconds": trial_entry.total_trial_time_seconds,
        "patient_reports": [_patient_report_to_dict(r) for r in trial_entry.patient_reports],
    }


def _safe_widget_text(widget, default=""):
    try:
        return widget.currentText()
    except Exception:
        try:
            return widget.text()
        except Exception:
            return default


def collect_trial_ui_settings_snapshot(controller) -> dict:
    """
    Capture the trial-related UI/settings state for crash recovery.
    This is written once at the top of the JSONL backup file.
    """
    settings = {
        "captured_at": datetime.now(),
        "hardware_enabled": getattr(controller, "hardware_enabled", None),
        "trial_running": bool(getattr(controller, "trial_running", False)),
        "current_trial_index": getattr(controller, "current_trial_index", None),
        "current_intensity": getattr(controller, "current_intensity", None),
        "current_output_display": getattr(controller.ui.current_output, "text", lambda: "")(),

        # Trial-mode settings
        "timing_mode": "Auto" if controller.ui.radioButton_7.isChecked() else "Manual",
        "number_of_trials": controller.ui.spinBox_2.value(),
        "trial_length": controller.ui.spinBox_3.value(),
        "rest_period": controller.ui.spinBox_4.value(),
        "max_intensity": controller.ui.doubleSpinBox_17.value(),
        "percent_of_max": controller.ui.spinBox_5.value(),
        "starting_current": controller.ui.trial_starting_current.value(),
        "current_increment": controller.ui.comboBox.currentText(),
        "state_setting": "On" if controller.ui.radioButton_8.isChecked() else "Off",
        "displayed_condition_label": getattr(controller.ui.condition_label, "text", lambda: "")(),
        "patient_information": (
            controller.get_patient_information()
            if hasattr(controller, "get_patient_information")
            else {
                "first_name": "",
                "last_name": "",
                "patient_id": "",
            }
        ),

        # DS5 / current-related settings used by trial mode
        "ds5_trial_input": controller.ui.ds5_trial_input.currentText(),
        "ds5_trial_output": controller.ui.ds5_trial_output.currentText(),

        # Trial table content
        "trial_conditions_table": controller.collect_trial_conditions() if hasattr(controller, "collect_trial_conditions") else {},

        # Current trial settings if available
        "current_trial_settings": getattr(controller, "current_trial_settings", None),
    }

    return settings


def get_auto_backup_journal_path(controller) -> Path:
    """
    Return the current experiment's append-only autosave journal path in Trial_Backups.
    """
    existing = getattr(controller, "_auto_backup_path", None)
    if existing:
        return Path(existing)

    backup_dir = Path.cwd() / "Trial_Backups"
    backup_dir.mkdir(parents=True, exist_ok=True)

    experiment_log = getattr(controller, "experiment_log", None)
    start_time = getattr(experiment_log, "start_time", None)

    if isinstance(start_time, datetime):
        stamp = start_time.strftime("%Y-%m-%d_%H-%M-%S")
    else:
        stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    journal_path = backup_dir / f"{stamp}_AUTO_BACKUP.jsonl"
    controller._auto_backup_path = str(journal_path)
    return journal_path


def append_auto_backup_event(controller, event_type: str, payload: dict | None = None, *, show_message_on_error: bool = False):
    """
    Append one JSONL journal event.
    If the file is new/empty, first write a session header containing all trial UI settings.
    """
    try:
        journal_path = get_auto_backup_journal_path(controller)
        journal_path.parent.mkdir(parents=True, exist_ok=True)

        file_is_new = (not journal_path.exists()) or (journal_path.stat().st_size == 0)

        with open(journal_path, "a", encoding="utf-8", newline="") as f:
            if file_is_new:
                header_event = {
                    "logged_at": datetime.now(),
                    "event_type": "session_header",
                    "trial_settings_snapshot": collect_trial_ui_settings_snapshot(controller),
                }
                f.write(json.dumps(header_event, ensure_ascii=False, default=_journal_json_default) + "\n")

            event = {
                "logged_at": datetime.now(),
                "event_type": event_type,
                "trial_running": bool(getattr(controller, "trial_running", False)),
                "current_trial_index": getattr(controller, "current_trial_index", None),
                "current_intensity": getattr(controller, "current_intensity", None),
                "payload": payload if payload is not None else {},
            }

            f.write(json.dumps(event, ensure_ascii=False, default=_journal_json_default) + "\n")
            f.flush()

        print(f"[append_auto_backup_event] appended {event_type} to {journal_path}")

    except Exception as e:
        print(f"[append_auto_backup_event] exception while appending {event_type}: {e}")
        traceback.print_exc()
        if show_message_on_error:
            QMessageBox.warning(
                controller,
                "Backup Warning",
                f"Could not append autosave event:\n{e}"
            )


def get_latest_auto_backup_journal() -> Path | None:
    """
    Return the newest JSONL backup file in Trial_Backups, or None if none exist.
    """
    backup_dir = Path.cwd() / "Trial_Backups"
    if not backup_dir.exists():
        return None

    candidates = sorted(
        backup_dir.glob("*_AUTO_BACKUP.jsonl"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )

    return candidates[0] if candidates else None


def _body_annotation_from_dict(data: dict) -> BodyAnnotation:
    return BodyAnnotation(
        x=float(data.get("x", 0.0)),
        y=float(data.get("y", 0.0)),
        intensity=int(data.get("intensity", 0) or 0),
        sensation=str(data.get("sensation", "") or ""),
        temporal_quality=str(data.get("temporal_quality", "") or ""),
        bilateral=bool(data.get("bilateral", False)),
        motor_threshold_reached=bool(data.get("motor_threshold_reached", False)),
        motor_intensity=int(data.get("motor_intensity", 0) or 0),
        motor_quality=str(data.get("motor_quality", "") or ""),
        motor_temporal_quality=str(data.get("motor_temporal_quality", "") or ""),
        additional_notes=str(data.get("additional_notes", "") or ""),
        created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now(),
    )


def _patient_body_log_from_dict(data: dict | None) -> PatientBodyLog | None:
    if not data:
        return None

    annotations = [
        _body_annotation_from_dict(item)
        for item in data.get("annotations", [])
    ]

    created_at = datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now()

    return PatientBodyLog(
        annotations=annotations,
        created_at=created_at,
    )


def _patient_report_from_dict(data: dict) -> PatientReport:
    return PatientReport(
        current_intensity_ma=float(data.get("current_intensity_ma", 0.0) or 0.0),
        patient_log=_patient_body_log_from_dict(data.get("patient_log")),
        current_time=datetime.fromisoformat(data["current_time"]) if data.get("current_time") else datetime.now(),
    )


def _intensity_change_event_from_dict(data: dict) -> IntensityChangeEvent:
    return IntensityChangeEvent(
        current_time=datetime.fromisoformat(data["current_time"]) if data.get("current_time") else datetime.now(),
        trial_index=int(data.get("trial_index", 0) or 0),
        order_number=int(data.get("order_number", 0) or 0),
        electrode_config=str(data.get("electrode_config", "") or ""),
        waveform=str(data.get("waveform", "") or ""),
        previous_intensity_ma=float(data.get("previous_intensity_ma", 0.0) or 0.0),
        new_intensity_ma=float(data.get("new_intensity_ma", 0.0) or 0.0),
        increment_ma=float(data.get("increment_ma", 0.0) or 0.0),
        direction=str(data.get("direction", "") or ""),
    )


def _trial_condition_from_dict(data: dict | None) -> TrialCondition:
    if not data:
        return TrialCondition()

    return TrialCondition(
        electrode_config=str(data.get("electrode_config", "") or ""),
        waveform=str(data.get("waveform", "") or ""),
        polarity=str(data.get("polarity", "") or ""),
    )


def _trial_log_entry_from_dict(data: dict) -> TrialLogEntry:
    return TrialLogEntry(
        current_time=datetime.fromisoformat(data["current_time"]) if data.get("current_time") else datetime.now(),
        condition=_trial_condition_from_dict(data.get("condition")),
        displayed_status=str(data.get("displayed_status", "") or ""),
        patient_reports=[
            _patient_report_from_dict(item)
            for item in data.get("patient_reports", [])
        ],
        order_number=int(data.get("order_number", 0) or 0),
        total_trial_time_seconds=int(data.get("total_trial_time_seconds", 0) or 0),
    )


# def load_recovery_payload_from_jsonl(journal_path: Path) -> dict:
#     """
#     Read the JSONL backup and reconstruct enough state to resume.
#     Ignores malformed trailing lines.
#     """
#     journal_path = Path(journal_path)
#     if not journal_path.exists():
#         raise FileNotFoundError(f"Backup file not found: {journal_path}")

#     header = None
#     events = []

#     with open(journal_path, "r", encoding="utf-8") as f:
#         for line_no, raw_line in enumerate(f, start=1):
#             line = raw_line.strip()
#             if not line:
#                 continue

#             try:
#                 obj = json.loads(line)
#             except Exception:
#                 print(f"[load_recovery_payload_from_jsonl] skipping malformed line {line_no}")
#                 traceback.print_exc()
#                 continue

#             event_type = obj.get("event_type", "")
#             if event_type == "session_header" and header is None:
#                 header = obj
#             else:
#                 events.append(obj)

#     if header is None:
#         raise RuntimeError("Backup file does not contain a session_header event.")

#     trial_settings_snapshot = header.get("trial_settings_snapshot", {}) or {}

#     experiment_log = ExperimentLog()
#     if trial_settings_snapshot.get("captured_at"):
#         try:
#             experiment_log.start_time = datetime.fromisoformat(trial_settings_snapshot["captured_at"])
#         except Exception:
#             pass

#     latest_trial_entry_payload = None
#     latest_trial_order_number = None

#     for event in events:
#         event_type = event.get("event_type", "")
#         payload = event.get("payload", {}) or {}

#         if event_type == "trial_entry_created":
#             trial_entry_data = payload.get("trial_entry")
#             if trial_entry_data:
#                 trial_entry = _trial_log_entry_from_dict(trial_entry_data)

#                 # Replace existing entry of same order_number if already present
#                 replaced = False
#                 for idx, existing in enumerate(experiment_log.trial_logs):
#                     if existing.order_number == trial_entry.order_number:
#                         experiment_log.trial_logs[idx] = trial_entry
#                         replaced = True
#                         break
#                 if not replaced:
#                     experiment_log.trial_logs.append(trial_entry)

#                 latest_trial_entry_payload = trial_entry_data
#                 latest_trial_order_number = trial_entry.order_number

#         elif event_type == "patient_report_added":
#             order_number = payload.get("order_number")
#             report_data = payload.get("patient_report")

#             if order_number is None or not report_data:
#                 continue

#             report = _patient_report_from_dict(report_data)

#             target_entry = None
#             for entry in experiment_log.trial_logs:
#                 if entry.order_number == int(order_number):
#                     target_entry = entry
#                     break

#             if target_entry is not None:
#                 target_entry.patient_reports.append(report)

#         elif event_type == "trial_entry_finalized":
#             order_number = payload.get("order_number")
#             total_trial_time_seconds = payload.get("total_trial_time_seconds", 0)

#             for entry in experiment_log.trial_logs:
#                 if entry.order_number == int(order_number):
#                     entry.total_trial_time_seconds = int(total_trial_time_seconds or 0)
#                     break

#     return {
#         "journal_path": journal_path,
#         "trial_settings_snapshot": trial_settings_snapshot,
#         "experiment_log": experiment_log,
#         "latest_trial_entry_payload": latest_trial_entry_payload,
#         "latest_trial_order_number": latest_trial_order_number,
#     }


def load_recovery_payload_from_jsonl(journal_path: Path) -> dict:
    """
    Read the JSONL backup and reconstruct enough state to resume.
    Ignores malformed trailing lines.
    """
    journal_path = Path(journal_path)
    if not journal_path.exists():
        raise FileNotFoundError(f"Backup file not found: {journal_path}")

    header = None
    events = []

    stored_trial_order = None
    last_current_trial_index = None
    last_current_intensity = None

    with open(journal_path, "r", encoding="utf-8") as f:
        for line_no, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
            except Exception:
                print(f"[load_recovery_payload_from_jsonl] skipping malformed line {line_no}")
                traceback.print_exc()
                continue

            event_type = obj.get("event_type", "")

            if obj.get("current_trial_index") is not None:
                last_current_trial_index = int(obj.get("current_trial_index"))

            if obj.get("current_intensity") is not None:
                try:
                    last_current_intensity = float(obj.get("current_intensity"))
                except Exception:
                    pass

            if event_type == "session_header" and header is None:
                header = obj
            else:
                events.append(obj)

            if event_type == "experiment_started":
                payload = obj.get("payload", {}) or {}
                if payload.get("trial_order") is not None:
                    stored_trial_order = payload.get("trial_order")

    if header is None:
        raise RuntimeError("Backup file does not contain a session_header event.")

    trial_settings_snapshot = header.get("trial_settings_snapshot", {}) or {}

    experiment_log = ExperimentLog()
    if trial_settings_snapshot.get("captured_at"):
        try:
            experiment_log.start_time = datetime.fromisoformat(trial_settings_snapshot["captured_at"])
        except Exception:
            pass

    patient_info = trial_settings_snapshot.get("patient_information", {}) or {}
    experiment_log.patient_first_name = str(patient_info.get("first_name", "") or "")
    experiment_log.patient_last_name = str(patient_info.get("last_name", "") or "")
    experiment_log.patient_id = str(patient_info.get("patient_id", "") or "")

    latest_trial_entry_payload = None
    latest_trial_order_number = None

    for event in events:
        event_type = event.get("event_type", "")
        payload = event.get("payload", {}) or {}

        if event_type == "trial_entry_created":
            trial_entry_data = payload.get("trial_entry")
            if trial_entry_data:
                trial_entry = _trial_log_entry_from_dict(trial_entry_data)

                replaced = False
                for idx, existing in enumerate(experiment_log.trial_logs):
                    if existing.order_number == trial_entry.order_number:
                        experiment_log.trial_logs[idx] = trial_entry
                        replaced = True
                        break
                if not replaced:
                    experiment_log.trial_logs.append(trial_entry)

                latest_trial_entry_payload = trial_entry_data
                latest_trial_order_number = trial_entry.order_number

        elif event_type == "patient_report_added":
            order_number = payload.get("order_number")
            report_data = payload.get("patient_report")

            if order_number is None or not report_data:
                continue

            report = _patient_report_from_dict(report_data)

            target_entry = None
            for entry in experiment_log.trial_logs:
                if entry.order_number == int(order_number):
                    target_entry = entry
                    break

            if target_entry is not None:
                target_entry.patient_reports.append(report)

        elif event_type == "trial_entry_finalized":
            order_number = payload.get("order_number")
            total_trial_time_seconds = payload.get("total_trial_time_seconds", 0)

            for entry in experiment_log.trial_logs:
                if entry.order_number == int(order_number):
                    entry.total_trial_time_seconds = int(total_trial_time_seconds or 0)
                    break

        elif event_type == "intensity_changed":
            event_data = payload.get("intensity_change_event")
            if event_data:
                experiment_log.intensity_change_events.append(
                    _intensity_change_event_from_dict(event_data)
                )

    return {
        "journal_path": journal_path,
        "trial_settings_snapshot": trial_settings_snapshot,
        "experiment_log": experiment_log,
        "latest_trial_entry_payload": latest_trial_entry_payload,
        "latest_trial_order_number": latest_trial_order_number,
        "stored_trial_order": stored_trial_order,
        "last_current_trial_index": last_current_trial_index,
        "last_current_intensity": last_current_intensity,
    }


def _rebuild_trial_order_from_snapshot(trial_settings_snapshot: dict, stored_trial_order=None) -> list[tuple[int, dict]]:
    """
    Rebuild controller.trial_order from recovery data.

    Priority:
    1) exact stored randomized trial_order from the journal
    2) fallback to trial_conditions_table from the session header
    """
    if stored_trial_order:
        rebuilt = []
        for item in stored_trial_order:
            if not isinstance(item, (list, tuple)) or len(item) != 2:
                continue

            raw_key, raw_settings = item
            try:
                row = int(raw_key)
            except Exception:
                row = raw_key

            settings = dict(raw_settings or {})
            rebuilt.append((row, settings))

        if rebuilt:
            return rebuilt

    table = trial_settings_snapshot.get("trial_conditions_table", {}) or {}
    rebuilt = []

    for raw_key, raw_settings in table.items():
        try:
            row = int(raw_key)
        except Exception:
            row = raw_key

        settings = dict(raw_settings or {})
        rebuilt.append((row, settings))

    rebuilt.sort(key=lambda item: item[0] if isinstance(item[0], int) else str(item[0]))
    return rebuilt


def _find_matching_trial_index(controller, trial_entry_payload: dict | None) -> int | None:
    """
    Find the matching trial index in controller.trial_order for a recovered trial entry.
    """
    if not trial_entry_payload:
        return None

    condition = trial_entry_payload.get("condition", {}) or {}

    target_electrode_config = str(condition.get("electrode_config", "") or "")
    target_waveform = str(condition.get("waveform", "") or "")
    target_polarity = str(condition.get("polarity", "") or "")

    for idx, (_, settings) in enumerate(getattr(controller, "trial_order", [])):
        if (
            str(settings.get("electrode_config", "") or "") == target_electrode_config
            and str(settings.get("waveform", "") or "") == target_waveform
            and str(settings.get("polarity", "") or "") == target_polarity
        ):
            return idx

    return None


def apply_recovered_trial_settings(controller, recovery_payload: dict):
    """
    Restore experiment state onto the controller and resume from the recovered trial.
    """
    trial_settings_snapshot = recovery_payload["trial_settings_snapshot"]
    experiment_log = recovery_payload["experiment_log"]
    latest_trial_entry_payload = recovery_payload["latest_trial_entry_payload"]
    latest_trial_order_number = recovery_payload["latest_trial_order_number"]
    journal_path = recovery_payload["journal_path"]
    stored_trial_order = recovery_payload.get("stored_trial_order")
    last_current_trial_index = recovery_payload.get("last_current_trial_index")
    last_current_intensity = recovery_payload.get("last_current_intensity")

    controller.experiment_log = experiment_log
    controller._auto_backup_path = str(journal_path)
    controller.trial_running = True
    controller.recovered_session = True

    patient_info = trial_settings_snapshot.get("patient_information", {}) or {}
    if hasattr(controller, "ui"):
        if hasattr(controller.ui, "patient_first_name_input"):
            controller.ui.patient_first_name_input.setText(str(patient_info.get("first_name", "") or ""))
        if hasattr(controller.ui, "patient_last_name_input"):
            controller.ui.patient_last_name_input.setText(str(patient_info.get("last_name", "") or ""))
        if hasattr(controller.ui, "patient_id_input"):
            controller.ui.patient_id_input.setText(str(patient_info.get("patient_id", "") or ""))

    # Restore UI trial settings from snapshot first
    try:
        starting_current = float(
            trial_settings_snapshot.get(
                "starting_current",
                controller.ui.trial_starting_current.value()
            )
        )
    except Exception:
        starting_current = float(controller.ui.trial_starting_current.value())

    controller.ui.trial_starting_current.setValue(starting_current)

    increment_text = str(
        trial_settings_snapshot.get(
            "current_increment",
            controller.ui.comboBox.currentText()
        )
    ).strip()
    increment_idx = controller.ui.comboBox.findText(increment_text)
    if increment_idx >= 0:
        controller.ui.comboBox.setCurrentIndex(increment_idx)
    else:
        print(f"[apply_recovered_trial_settings] warning: current increment {increment_text!r} not found in comboBox")

    # Rebuild exact trial_order from stored randomized order if available
    controller.trial_order = _rebuild_trial_order_from_snapshot(
        trial_settings_snapshot,
        stored_trial_order=stored_trial_order,
    )

    if not controller.trial_order:
        raise RuntimeError("Recovered backup does not contain any trial conditions.")

    # Prefer the exact last current_trial_index stored in the journal
    if last_current_trial_index is not None:
        recovered_index = int(last_current_trial_index)
    else:
        recovered_index = _find_matching_trial_index(controller, latest_trial_entry_payload)
        if recovered_index is None:
            recovered_index = max(0, int(latest_trial_order_number or 1) - 1)

    recovered_index = max(0, min(recovered_index, len(controller.trial_order) - 1))
    controller.current_trial_index = recovered_index

    # Explicitly restore current trial settings
    _, recovered_settings = controller.trial_order[controller.current_trial_index]
    controller.current_trial_settings = dict(recovered_settings or {})

    # Per your stated behavior, resume at starting_current
    controller.current_intensity = starting_current
    controller.current_v_max = 0.0

    # Reflect current in UI
    controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")
    controller.ui.stackedWidget.setCurrentWidget(controller.ui.trial_running_page)
    if hasattr(controller, "update_system_status_visibility"):
        controller.update_system_status_visibility()
    controller.ui.radioButton_8.setChecked(True)

    # Start timers fresh for resumed session
    controller.start_experiment_timers()

    # Load the recovered condition into the live UI/runtime
    load_trial_settings(controller)

    # Force current back to starting_current after load_trial_settings
    controller.current_intensity = starting_current
    controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")

    # Refresh decrease button state now that increment/current are restored
    if hasattr(controller, "disable_descrease"):
        controller.disable_descrease()

    # Only reapply if current_trial_settings still exists after load_trial_settings
    if hasattr(controller, "current_trial_settings") and controller.current_trial_settings:
        apply_current_trial_settings(controller)
    else:
        raise RuntimeError("Recovery failed to restore current_trial_settings.")

    print(f"[apply_recovered_trial_settings] resumed from backup {journal_path}")
    print(f"[apply_recovered_trial_settings] recovered trial index={controller.current_trial_index}")
    print(f"[apply_recovered_trial_settings] restored starting current={controller.current_intensity}")
    print(f"[apply_recovered_trial_settings] restored current increment={controller.ui.comboBox.currentText()!r}")


def maybe_prompt_resume_from_backup(controller):
    """
    If a backup journal exists, ask the user whether to resume.
    If the user declines, delete that backup file.
    """
    try:
        journal_path = get_latest_auto_backup_journal()
        if journal_path is None:
            return

        reply = QMessageBox.question(
            controller,
            "Resume Experiment?",
            "It appears as if the system crashed during an experiment, would you like to resume the experiment from where you left off?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            recovery_payload = load_recovery_payload_from_jsonl(journal_path)
            apply_recovered_trial_settings(controller, recovery_payload)
            return

        # User chose No -> delete the backup file
        try:
            if journal_path.exists():
                journal_path.unlink()
                print(f"[maybe_prompt_resume_from_backup] deleted declined backup {journal_path}")
        except Exception as delete_exc:
            print(f"[maybe_prompt_resume_from_backup] failed to delete declined backup: {delete_exc}")
            traceback.print_exc()

    except Exception as e:
        traceback.print_exc()
        QMessageBox.warning(
            controller,
            "Crash Recovery Warning",
            f"Could not resume experiment from backup:\n{e}"
        )


def simulate_crash_now():
    """
    Hard crash helper for testing recovery.
    """
    print("[simulate_crash_now] forcing process exit for crash-recovery test")
    os._exit(1)


def setup_crash_test_timer(controller, timeout_ms: int = 60000):
    """
    Start a one-shot timer that will force a simulated crash after timeout_ms.
    Intended for crash-recovery testing during active experiments.
    """
    try:
        existing = getattr(controller, "_crash_test_timer", None)
        if existing is not None:
            existing.stop()

        timer = QTimer(controller)
        timer.setSingleShot(True)
        timer.timeout.connect(simulate_crash_now)
        timer.start(timeout_ms)

        controller._crash_test_timer = timer
        print(f"[setup_crash_test_timer] crash timer armed for {timeout_ms} ms")

    except Exception:
        traceback.print_exc()


def stop_crash_test_timer(controller):
    try:
        timer = getattr(controller, "_crash_test_timer", None)
        if timer is not None:
            timer.stop()
    except Exception:
        traceback.print_exc()


def start_trial(controller, conditions, auto_man):

    '''
    Start timer using datetime or time module to track trial duration
    Track state changes, time of change, intensity of output, electrode configuration, waveform

    Manual Mode
    ------------
    - Control is given to the user or practicioner to increase intensity. Program is randomized and order automatically generated.
    - User presses start, and the first program starts at a low intensity. User presses UP/DOWN to increase/decrease intensity, in increments of 2.5mA?
    - Opportunity is given to log data at each intensity.
    - Next program buttons and abort buttons at top of screen.
    - Other controls are hidden until trial is complete, LED light off on the D188.
    
    Conditions
    -----------
    - Active w/Normal Waveform
    - Active w/Sham Waveform
    - Sham w/Normal Waveform
    - Sham w/Sham Waveform
    - DO-I w/Normal Waveform

    For each condition, random selection between whether user is told active or sham.
    Indicate this with colors and even music.

    Operation
    -----------
    
    - Randomize order of conditions.
    - Assign each condition as active/sham
    - Initiate program. 
    
    Run loop that iterates based on number of trials
    For each trial, randomly select a number
    Make sure this number has not been selected yet. If it has, randomly select again until you get a unique number.
    Use this number to select the condition.


    Random number generator to select between:

        - Active
        - Sham
        - Lessebo
        - Nocebo
    
    '''

    print("Starting trial with current settings...")
    print("Trial started! (This is a placeholder - implement trial logic here)")

    print("Starting trial with current settings...")

    controller.start_experiment_timers()

    controller.trial_order = list(conditions.items())
    random.shuffle(controller.trial_order)

    row_keys = list(conditions.keys())
    random.shuffle(row_keys)

    print(f"Randomized row order: {row_keys}")

    for row in row_keys:
        settings = conditions[row]
        electrode_config = settings.get("electrode_config", "")
        waveform = settings.get("waveform", "")
        polarity = settings.get("polarity", "")
        channel = settings.get("channel", "")

        print(f"\nRow {row}:")
        print(f"  Electrode Config: {electrode_config}")
        print(f"  Waveform: {waveform}")
        print(f"  Polarity: {polarity}")
        print(f"  Channel: {channel}")

    # controller.current_trial_index = 0
    # controller.trial_running = True
    # controller.current_v_max = 0.0
    # controller.current_intensity = controller.ui.trial_starting_current.value()
    # controller.experiment_log = ExperimentLog()

    # # Initialize simple auto-backup path in Trial_Logs and save initial state.
    # controller._auto_backup_path = None
    # save_auto_backup_log(controller, show_message_on_error=False)


    controller.current_trial_index = 0
    controller.trial_running = True
    controller.current_v_max = 0.0
    controller.current_intensity = controller.ui.trial_starting_current.value()
    controller.experiment_log = ExperimentLog()
    if hasattr(controller, "get_patient_information"):
        patient_info = controller.get_patient_information()
        controller.experiment_log.patient_first_name = patient_info.get("first_name", "")
        controller.experiment_log.patient_last_name = patient_info.get("last_name", "")
        controller.experiment_log.patient_id = patient_info.get("patient_id", "")
    controller.recovered_session = False

    # Initialize append-only autosave journal.
    controller._auto_backup_path = None
    append_auto_backup_event(
        controller,
        "experiment_started",
        payload={
            "experiment_start_time": controller.experiment_log.start_time,
            "trial_order": controller.trial_order,
        },
        show_message_on_error=False,
    )

    # Arm simulated crash timer for testing by default.
    if getattr(controller, "enable_crash_test_timer", False):
        setup_crash_test_timer(controller, timeout_ms=60000)
    else:
        stop_crash_test_timer(controller)

    print(f'Current Time: {controller.experiment_log.start_time}')
    load_trial_settings(controller)
    controller.ui.radioButton_8.setChecked(True)
    controller.change_state()

    return


def finalize_current_trial_log_entry(controller):
    if not hasattr(controller, "experiment_log") or controller.experiment_log is None:
        return

    if not controller.experiment_log.trial_logs:
        return

    trial_entry = controller.experiment_log.trial_logs[-1]
    trial_entry.total_trial_time_seconds = controller.get_current_trial_elapsed_seconds()

    append_auto_backup_event(
        controller,
        "trial_entry_finalized",
        payload={
            "order_number": trial_entry.order_number,
            "total_trial_time_seconds": trial_entry.total_trial_time_seconds,
        },
        show_message_on_error=False,
    )


def load_trial_settings(controller):

    print("Loading trial settings for current trial...")

    if not controller.trial_running:
        return
    
    
    # Finalize the previous trial before loading a new one
    if controller.current_trial_index > 0 and controller.experiment_log.trial_logs:
        previous_order_number = controller.current_trial_index
        last_logged_order_number = controller.experiment_log.trial_logs[-1].order_number

        if last_logged_order_number == previous_order_number:
            finalize_current_trial_log_entry(controller)

    if not (0 <= controller.current_trial_index < len(controller.trial_order)):

        # Finalize the last trial before ending
        finalize_current_trial_log_entry(controller)

        # Capture total experiment time before stopping timers
        if hasattr(controller, "experiment_log") and controller.experiment_log is not None:
            controller.experiment_log.total_experiment_time_seconds = (
                controller.get_total_experiment_elapsed_seconds()
            )

        cancelled = prompt_save_after_trial(controller)
        if cancelled:
            return

        print("No more trials.")
        controller.trial_running = False
        controller.stop_timers()
        controller.ui.stackedWidget.setCurrentWidget(controller.ui.trial_settings_page)
        if hasattr(controller, "update_system_status_visibility"):
            controller.update_system_status_visibility()
        print_patient_log_counts(controller)

        controller.ui.radioButton_9.setChecked(True)
        controller.change_state()

        return

 
    controller.ui.trial_number.setText(f"Trial {controller.current_trial_index + 1}/{len(controller.trial_order)}")

    # Dynamic coding
    # Change/disable options at the top of the screen based on trial index
    if controller.current_trial_index == 0:
        controller.ui.previous_config.setEnabled(False)
    else:
        controller.ui.previous_config.setEnabled(True)

    # Change button text depending on trial number
    if controller.current_trial_index == len(controller.trial_order) - 1:
        controller.ui.next_config.setText("Finish")
    else:
        controller.ui.next_config.setText("Next Config")

    # Reset current intensity to starting value for each trial
    controller.current_intensity = controller.ui.trial_starting_current.value()

    controller.start_new_trial_timer()
    # Display current current intensity in the UI
    controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")

    row, settings = controller.trial_order[controller.current_trial_index]
    controller.current_trial_settings = settings

    print(f"Loading trial from row {row}: {settings}")

    electrode_config = settings.get("electrode_config", "")
    waveform = settings.get("waveform", "")
    polarity = settings.get("polarity", "")
    channel = settings.get("channel", "")

    existing_trial_entry = None
    for entry in controller.experiment_log.trial_logs:
        if entry.order_number == controller.current_trial_index + 1:
            existing_trial_entry = entry
            break

    if existing_trial_entry is not None:
        display_text = existing_trial_entry.displayed_status
    else:
        display_text = random.choice(["Sham", "Active"])

    controller.ui.condition_label.setText(display_text)
    update_display_status_colour(controller, display_text)

    # Update experiment log with new trial entry only if it does not already exist
    if existing_trial_entry is None:
        trial_entry = TrialLogEntry(
            condition=TrialCondition(
                electrode_config=electrode_config,
                waveform=waveform,
                polarity=polarity
            ),
            displayed_status=display_text,
            order_number=controller.current_trial_index + 1
        )
        controller.experiment_log.trial_logs.append(trial_entry)

        append_auto_backup_event(
            controller,
            "trial_entry_created",
            payload={
                "trial_entry": _trial_log_entry_to_dict(trial_entry),
            },
            show_message_on_error=False,
        )
    else:
        trial_entry = existing_trial_entry


    print(f'Current trial index: {controller.experiment_log.trial_logs[-1].order_number}')
    print (f'Current electrode config: {controller.experiment_log.trial_logs[-1].condition.electrode_config}')

    apply_current_trial_settings(controller)
    
    return


def build_trial_stateful_kwargs(controller):
    settings = getattr(controller, "current_trial_settings", None)
    if not settings:
        raise RuntimeError("controller.current_trial_settings is missing or empty.")

    waveform = settings.get("waveform", "")
    channel = settings.get("channel", "")
    polarity = settings.get("polarity", "")

    reverse = True if polarity == "Reversed" else False
    state = 1 if controller.ui.radioButton_8.isChecked() and getattr(controller, "trial_running", True) else 0
    freq_hz = 30

    if waveform == "Active":
        shape = "pulse"
        charge_balance = 1
        pw = 1
        custom = 'no'
        auto_k = False
        pph = 0
        ppw = 0
        ramp = "no"

    elif waveform == "Sham":
        shape = "pulse"
        custom = "yes"
        ramp = "yes"
        pw = 0.2
        charge_balance = 1
        auto_k = True
        pph = 0.4
        ppw = 0.8

    else:
        raise ValueError(f"Unsupported waveform: {waveform!r}")

    v_out = calc_v_from_i_ds5(controller)

    kwargs = dict(
        shape=shape,
        channel=1,
        state=state,
        d188=True,
        d188_channel=channel,
        charge_balance=charge_balance,
        reverse=reverse,
        auto_k=auto_k,
        pph=pph,
        ppw=ppw,
        pw=pw,
        ramp=ramp,
        custom=custom,
        v_min=0,
        v_max=v_out,
        d188_led=False,
    )

    if freq_hz != 0:
        kwargs["freq"] = freq_hz

    return kwargs


def apply_current_trial_settings(controller):
    print("Applying current trial settings to the system...")

    kwargs = build_trial_stateful_kwargs(controller)
    controller.request_trial_apply(kwargs)

    return
  

def record_intensity_change(controller, *, previous_intensity: float, new_intensity: float, increment: float, direction: str):
    experiment_log = getattr(controller, "experiment_log", None)
    if experiment_log is None:
        print("[record_intensity_change] experiment_log is missing; skipping intensity-change log.")
        return

    settings = getattr(controller, "current_trial_settings", {}) or {}

    event = IntensityChangeEvent(
        current_time=datetime.now(),
        trial_index=int(getattr(controller, "current_trial_index", 0) or 0),
        order_number=int(getattr(controller, "current_trial_index", 0) or 0) + 1,
        electrode_config=str(settings.get("electrode_config", "") or ""),
        waveform=str(settings.get("waveform", "") or ""),
        previous_intensity_ma=float(previous_intensity),
        new_intensity_ma=float(new_intensity),
        increment_ma=float(increment),
        direction=direction,
    )

    if not hasattr(experiment_log, "intensity_change_events"):
        experiment_log.intensity_change_events = []

    experiment_log.intensity_change_events.append(event)

    append_auto_backup_event(
        controller,
        "intensity_changed",
        payload={
            "intensity_change_event": _intensity_change_event_to_dict(event),
        },
        show_message_on_error=False,
    )


def increase_intensity(controller, inc = False):
    print("Increasing intensity...")

    if getattr(controller, "trial_hw_busy", False):
        print("Trial hardware busy; ignoring increase.")
        return

    previous_intensity = float(controller.current_intensity)

    if not inc:
        increment_val = float(controller.ui.comboBox.currentText())
        controller.current_intensity += increment_val
        controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")
    
    else:
        increment_val = 0.5
        controller.current_intensity += increment_val
        controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")


    record_intensity_change(
        controller,
        previous_intensity=previous_intensity,
        new_intensity=float(controller.current_intensity),
        increment=increment_val,
        direction="increase",
    )

    kwargs = build_trial_stateful_kwargs(controller)
    controller.request_trial_apply(kwargs)

    return


def decrease_intensity(controller, inc = False):
    print("Decreasing intensity...")

    if getattr(controller, "trial_hw_busy", False):
        print("Trial hardware busy; ignoring decrease.")
        return

    previous_intensity = float(controller.current_intensity)
    intensity_changed = False

    if not inc:    
        increment_val = float(controller.ui.comboBox.currentText())

        if (controller.current_intensity - increment_val) >= 0:
            controller.current_intensity -= increment_val
            intensity_changed = True
    
    else:
        increment_val = 0.5

        if (controller.current_intensity - increment_val) >= 0:
            controller.current_intensity -= increment_val
            intensity_changed = True


    controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")

    if intensity_changed:
        record_intensity_change(
            controller,
            previous_intensity=previous_intensity,
            new_intensity=float(controller.current_intensity),
            increment=increment_val,
            direction="decrease",
        )

    kwargs = build_trial_stateful_kwargs(controller)
    controller.request_trial_apply(kwargs)

    return


def _json_converter_for_logs(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def delete_auto_backup_log(controller, *, show_message_on_error: bool = False):
    """
    Delete the current experiment's auto-backup file from Trial_Logs.
    """
    try:
        backup_path = getattr(controller, "_auto_backup_path", None)
        if not backup_path:
            return

        backup_path = Path(backup_path)
        if backup_path.exists():
            backup_path.unlink()
            print(f"[delete_auto_backup_log] deleted {backup_path}")

        controller._auto_backup_path = None

    except Exception as e:
        print(f"[delete_auto_backup_log] exception: {e}")
        traceback.print_exc()
        if show_message_on_error:
            QMessageBox.warning(
                controller,
                "Backup Cleanup Warning",
                f"Could not delete auto-backup log:\n{e}"
            )


def create_log(controller):
    print("[create_log] start")

    try:
        if not getattr(controller, "trial_running", False):
            print("[create_log] no active trial")
            QMessageBox.warning(controller, "Cannot Log", "No trial is currently running.")
            return

        experiment_log = getattr(controller, "experiment_log", None)
        print(f"[create_log] experiment_log exists={experiment_log is not None}")
        if experiment_log is None:
            QMessageBox.critical(controller, "Logging Error", "experiment_log is missing.")
            return

        print(f"[create_log] number of trial logs={len(experiment_log.trial_logs)}")
        if not experiment_log.trial_logs:
            QMessageBox.critical(controller, "Logging Error", "No active trial log entry exists.")
            return

        current_intensity = getattr(controller, "current_intensity", None)
        print(f"[create_log] current_intensity={current_intensity}")
        if current_intensity is None:
            QMessageBox.critical(controller, "Logging Error", "Current intensity is not available.")
            return

        print("[create_log] before open_body_log_dialog")
        patient_log = open_body_log_dialog(controller)
        print(f"[create_log] open_body_log_dialog returned {type(patient_log)}")

        if patient_log is None:
            print("[create_log] patient log dialog cancelled")
            return

        print(f"[create_log] patient_log annotation count={len(patient_log.annotations)}")
        print("[create_log] before PatientReport construction")
        report = PatientReport(
            current_intensity_ma=float(current_intensity),
            patient_log=patient_log,
        )
        print("[create_log] PatientReport constructed")

        print("[create_log] before append to experiment_log.trial_logs[-1].patient_reports")
        experiment_log.trial_logs[-1].patient_reports.append(report)
        print("[create_log] append complete")

        print("[create_log] before append_auto_backup_event")
        append_auto_backup_event(
            controller,
            "patient_report_added",
            payload={
                "order_number": experiment_log.trial_logs[-1].order_number,
                "patient_report": _patient_report_to_dict(report),
            },
            show_message_on_error=False,
        )
        print("[create_log] after append_auto_backup_event")

        print(f"[create_log] Current log time: {report.current_time}")
        print(f"[create_log] Stored {len(patient_log.annotations)} body annotation(s) in patient_log.")

    except Exception as e:
        print(f"[create_log] exception: {e}")
        traceback.print_exc()
        QMessageBox.critical(
            controller,
            "Logging Error",
            f"Failed to create trial log:\n{e}"
        )


def print_patient_log_counts(controller):
    if not hasattr(controller, "experiment_log") or controller.experiment_log is None:
        print("No experiment_log found on controller.")
        return

    for i, trial_entry in enumerate(controller.experiment_log.trial_logs, start=1):
        count = len(trial_entry.patient_reports)
        print(f"Trial entry {i}: {count} patient log(s)")


def open_body_log_dialog(controller):
    try:
        print("[open_body_log_dialog] start")

        base_dir = Path(__file__).resolve().parent
        image_path = base_dir / "Body-chart-1.png"
        print(f"[open_body_log_dialog] image_path={image_path}")

        if not image_path.exists():
            raise FileNotFoundError(f"Body map image not found: {image_path}")

        controller.image_path = str(image_path)

        dialog = getattr(controller, "patient_body_log_dialog", None)
        if dialog is None:
            raise RuntimeError("Persistent PatientBodyLogDialog is not available on controller.")

        print("[open_body_log_dialog] resetting persistent PatientBodyLogDialog")
        dialog.reset_for_new_session(controller.image_path)

        print("[open_body_log_dialog] before dialog.exec()")
        result = dialog.exec()
        print(f"[open_body_log_dialog] dialog.exec() returned result={result}")

        if result == QDialog.Accepted:
            print("[open_body_log_dialog] accepted, building patient log")
            return dialog.get_patient_log()

        print("[open_body_log_dialog] cancelled")
        return None

    except Exception as e:
        traceback.print_exc()
        QMessageBox.critical(
            controller,
            "Body Log Error",
            f"Could not open body log dialog:\n{e}"
        )
        return None


def _atomic_write_text(text: str, target_path: Path):
    """
    Atomically write text to target_path.

    We write to a temp file in the same directory first, then replace the target.
    This prevents the real file from being truncated to empty if the app crashes
    mid-write.
    """
    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    tmp_path = target_path.with_name(target_path.name + ".tmp")

    try:
        with open(tmp_path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())

        os.replace(tmp_path, target_path)

    finally:
        try:
            if tmp_path.exists():
                tmp_path.unlink()
        except Exception:
            traceback.print_exc()


def _manual_experiment_log_to_dict(experiment_log: ExperimentLog) -> dict:
    """
    Manual serializer fallback for ExperimentLog.
    Avoids dataclasses.asdict() recursion/deepcopy behavior.
    """
    return {
        "start_time": experiment_log.start_time,
        "patient_first_name": getattr(experiment_log, "patient_first_name", ""),
        "patient_last_name": getattr(experiment_log, "patient_last_name", ""),
        "patient_id": getattr(experiment_log, "patient_id", ""),
        "total_experiment_time_seconds": experiment_log.total_experiment_time_seconds,
        "intensity_change_events": [
            {
                "current_time": event.current_time,
                "trial_index": event.trial_index,
                "order_number": event.order_number,
                "electrode_config": event.electrode_config,
                "waveform": event.waveform,
                "previous_intensity_ma": event.previous_intensity_ma,
                "new_intensity_ma": event.new_intensity_ma,
                "increment_ma": event.increment_ma,
                "direction": event.direction,
            }
            for event in getattr(experiment_log, "intensity_change_events", [])
        ],
        "trial_logs": [
            {
                "current_time": trial_entry.current_time,
                "condition": {
                    "electrode_config": trial_entry.condition.electrode_config,
                    "waveform": trial_entry.condition.waveform,
                    "polarity": trial_entry.condition.polarity,
                } if trial_entry.condition is not None else None,
                "displayed_status": trial_entry.displayed_status,
                "order_number": trial_entry.order_number,
                "total_trial_time_seconds": trial_entry.total_trial_time_seconds,
                "patient_reports": [
                    {
                        "current_intensity_ma": report.current_intensity_ma,
                        "current_time": report.current_time,
                        "patient_log": {
                            "created_at": report.patient_log.created_at,
                            "annotations": [
                                {
                                    "x": ann.x,
                                    "y": ann.y,
                                    "intensity": ann.intensity,
                                    "sensation": ann.sensation,
                                    "temporal_quality": ann.temporal_quality,
                                    "bilateral": ann.bilateral,
                                    "motor_threshold_reached": ann.motor_threshold_reached,
                                    "motor_intensity": ann.motor_intensity,
                                    "motor_quality": ann.motor_quality,
                                    "motor_temporal_quality": ann.motor_temporal_quality,
                                    "additional_notes": ann.additional_notes,
                                    "created_at": ann.created_at,
                                }
                                for ann in (report.patient_log.annotations if report.patient_log is not None else [])
                            ],
                        } if report.patient_log is not None else None,
                    }
                    for report in trial_entry.patient_reports
                ],
            }
            for trial_entry in experiment_log.trial_logs
        ],
    }


def experiment_log_to_dict_with_retries(
    experiment_log: ExperimentLog,
    *,
    attempts: int = 3,
    strict: bool = True,
) -> dict | None:
    """
    Try converting experiment_log to a plain dict several times using the manual serializer.

    strict=True:
        raise if conversion fails
    strict=False:
        return None if conversion fails
    """
    last_exc = None

    for attempt in range(1, attempts + 1):
        try:
            print(f"[experiment_log_to_dict_with_retries] manual serialization attempt {attempt}/{attempts}")
            data = _manual_experiment_log_to_dict(experiment_log)
            print("[experiment_log_to_dict_with_retries] manual serialization succeeded")
            return data
        except Exception as e:
            last_exc = e
            print(f"[experiment_log_to_dict_with_retries] manual serialization failed on attempt {attempt}: {e}")
            traceback.print_exc()

    if strict:
        raise RuntimeError(f"Failed to convert experiment_log to dict: {last_exc}")

    return None


def save_experiment_log_json(
    experiment_log: ExperimentLog,
    out_dir: Path,
    image_path: str = "",
    filename: str | None = None,
    *,
    strict: bool = True,
):
    """
    Save the experiment log JSON and summary CSV.

    Behavior:
    - Creates a new folder inside out_dir named:
        {date}_{time}_experiment_log_{participant_id}_{custom_name}
    - Saves:
        experiment_log_{participant_id}.json
        experiment_summary_{participant_id}.csv
    - If participant_id is blank, the participant_id segment is omitted.
    - If filename is provided, its stem is used as {custom_name}
    """
    try:
        print(f"[save_experiment_log_json] start with out_dir={out_dir} filename={filename} strict={strict}")

        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        print(f"[save_experiment_log_json] output directory ensured at {out_dir}")

        data = experiment_log_to_dict_with_retries(
            experiment_log,
            attempts=3,
            strict=strict,
        )

        if data is None:
            print("[save_experiment_log_json] conversion failed in non-strict mode; skipping save")
            return None

        print(f"[save_experiment_log_json] experiment_log converted to dict with {len(experiment_log.trial_logs)} trial log(s)")

        def json_converter(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

        # Determine folder custom name
        if filename:
            custom_name = Path(filename).stem.strip()
        else:
            custom_name = "default"

        if not custom_name:
            custom_name = "default"

        safe_custom_name = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in custom_name)

        participant_id = str(getattr(experiment_log, "patient_id", "") or "").strip()
        safe_participant_id = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in participant_id)
        participant_id_segment = f"_{safe_participant_id}" if safe_participant_id else ""

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        experiment_dir = out_dir / f"{timestamp}_experiment_log{participant_id_segment}_{safe_custom_name}"
        experiment_dir.mkdir(parents=True, exist_ok=True)

        print(f"[save_experiment_log_json] experiment_dir created at {experiment_dir}")

        json_path = experiment_dir / f"experiment_log{participant_id_segment}.json"

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False, default=json_converter)

        print(f"Saved experiment log JSON to: {json_path}")

        export_experiment_summary_csv(
            experiment_log=experiment_log,
            experiment_dir=experiment_dir,
            filename=f"experiment_summary{participant_id_segment}.csv",
            image_path=image_path,
        )

        return json_path

    except Exception:
        traceback.print_exc()
        if strict:
            raise RuntimeError("Failed to save experiment log JSON.")
        return None


def export_experiment_summary_csv(experiment_log, experiment_dir, filename="experiment_summary.csv", image_path=""):
    """
    Export a high-level CSV summary into the experiment directory.
    """
    experiment_dir = Path(experiment_dir)
    csv_path = experiment_dir / filename

    start_time = getattr(experiment_log, "start_time", None)
    if isinstance(start_time, datetime):
        start_time_str = start_time.isoformat()
    else:
        start_time_str = str(start_time) if start_time is not None else ""

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["Field", "Value"])
        writer.writerow(["Start Time", start_time_str])
        writer.writerow(["Image Path", image_path])
        writer.writerow(["Participant First Name", getattr(experiment_log, "patient_first_name", "")])
        writer.writerow(["Participant Last Name", getattr(experiment_log, "patient_last_name", "")])
        writer.writerow(["Participant ID", getattr(experiment_log, "patient_id", "")])
        writer.writerow(["Total Experiment Time (s)", getattr(experiment_log, "total_experiment_time_seconds", 0)])
        writer.writerow([])

        writer.writerow([
            "Trial Index",
            "Electrode Config",
            "Waveform",
            "Polarity",
            "Displayed Status",
            "Number of Log Entries",
            "Total Trial Time (s)",
        ])

        for i, trial_entry in enumerate(experiment_log.trial_logs, start=1):
            condition = getattr(trial_entry, "condition", None)

            electrode_config = getattr(condition, "electrode_config", "") if condition else ""
            waveform = getattr(condition, "waveform", "") if condition else ""
            polarity = getattr(condition, "polarity", "") if condition else ""
            displayed_status = getattr(trial_entry, "displayed_status", "")
            num_logs = len(getattr(trial_entry, "patient_reports", []))

            writer.writerow([
                i,
                electrode_config,
                waveform,
                polarity,
                displayed_status,
                num_logs,
                getattr(trial_entry, "total_trial_time_seconds", 0),
            ])

    print(f"Saved experiment summary CSV to: {csv_path}")


def prompt_save_after_trial(controller):
    experiment_log = getattr(controller, "experiment_log", None)
    if experiment_log is not None and hasattr(controller, "get_patient_information"):
        patient_info = controller.get_patient_information()
        experiment_log.patient_first_name = patient_info.get("first_name", "")
        experiment_log.patient_last_name = patient_info.get("last_name", "")
        experiment_log.patient_id = patient_info.get("patient_id", "")

    reply = QMessageBox.question(
        controller,
        "Save Experiment Log",
        "Do you want to save the experiment log?",
        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
    )

    if reply == QMessageBox.Yes:
        path, _ = QFileDialog.getSaveFileName(
            controller,
            "Choose custom experiment log name",
            str(Path.cwd() / "Trial_Logs" / "my_experiment"),
            "All Files (*)"
        )

        if not path:
            print("User cancelled save dialog.")
            return None

        try:
            chosen_path = Path(path)

            # Always save final logs into Trial_Logs as requested
            trial_logs_dir = Path.cwd() / "Trial_Logs"
            trial_logs_dir.mkdir(parents=True, exist_ok=True)

            save_experiment_log_json(
                controller.experiment_log,
                trial_logs_dir,
                image_path=getattr(controller, "image_path", ""),
                filename=chosen_path.name,
                strict=True,
            )

            # Only delete backup after final save succeeds
            delete_auto_backup_log(controller, show_message_on_error=False)
            stop_crash_test_timer(controller)
    
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(
                controller,
                "Save Error",
                f"Failed to save experiment log:\n{e}"
            )
            return True

    elif reply == QMessageBox.No:
        # User intentionally chose not to save final log.
        # Delete backup file since it's no longer needed, but don't show an error message if deletion fails since it's not critical.
        delete_auto_backup_log(controller, show_message_on_error=False)
        stop_crash_test_timer(controller)
        return None

    else:
        print("User cancelled.")
        controller.current_trial_index -= 1
        return True


def update_display_status_colour(controller, display_text: str):
    display_text = (display_text or "").strip().lower()

    if display_text == "active":
        colour = "#206020"
    elif display_text == "sham":
        colour = "rgba(128, 77, 0, 180)"
    else:
        colour = None

    # if display_text == "active":
    #     colour = "rgba(32, 96, 32, 180)"
    # elif display_text == "sham":
    #     colour = "rgba(217, 140, 0, 180)"
    # else:
    #     colour = None

    if colour is None:
        controller.ui.groupBox_6.setStyleSheet("")
    else:
        controller.ui.groupBox_6.setStyleSheet(f"""
            QGroupBox {{
                background-color: {colour};
            }}
        """)


def calc_v_from_i_ds5(controller):

    v_in = controller.ui.ds5_trial_input.currentText()
    i_out = controller.ui.ds5_trial_output.currentText()
    i_set = controller.current_intensity

    v_in = float(v_in)
    i_out = float(i_out)
    v_out = v_in * (i_set / i_out)

    return v_out
