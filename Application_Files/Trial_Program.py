from __future__ import annotations
import random
import datetime
import numpy as np
import pandas as pd
from FuncGen_Selector_Function_2 import func_gen_control, func_gen_control_stateful
from dataclasses import dataclass, field
from datetime import datetime

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
from PySide6.QtCore import Qt

import json
import csv
from pathlib import Path
from dataclasses import asdict


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



class AnnotationEditorDialog(QDialog):
    def __init__(self, annotation: BodyAnnotation | None = None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Body Annotation")
        self.resize(500, 520)

        # -------------------------
        # Sensation section
        # -------------------------
        self.intensity_group = QButtonGroup(self)
        self.intensity_buttons = []

        sensation_group = QGroupBox("Sensation")
        sensation_layout = QVBoxLayout(sensation_group)

        intensity_row = QHBoxLayout()
        intensity_row.addWidget(QLabel("Intensity:"))
        for i in range(1, 6):
            btn = QRadioButton(str(i))
            self.intensity_group.addButton(btn, i)
            self.intensity_buttons.append(btn)
            intensity_row.addWidget(btn)
        intensity_row.addStretch()
        sensation_layout.addLayout(intensity_row)

        sensation_type_row = QHBoxLayout()
        sensation_type_row.addWidget(QLabel("Sensation:"))
        self.sensation_combo = QComboBox()
        self.sensation_combo.addItems(SENSATION_OPTIONS)
        sensation_type_row.addWidget(self.sensation_combo)
        sensation_layout.addLayout(sensation_type_row)

        temporal_row = QHBoxLayout()
        temporal_row.addWidget(QLabel("Temporal Quality:"))
        self.temporal_combo = QComboBox()
        self.temporal_combo.addItems(TEMPORAL_QUALITY_OPTIONS)
        temporal_row.addWidget(self.temporal_combo)
        sensation_layout.addLayout(temporal_row)

        # -------------------------
        # Motor section
        # -------------------------
        motor_group = QGroupBox("Motor")
        motor_layout = QVBoxLayout(motor_group)

        threshold_row = QHBoxLayout()
        threshold_row.addWidget(QLabel("Motor threshold reached?"))
        self.motor_threshold_group = QButtonGroup(self)
        self.motor_threshold_yes = QRadioButton("Yes")
        self.motor_threshold_no = QRadioButton("No")
        self.motor_threshold_group.addButton(self.motor_threshold_yes)
        self.motor_threshold_group.addButton(self.motor_threshold_no)
        self.motor_threshold_no.setChecked(True)

        self.motor_threshold_yes.toggled.connect(self.update_motor_controls_enabled_state)
        self.motor_threshold_no.toggled.connect(self.update_motor_controls_enabled_state)

        threshold_row.addWidget(self.motor_threshold_yes)
        threshold_row.addWidget(self.motor_threshold_no)
        threshold_row.addStretch()
        motor_layout.addLayout(threshold_row)

        motor_intensity_row = QHBoxLayout()
        motor_intensity_row.addWidget(QLabel("Intensity:"))
        self.motor_intensity_group = QButtonGroup(self)
        self.motor_intensity_buttons = []
        for i in range(1, 6):
            btn = QRadioButton(str(i))
            self.motor_intensity_group.addButton(btn, i)
            self.motor_intensity_buttons.append(btn)
            motor_intensity_row.addWidget(btn)
        motor_intensity_row.addStretch()
        motor_layout.addLayout(motor_intensity_row)

        motor_quality_row = QHBoxLayout()
        motor_quality_row.addWidget(QLabel("Quality:"))
        self.motor_quality_combo = QComboBox()
        self.motor_quality_combo.addItems(MOTOR_QUALITY)
        motor_quality_row.addWidget(self.motor_quality_combo)
        motor_layout.addLayout(motor_quality_row)

        motor_temporal_row = QHBoxLayout()
        motor_temporal_row.addWidget(QLabel("Temporal Quality:"))
        self.motor_temporal_combo = QComboBox()
        self.motor_temporal_combo.addItems(TEMPORAL_QUALITY_OPTIONS)
        motor_temporal_row.addWidget(self.motor_temporal_combo)
        motor_layout.addLayout(motor_temporal_row)

        # -------------------------
        # Additional notes
        # -------------------------
        notes_group = QGroupBox("Additional Notes")
        notes_layout = QVBoxLayout(notes_group)
        self.additional_notes_edit = QTextEdit()
        notes_layout.addWidget(self.additional_notes_edit)

        # -------------------------
        # Buttons
        # -------------------------
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(sensation_group)
        main_layout.addWidget(motor_group)
        main_layout.addWidget(notes_group)
        main_layout.addWidget(self.button_box)

        if annotation is not None:
            self.set_from_annotation(annotation)

        self.update_motor_controls_enabled_state()

    def update_motor_controls_enabled_state(self):
        enabled = self.motor_threshold_yes.isChecked()

        for btn in self.motor_intensity_buttons:
            btn.setEnabled(enabled)

        self.motor_quality_combo.setEnabled(enabled)
        self.motor_temporal_combo.setEnabled(enabled)

        if not enabled:
            # Clear motor selections when threshold is not reached
            self.motor_intensity_group.setExclusive(False)
            for btn in self.motor_intensity_buttons:
                btn.setChecked(False)
            self.motor_intensity_group.setExclusive(True)

            self.motor_quality_combo.setCurrentIndex(0)
            self.motor_temporal_combo.setCurrentIndex(0)

    def set_from_annotation(self, annotation: BodyAnnotation):
        # Sensation
        if 1 <= annotation.intensity <= 5:
            button = self.intensity_group.button(annotation.intensity)
            if button is not None:
                button.setChecked(True)

        idx = self.sensation_combo.findText(annotation.sensation)
        if idx >= 0:
            self.sensation_combo.setCurrentIndex(idx)

        idx = self.temporal_combo.findText(annotation.temporal_quality)
        if idx >= 0:
            self.temporal_combo.setCurrentIndex(idx)

        # Motor
        if annotation.motor_threshold_reached:
            self.motor_threshold_yes.setChecked(True)
        else:
            self.motor_threshold_no.setChecked(True)

        if 1 <= annotation.motor_intensity <= 5:
            button = self.motor_intensity_group.button(annotation.motor_intensity)
            if button is not None:
                button.setChecked(True)

        idx = self.motor_quality_combo.findText(annotation.motor_quality)
        if idx >= 0:
            self.motor_quality_combo.setCurrentIndex(idx)

        idx = self.motor_temporal_combo.findText(annotation.motor_temporal_quality)
        if idx >= 0:
            self.motor_temporal_combo.setCurrentIndex(idx)

        # Notes
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
    def __init__(self, image_path, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Patient Body Log")
        self.resize(1100, 800)

        self.annotations = []

        self.view = ZoomableGraphicsView()
        self.scene = BodyMapScene(parent_dialog=self)
        self.view.setScene(self.scene)
        self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        print(f"Image path: {image_path}")
        pixmap = QPixmap(image_path)
        self.body_pixmap_item = self.scene.addPixmap(pixmap)
        self.scene.setSceneRect(self.body_pixmap_item.boundingRect())

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
        self.annotations.append(annotation)

        list_item = QListWidgetItem(self.format_annotation_text(annotation))
        self.annotation_list.addItem(list_item)

        marker = AnnotationMarker(
            annotation=annotation,
            list_item=list_item,
            dialog=self,
        )
        self.scene.addItem(marker)

    def edit_annotation(self, marker):
        dialog = AnnotationEditorDialog(annotation=marker.annotation, parent=self)
        if dialog.exec() != QDialog.Accepted:
            return

        dialog.update_annotation(marker.annotation)
        marker.refresh_brush()

        if marker.list_item is not None:
            marker.list_item.setText(
                self.format_annotation_text(marker.annotation)
            )

    
    def delete_annotation(self, marker):
        # Remove from annotation model
        if marker.annotation in self.annotations:
            self.annotations.remove(marker.annotation)

        # Remove from list widget
        if marker.list_item is not None:
            row = self.annotation_list.row(marker.list_item)
            if row >= 0:
                self.annotation_list.takeItem(row)

        # Remove from scene
        self.scene.removeItem(marker)

    def get_patient_log(self) -> PatientBodyLog:
        return PatientBodyLog(
            annotations=[
                BodyAnnotation(
                    x=ann.x,
                    y=ann.y,

                    intensity=ann.intensity,
                    sensation=ann.sensation,
                    temporal_quality=ann.temporal_quality,

                    motor_threshold_reached=ann.motor_threshold_reached,
                    motor_intensity=ann.motor_intensity,
                    motor_quality=ann.motor_quality,
                    motor_temporal_quality=ann.motor_temporal_quality,

                    additional_notes=ann.additional_notes,
                    created_at=ann.created_at,
                )
                for ann in self.annotations
            ]
        )



class BodyMapScene(QGraphicsScene):
    def __init__(self, parent_dialog=None):
        super().__init__()
        self.parent_dialog = parent_dialog

    def mousePressEvent(self, event):
        item = self.itemAt(event.scenePos(), self.views()[0].transform())

        # Create a new annotation only when empty background/body image is clicked
        if item is None or item == self.parent_dialog.body_pixmap_item:
            editor = AnnotationEditorDialog(parent=self.parent_dialog)
            if editor.exec() == QDialog.Accepted:
                ann = editor.build_annotation(
                    x=event.scenePos().x(),
                    y=event.scenePos().y(),
                )
                self.parent_dialog.add_annotation(ann)

        super().mousePressEvent(event)

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

def start_trial(controller, conditions, auto_man):

    print("Starting trial with current settings...")
    # Here you would collect all the settings from the UI and start the trial logic
    # For now, we just print a message
    print("Trial started! (This is a placeholder - implement trial logic here)")

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



    controller.current_trial_index = 0
    controller.trial_running = True
    controller.current_v_max = 0.0
    controller.current_intensity = controller.ui.trial_starting_current.value()
    controller.experiment_log = ExperimentLog()

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

    controller.experiment_log.trial_logs[-1].total_trial_time_seconds = (
        controller.get_current_trial_elapsed_seconds()
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
    state = 1 if controller.ui.radioButton_8.isChecked() else 0
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
    )

    if freq_hz != 0:
        kwargs["freq"] = freq_hz

    return kwargs

def apply_current_trial_settings(controller):
    print("Applying current trial settings to the system...")

    kwargs = build_trial_stateful_kwargs(controller)
    controller.request_trial_apply(kwargs)

    return
    

# def apply_current_trial_settings(controller):

#     print("Applying current trial settings to the system...")  

#     waveform = controller.current_trial_settings.get("waveform", "")
#     channel = controller.current_trial_settings.get("channel", "")
#     polarity = controller.current_trial_settings.get("polarity", "")
#     reverse = controller.current_trial_settings.get("reverse", "")
#     state = 1 if controller.ui.radioButton_8.isChecked() else 0

#     freq_hz=30

#     print(f'waveform = {waveform}')
#     print(f'channel = {channel}')
#     print(f'polarity = {polarity}')
#     print(f'reverse = {reverse}')
#     print(f'state = {state}')

#     if (waveform == 'Active'):
#         shape = 'pulse'
#         charge_balance = 1
#         pw = 1
#         custom = 0
#         auto_k = False
#         pph = 0
#         ppw = 0
#         ramp = 'no'

#     elif (waveform == 'Sham'):
#         shape = 'pulse'
#         custom = 'yes'
#         ramp = 'yes'
#         pw = 0.2
#         charge_balance = 0
#         auto_k = True
#         pph = 0.4
#         ppw = 0.8
#         print("Sham waveform selected")


#     '''
# from FuncGen_Selector_Function_2 import func_gen_control, func_gen_control_stateful

#     func_gen_control_stateful(
#     channel=1,
#     shape = 'pulse',
#     charge_balance=False,
#     v_min = 0.0,
#     v_max= 5.0,
#     freq=30,          # example; use your real param names
#     pw=0.2,  # example; use your real param names
#     pph=0.4,
#     ppw=0.8,
#     custom='yes',
#     ramp = 'yes',
# )
#     '''

#     # Calculate output voltage based on current intensity and electrode configuration
    
#     v_out = calc_v_from_i_ds5(controller)
    
#     state = 1 if controller.ui.radioButton_8.isChecked() else 0

#     kwargs = dict(
#         shape=shape,
#         channel=1,
#         state=state,
#         d188=True,
#         d188_channel=channel,
#         charge_balance=charge_balance,
#         reverse=reverse,
#         auto_k = auto_k,
#         pph = pph,
#         ppw = ppw, 
#         pw = pw,
#         ramp = ramp,
#         custom = custom
#     )

#     if freq_hz != 0:
#         kwargs["freq"] = freq_hz

#     kwargs["v_min"] = 0
#     kwargs["v_max"] = v_out
   
#     func_gen_control_stateful(**kwargs)

#     return


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


# def increase_intensity(controller):
#     print("Increasing intensity...")

#     increment_val = float(controller.ui.comboBox.currentText())
#     controller.current_intensity += increment_val
#     controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")

#     QApplication.processEvents()

#     # Ramp increase on function generator to new voltage based on current intensity and electrode configuration
#     v_out = calc_v_from_i_ds5(controller)
#     func_gen_control_stateful(v_min = 0, v_max = v_out)

#     return

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

# def decrease_intensity(controller):
#     print("Decreasing intensity...")

#     increment_val = float(controller.ui.comboBox.currentText())

#     if ((controller.current_intensity - increment_val)>=0):
#         controller.current_intensity -= increment_val

#     controller.ui.current_output.setText(f"{controller.current_intensity:.2f}")

#     QApplication.processEvents()

#     # Ramp decrease on function generator to new voltage based on current intensity and electrode configuration
#     v_out = calc_v_from_i_ds5(controller)
#     func_gen_control_stateful(v_min = 0, v_max = v_out)

#     # Implement logic to decrease intensity, e.g. by 2.5mA increments
#     # Update the function generator settings accordingly

#     return

def create_log(controller):
    print("Creating log of trial data...")

    patient_log = open_body_log_dialog(controller)

    if patient_log is None:
        print("Patient log dialog cancelled.")
        return

    controller.experiment_log.trial_logs[-1].patient_reports.append(
        PatientReport(
            current_intensity_ma=controller.current_intensity,
            patient_log=patient_log,
        )
    )

    print(f"Current log time: {controller.experiment_log.trial_logs[-1].patient_reports[-1].current_time}")
    print(f"Stored {len(patient_log.annotations)} body annotation(s) in patient_log.")

    return


def print_patient_log_counts(controller):
    if not hasattr(controller, "experiment_log") or controller.experiment_log is None:
        print("No experiment_log found on controller.")
        return

    for i, trial_entry in enumerate(controller.experiment_log.trial_logs, start=1):
        count = len(trial_entry.patient_reports)
        print(f"Trial entry {i}: {count} patient log(s)")


def open_body_log_dialog(controller):
    controller.image_path = r"Application_Files\Body-chart-1.png"
    dialog = PatientBodyLogDialog(
        image_path=controller.image_path,
        parent=controller,
    )

    result = dialog.exec()

    if result == QDialog.Accepted:
        return dialog.get_patient_log()

    return None


def save_experiment_log_json(experiment_log, path, image_path=""):
    base_dir = Path(path)
    base_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    experiment_dir = base_dir / f"{timestamp}_Experiment_Log"
    experiment_dir.mkdir(parents=True, exist_ok=True)

    json_path = experiment_dir / f"{timestamp}_experiment_log.json"

    data = asdict(experiment_log)

    def json_converter(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False, default=json_converter)

    print(f"Saved experiment log JSON to: {json_path}")

    export_experiment_summary_csv(
        experiment_log=experiment_log,
        experiment_dir=experiment_dir,
        timestamp=timestamp,
        image_path=image_path,
    )


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

def prompt_save_experiment_log(controller):
    start_dir = Path.cwd() / "Trial_Logs"
    start_dir.mkdir(parents=True, exist_ok=True)

    path, _ = QFileDialog.getSaveFileName(
        controller,
        "Choose where to save experiment log",
        str(start_dir),
        "JSON Files (*.json);;All Files (*)"
    )

    if not path:
        print("User cancelled save.")
        return None

    return Path(path)

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
            str(Path.cwd() / "Trial_Programs" / "experiment_log.json"),
            "JSON Files (*.json);;All Files (*)"
        )
        if path:
            save_experiment_log_json(controller.experiment_log, Path(path).parent)
    elif reply == QMessageBox.No:
        pass
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
