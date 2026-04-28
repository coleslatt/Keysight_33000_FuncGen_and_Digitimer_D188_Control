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
class ExperimentLog:
    start_time: datetime = field(default_factory=datetime.now)
    trial_logs: list[TrialLogEntry] = field(default_factory=list)
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


def get_auto_backup_journal_path(controller) -> Path:
    """
    Return the current experiment's append-only autosave journal path in Trial_Logs.
    """
    existing = getattr(controller, "_auto_backup_path", None)
    if existing:
        return Path(existing)

    logs_dir = Path.cwd() / "Trial_Logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    experiment_log = getattr(controller, "experiment_log", None)
    start_time = getattr(experiment_log, "start_time", None)

    if isinstance(start_time, datetime):
        stamp = start_time.strftime("%Y-%m-%d_%H-%M-%S")
    else:
        stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    journal_path = logs_dir / f"{stamp}_AUTO_BACKUP.jsonl"
    controller._auto_backup_path = str(journal_path)
    return journal_path


def append_auto_backup_event(controller, event_type: str, payload: dict | None = None, *, show_message_on_error: bool = False):
    """
    Append one small JSONL journal event instead of rewriting the whole experiment log.
    """
    try:
        journal_path = get_auto_backup_journal_path(controller)
        journal_path.parent.mkdir(parents=True, exist_ok=True)

        event = {
            "logged_at": datetime.now(),
            "event_type": event_type,
            "trial_running": bool(getattr(controller, "trial_running", False)),
            "current_trial_index": getattr(controller, "current_trial_index", None),
            "current_intensity": getattr(controller, "current_intensity", None),
            "payload": payload if payload is not None else {},
        }

        line = json.dumps(event, ensure_ascii=False, default=_journal_json_default) + "\n"

        with open(journal_path, "a", encoding="utf-8", newline="") as f:
            f.write(line)
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

    # Initialize append-only autosave journal in Trial_Logs.
    controller._auto_backup_path = None
    append_auto_backup_event(
        controller,
        "experiment_started",
        payload={
            "experiment_start_time": controller.experiment_log.start_time,
        },
        show_message_on_error=False,
    )

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
    waveform = controller.current_trial_settings.get("waveform", "")
    channel = controller.current_trial_settings.get("channel", "")
    polarity = controller.current_trial_settings.get("polarity", "")

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
        d188_led = False,
    )

    if freq_hz != 0:
        kwargs["freq"] = freq_hz

    return kwargs


def apply_current_trial_settings(controller):
    print("Applying current trial settings to the system...")

    kwargs = build_trial_stateful_kwargs(controller)
    controller.request_trial_apply(kwargs)

    return
  

def increase_intensity(controller):
    print("Increasing intensity...")

    if getattr(controller, "trial_hw_busy", False):
        print("Trial hardware busy; ignoring increase.")
        return

    increment_val = float(controller.ui.comboBox.currentText())
    controller.current_intensity += increment_val
    controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")

    kwargs = build_trial_stateful_kwargs(controller)
    controller.request_trial_apply(kwargs)

    return


def decrease_intensity(controller):
    print("Decreasing intensity...")

    if getattr(controller, "trial_hw_busy", False):
        print("Trial hardware busy; ignoring decrease.")
        return

    increment_val = float(controller.ui.comboBox.currentText())

    if (controller.current_intensity - increment_val) >= 0:
        controller.current_intensity -= increment_val

    controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")

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


# def open_body_log_dialog(controller):
#     try:
#         print("[open_body_log_dialog] start")

#         base_dir = Path(__file__).resolve().parent
#         image_path = base_dir / "Body-chart-1.png"
#         print(f"[open_body_log_dialog] image_path={image_path}")

#         if not image_path.exists():
#             raise FileNotFoundError(f"Body map image not found: {image_path}")

#         controller.image_path = str(image_path)

#         print("[open_body_log_dialog] creating PatientBodyLogDialog")
#         dialog = PatientBodyLogDialog(
#             image_path=controller.image_path,
#             parent=controller,
#             controller=controller,
#         )
#         print("[open_body_log_dialog] dialog created successfully")

#         print("[open_body_log_dialog] before dialog.exec()")
#         result = dialog.exec()
#         print(f"[open_body_log_dialog] dialog.exec() returned result={result}")

#         if result == QDialog.Accepted:
#             print("[open_body_log_dialog] accepted, building patient log")
#             return dialog.get_patient_log()

#         print("[open_body_log_dialog] cancelled")
#         return None

#     except Exception as e:
#         traceback.print_exc()
#         QMessageBox.critical(
#             controller,
#             "Body Log Error",
#             f"Could not open body log dialog:\n{e}"
#         )
#         return None

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
        "total_experiment_time_seconds": experiment_log.total_experiment_time_seconds,
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
    Save the experiment log JSON and companion summary CSV.

    strict=True:
        final save behavior — raise if conversion or writing fails

    strict=False:
        auto-backup behavior — if conversion/save fails, return None and let caller continue
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

        print(f'[save_experiment_log_json] experiment_log_to_dict_with_retries returned data={data is not None}')

        if data is None:
            print("[save_experiment_log_json] conversion failed in non-strict mode; skipping save")
            return None

        print(f"[save_experiment_log_json] experiment_log converted to dict with {len(experiment_log.trial_logs)} trial log(s)")

        def json_converter(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

        # Serialize fully in memory first.
        json_text = json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
            default=json_converter,
        )

        print(f"[save_experiment_log_json] experiment_log serialized to JSON text with length {len(json_text)}")

        if filename is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            experiment_dir = out_dir / f"{timestamp}_Experiment_Log"
            experiment_dir.mkdir(parents=True, exist_ok=True)

            print(f"[save_experiment_log_json] experiment_dir created at {experiment_dir}")

            json_path = experiment_dir / f"{timestamp}_experiment_log.json"

            _atomic_write_text(json_text, json_path)

            print(f"Saved experiment log JSON to: {json_path}")

            export_experiment_summary_csv(
                experiment_log=experiment_log,
                experiment_dir=experiment_dir,
                timestamp=timestamp,
                image_path=image_path,
            )

            return json_path

        json_path = out_dir / filename
        json_path.parent.mkdir(parents=True, exist_ok=True)

        _atomic_write_text(json_text, json_path)

        print(f"Saved experiment log JSON to: {json_path}")

        csv_stem = json_path.stem
        export_experiment_summary_csv(
            experiment_log=experiment_log,
            experiment_dir=json_path.parent,
            timestamp=csv_stem,
            image_path=image_path,
        )

        return json_path

    except Exception:
        traceback.print_exc()
        if strict:
            raise RuntimeError("Failed to save experiment log JSON.")
        return None


def export_experiment_summary_csv(experiment_log, experiment_dir, timestamp, image_path=""):
    """
    Export a high-level CSV summary into the experiment directory.

    Rows included:
    - Start Time
    - Image Path
    - One row per trial condition, in experiment order, with log count
    """
    experiment_dir = Path(experiment_dir)
    csv_path = experiment_dir / f"{timestamp}_experiment_summary.csv"

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
    reply = QMessageBox.question(
        controller,
        "Save Experiment Log",
        "Do you want to save the experiment log?",
        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
    )

    if reply == QMessageBox.Yes:
        path, _ = QFileDialog.getSaveFileName(
            controller,
            "Choose where to save experiment log",
            str(Path.cwd() / "Trial_Logs" / "experiment_log.json"),
            "JSON Files (*.json);;All Files (*)"
        )

        if not path:
            print("User cancelled save dialog.")
            return None

        try:
            chosen_path = Path(path)
            save_experiment_log_json(
                controller.experiment_log,
                chosen_path.parent,
                image_path=getattr(controller, "image_path", ""),
                filename=chosen_path.name,
                strict=True,
            )

            # Normal successful completion of the save flow:
            delete_auto_backup_log(controller, show_message_on_error=False)

        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(
                controller,
                "Save Error",
                f"Failed to save experiment log:\n{e}"
            )
            return True  # treat as interrupted so user is not advanced silently

    elif reply == QMessageBox.No:
        # User intentionally chose not to save the final log,
        # but the experiment flow is still ending normally.
        delete_auto_backup_log(controller, show_message_on_error=False)
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
