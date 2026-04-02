# Custom controller main window

from operator import index
import sys
import traceback
import threading
import os
import time

from PySide6.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QDialog, QComboBox, QHBoxLayout, QRadioButton, QButtonGroup
from FuncGen_Selector_Function_2 import func_gen_control, func_gen_control_stateful
from burst_mode_function import burst_mode

from Trial_Program import (start_trial, 
                            load_trial_settings, 
                            increase_intensity, 
                            decrease_intensity, 
                            print_patient_log_counts, 
                            create_log,
                            prompt_save_after_trial,
                            build_trial_stateful_kwargs)

from stim_system_gui_v3 import Ui_Controller_Main

from PySide6.QtCore import QObject, QEvent, QThread, Signal, Slot, QTimer
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog
from pathlib import Path
import pandas as pd
from dataclasses import dataclass, field
from datetime import datetime


class NameOnHover(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Enter and isinstance(obj, QtWidgets.QWidget):
            name = obj.objectName() or "<no objectName>"
            obj.setToolTip(f"{name}  ({obj.metaObject().className()})")
        return super().eventFilter(obj, event)


class NoWheelFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel:
            return True
        return super().eventFilter(obj, event)
    


def enable_name_tooltips(root: QtWidgets.QWidget):
    filt = NameOnHover(root)
    # keep a reference so it doesn't get garbage-collected
    root._name_tooltip_filter = filt
    for w in root.findChildren(QtWidgets.QWidget):
        w.installEventFilter(filt)


class BurstWorker(QObject):
    finished = Signal()
    error = Signal(str)
    status = Signal(str)

    def __init__(self, burst_kwargs: dict):
        super().__init__()
        self.burst_kwargs = burst_kwargs
        self.stop_event = threading.Event()

    @Slot()
    def run(self):
        try:
            self.status.emit("Resetting function generator state...")
            func_gen_control_stateful(reset=True)

            if self.stop_event.is_set():
                self.status.emit("Burst run cancelled before start.")
                return

            self.status.emit("Burst run started.")
            burst_mode(
                **self.burst_kwargs,
                stop_event=self.stop_event,
            )

            if self.stop_event.is_set():
                self.status.emit("Burst run stopped by user.")
            else:
                self.status.emit("Burst run completed.")
        except Exception:
            self.error.emit(traceback.format_exc())
        finally:
            self.finished.emit()

    def stop(self):
        self.stop_event.set()


class TrialHardwareWorker(QObject):
    finished = Signal()
    error = Signal(str)
    status = Signal(str)

    @Slot(dict)
    def apply_settings(self, kwargs: dict):
        try:
            self.status.emit("Applying trial hardware settings...")
            func_gen_control_stateful(**kwargs)
        except Exception:
            self.error.emit(traceback.format_exc())
        finally:
            self.finished.emit()


class ControllerMain(QDialog):

    request_trial_hardware_apply = Signal(dict)

    def __init__(self):

        super().__init__()
        self.ui = Ui_Controller_Main()
        self.ui.setupUi(self)

        # Timer Logic
        # Timer Logic
        self.trial_start_monotonic = None
        self.experiment_start_monotonic = None

        self.display_timer = QTimer(self)
        self.display_timer.setInterval(1000)  # 1000 ms = 1 second
        self.display_timer.timeout.connect(self.update_timer_displays)

        self.ui.totaltime_2.setText("00:00")
        self.ui.trial_timer.setText("00:00")



        self.no_wheel_filter = NoWheelFilter()

        for w in self.findChildren(QSpinBox):
            w.installEventFilter(self.no_wheel_filter)

        for w in self.findChildren(QDoubleSpinBox):
            w.installEventFilter(self.no_wheel_filter)

        enable_name_tooltips(self)

        self.burst_thread = None
        self.burst_worker = None

        self.trial_hw_busy = False
        self.trial_hw_thread = QThread(self)
        self.trial_hw_worker = TrialHardwareWorker()
        self.trial_hw_worker.moveToThread(self.trial_hw_thread)

        self.request_trial_hardware_apply.connect(self.trial_hw_worker.apply_settings)
        self.trial_hw_worker.finished.connect(self.on_trial_hardware_finished)
        self.trial_hw_worker.error.connect(self.on_trial_hardware_error)
        self.trial_hw_worker.status.connect(self.on_trial_hardware_status)

        self.trial_hw_thread.start()

        print(f"Current working directory: {os.getcwd()}")

        # Burst Mode Defaults and Settings

        # region Continuous mode default settings
        self.ui.groupBox_16.setEnabled(False)
        self.ui.groupBox_23.setEnabled(False)
        self.ui.doubleSpinBox_8.setEnabled(False)
        self.ui.doubleSpinBox_16.setEnabled(False)
        self.ui.doubleSpinBox_7.setEnabled(False)
        self.ui.doubleSpinBox_14.setEnabled(False)
        self.ui.ch1_off.setChecked(True)
        self.ui.ch1_off_3.setChecked(True)

        self.ui.doubleSpinBox_7.setMinimum(0.001)   # Pulse Width Ch1 minimum
        self.ui.doubleSpinBox_14.setMinimum(0.001)  # Pulse Width Ch2 minimum

        self.ui.doubleSpinBox_5.setValue(1.0)   # Set default current to 1 mA for CH1
        self.ui.doubleSpinBox_11.setValue(1.0)  # Set default current to 1 mA for CH2
        self.ui.doubleSpinBox_2.setValue(60)    # Set default frequency to 60 Hz for CH1
        self.ui.doubleSpinBox_4.setValue(60)    # Set default frequency to 60 Hz for CH2
        # endregion

        # region Continuous mode dynamic UI logic
        self.ui.comboBox_2.currentTextChanged.connect(self._update_groupbox_visibility)
        self.ui.comboBox_7.currentTextChanged.connect(self._update_groupbox_visibility2)

        self.ui.tabWidget.currentChanged.connect(self.on_tab_changed_ch1)
        self.ui.tabWidget_2.currentChanged.connect(self.on_tab_changed_ch2)
        self.ui.radioButton_13.toggled.connect(self.on_radioButton_13_toggled)
        self.ui.radioButton_17.toggled.connect(self.on_radioButton_17_toggled)
        self.ui.modeSelektor.currentChanged.connect(self.tab_mode_change)

        # endregion

        # region Limits for Continuous Mode
        for sb in self.findChildren(QSpinBox):
            sb.setMaximum(10000000)
            sb.setMinimum(-10000000)

        for sb in self.findChildren(QDoubleSpinBox):
            sb.setMaximum(10000000)
            sb.setMinimum(-10000000)
            sb.setDecimals(3)

        self.ui.doubleSpinBox_7.setMinimum(0.01)   # Pulse Width minimum for CH1
        self.ui.doubleSpinBox_14.setMinimum(0.01)  # Pulse Width minimum for CH2
        # endregion

        # Existing button logic
        self.ui.pushButton.clicked.connect(self.apply_ch1)
        self.ui.pushButton.clicked.connect(self.apply_ch2)

        # Burst Mode Defaults and Settings

        # region Default burst mode settings
        self.ui.radioButton_4.setChecked(True)
        self.ui.radioButton_2.setChecked(True)
        self.ui.radioButton_6.setChecked(True)
        self.ui.num_stims.setValue(1)
        self.ui.spinBox.setValue(1)
        self.ui.interstim_delay.setValue(1)
        self.ui.widget_25.setEnabled(False)
        self.ui.ch2_delay_widget.setEnabled(False)
        self.ui.jitter_off_3.setChecked(True)
        self.ui.radioButton_6.setChecked(False)
        self.ui.ch1_on_7.setChecked(True)
        self.ui.ch2_on_8.setChecked(True)
        self.ui.waveform_ch1_burst_2.setEnabled(False)
        self.ui.waveform_ch2_burst.setEnabled(False)
        self.ui.doubleSpinBox_38.setValue(5)      # CH1 Vmax default
        self.ui.doubleSpinBox_37.setValue(0)      # CH1 Vmin default
        self.ui.doubleSpinBox_36.setValue(0.001)  # CH1 Iset default for current calc
        self.ui.doubleSpinBox_42.setValue(0.001)  # CH2 Iset default for current calc
        self.ui.doubleSpinBox_44.setValue(5)  # CH2 Vmax default
        self.ui.doubleSpinBox_43.setValue(0)  # CH2 Vmin default
        self.ui.comboBox_19.setCurrentText("Pulse")  # CH1 waveform default
        self.ui.comboBox_22.setCurrentText("Pulse")  # CH2 waveform default
        self.ui.doubleSpinBox_39.setValue(1)  # CH1 Pulse Width default
        self.ui.doubleSpinBox_47.setValue(1)  # CH2 Pulse Width default
        self.ui.ch1_off_11.setChecked(True)         # CH1 Charge Balance default
        self.ui.ch2_chargebalance.setChecked(True)  # CH2 Charge Balance default
        self.ui.radioButton_35.setChecked(True)  # CH1 Polarity Normal default
        self.ui.radioButton_40.setChecked(True)  # CH2 Polarity Normal default
        self.ui.groupBox_26.setEnabled(False)  # CH1 Custom Waveform settings hidden by default
        self.ui.groupBox_28.setEnabled(False)  # CH2 Custom Waveform settings hidden by default
        # endregion

        # region Burst mode dynamic UI logic
        self.ui.radioButton_4.toggled.connect(self._switch_delay_freq_1)
        self.ui.freq_select_stim.toggled.connect(self._switch_delay_freq_1)

        self.ui.radioButton_2.toggled.connect(self._switch_delay_freq_2)
        self.ui.radioButton.toggled.connect(self._switch_delay_freq_2)

        self.ui.jitter_on_3.toggled.connect(self.enable_jitter_1)
        self.ui.jitter_off_3.toggled.connect(self.enable_jitter_1)

        self.ui.radioButton_5.toggled.connect(self.enable_channel_2)
        self.ui.radioButton_6.toggled.connect(self.enable_channel_2)

        self.ui.ch1_on_7.toggled.connect(self.enable_ch1_waveform)
        self.ui.ch1_off_7.toggled.connect(self.enable_ch1_waveform)

        self.ui.ch2_on_8.toggled.connect(self.enable_ch2_waveform)
        self.ui.ch2_off_8.toggled.connect(self.enable_ch2_waveform)

        self.ui.comboBox_19.currentTextChanged.connect(self._update_groupbox_visibility3)
        self.ui.comboBox_22.currentTextChanged.connect(self._update_groupbox_visibility4)

        self.ui.pushButton_4.clicked.connect(self.apply_burst_mode_settings)
        self.ui.stop_button.clicked.connect(self.stop_burst_mode)
        self.ui.stop_button.setEnabled(False)
        # endregion

        # region Enforce Limits
        self.ui.num_stims.setMinimum(1)
        self.ui.interstim_delay.setMinimum(0)
        self.ui.doubleSpinBox_24.setMinimum(0)      # Jitter rate minimum
        self.ui.doubleSpinBox_36.setMinimum(0.001)  # Iset minimum for CH1 current calc
        self.ui.doubleSpinBox_42.setMinimum(0.001)  # Iset minimum for CH2 current calc
        self.ui.spinBox.setMinimum(1)               # Pulses per stim minimum
        self.ui.doubleSpinBox.setMinimum(0)         # Interpulse delay or frequency minimum
        self.ui.doubleSpinBox_3.setMinimum(0)       # CH2 delay minimum
        # endregion


    #region Trial Mode Logic

        # Defaults

        self.ui.radioButton_3.setChecked(True) # Timing option default
        self.manual_v_auto_change() # Disable timing relevant options at start
        self.ui.trial_starting_current.setMinimum(1)
        self.ui.trial_starting_current.setValue(1)

        self.ui.radioButton_8.setChecked(True)

        # Set timer display colour
        self.ui.widget_38.setStyleSheet("color: red; font-weight: bold;")

        self.ui.stackedWidget.setCurrentWidget(self.ui.trial_settings_page)
        page = self.ui.modeSelektor.widget(self.ui.modeSelektor.currentIndex())
        page_name = page.objectName()

        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "Electrode Config",
            "Waveform",
            "Polarity",
            "D188 Channel",
        ])

        if page_name == "TrialMode":
            self.ui.system_status.hide()
        else:
            self.ui.system_status.show()

        self.ui.radioButton_3.toggled.connect(self.manual_v_auto_change)
        self.ui.radioButton_7.toggled.connect(self.manual_v_auto_change)

        self.ui.pushButton_5.clicked.connect(self.browse_load_file)
        self.ui.pushButton_6.clicked.connect(self.browse_save_file)

        self.ui.current_output.textChanged.connect(self.disable_descrease)
        
        options = ["", "DV-I",  "DO-C", "DO-I"]

        for row in range(6):
            combo = QComboBox()
            combo.addItems(options)
            self.ui.tableWidget.setCellWidget(row, 0, combo)

            combo.currentTextChanged.connect(
                lambda text, r=row: self.update_d188_channel_for_row(r)
            )

            # initialize the D188 channel cell
            self.update_d188_channel_for_row(row)

        for row in range(self.ui.tableWidget.rowCount()):
            mode_widget = self.make_active_sham_widget()
            self.ui.tableWidget.setCellWidget(row, 1, mode_widget)   # column 1 example

        for row in range(self.ui.tableWidget.rowCount()):
            pol_widget = self.make_normal_reversed_widget()
            self.ui.tableWidget.setCellWidget(row, 2, pol_widget) 
        # self.ui.tableWidget.setCellWidget(row, col, combo)


        # self.ui.pushButton_7.clicked.connect(
        #     lambda: (
        #         self.ui.stackedWidget.setCurrentWidget(self.ui.trial_running_page),
        #         start_trial(
        #             self,
        #             conditions=self.collect_trial_conditions(),
        #             auto_man=0,
        #         )
        #     )
        # )

        self.ui.pushButton_7.clicked.connect(self.on_start_trial_clicked)

        self.ui.abprt_button.clicked.connect(self.on_abort_trials_clicked)

        self.ui.next_config.clicked.connect(self.on_next_config_clicked)
        self.ui.previous_config.clicked.connect(self.on_previous_config_clicked)

        self.ui.increase_intensity.clicked.connect(
            lambda: (
                increase_intensity(self)
            )
        )

        self.ui.decrease_intensity.clicked.connect(
            lambda: (
                decrease_intensity(self)
            )
        )

        self.ui.log_button.clicked.connect(
            lambda: (
                create_log(self)
            )
        )

        self.ui.radioButton_8.toggled.connect(self.change_state)
        self.ui.radioButton_9.toggled.connect(self.change_state)

    #endregion

    def on_start_trial_clicked(self):
        if self.trial_hw_busy:
            print("Trial hardware busy; cannot start.")
            return

        self.ui.stackedWidget.setCurrentWidget(self.ui.trial_running_page)
        start_trial(
            self,
            conditions=self.collect_trial_conditions(),
            auto_man=0,
        )

    def disable_descrease(self):

        increment_val = float(self.ui.comboBox.currentText())
        if ((self.current_intensity - increment_val)<0):
            self.ui.decrease_intensity.setEnabled(False)
            print('disabled')
        else:
            self.ui.decrease_intensity.setEnabled(True)
            print('enabled')

    # def on_abort_trials_clicked(self):
    #     cancelled = prompt_save_after_trial(self)
    #     if cancelled:
    #         return

    #     self.trial_running = False
    #     self.stop_timers()
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.trial_settings_page)
    #     print_patient_log_counts(self)

    def on_abort_trials_clicked(self):
        if hasattr(self, "experiment_log") and self.experiment_log is not None:
            if self.experiment_log.trial_logs:
                self.experiment_log.trial_logs[-1].total_trial_time_seconds = (
                    self.get_current_trial_elapsed_seconds()
                )

            self.experiment_log.total_experiment_time_seconds = (
                self.get_total_experiment_elapsed_seconds()
            )

        cancelled = prompt_save_after_trial(self)
        if cancelled:
            return

        self.trial_running = False
        self.stop_timers()
        self.ui.stackedWidget.setCurrentWidget(self.ui.trial_settings_page)
        print_patient_log_counts(self)
        self.ui.radioButton_9.setChecked(True)
        self.change_state()
    

    def update_timer_displays(self):
        # Total experiment timer
        if self.experiment_start_monotonic is None:
            self.ui.totaltime_2.setText("00:00")
        else:
            exp_elapsed = int(time.monotonic() - self.experiment_start_monotonic)
            exp_minutes = exp_elapsed // 60
            exp_seconds = exp_elapsed % 60
            self.ui.totaltime_2.setText(f"{exp_minutes:02d}:{exp_seconds:02d}")

        # Per-trial timer
        if self.trial_start_monotonic is None:
            self.ui.trial_timer.setText("00:00")
        else:
            trial_elapsed = int(time.monotonic() - self.trial_start_monotonic)
            trial_minutes = trial_elapsed // 60
            trial_seconds = trial_elapsed % 60
            self.ui.trial_timer.setText(f"{trial_minutes:02d}:{trial_seconds:02d}")

    def start_experiment_timers(self):
        now = time.monotonic()
        self.experiment_start_monotonic = now
        self.trial_start_monotonic = now
        self.update_timer_displays()
        self.display_timer.start()

    def start_new_trial_timer(self):
        self.trial_start_monotonic = time.monotonic()
        self.update_timer_displays()

    def stop_timers(self):
        self.display_timer.stop()

    def reset_timers(self):
        self.display_timer.stop()
        self.experiment_start_monotonic = None
        self.trial_start_monotonic = None
        self.ui.totaltime_2.setText("00:00")
        self.ui.trial_timer.setText("00:00")

    def get_total_experiment_elapsed_seconds(self) -> int:
        if self.experiment_start_monotonic is None:
            return 0
        return int(time.monotonic() - self.experiment_start_monotonic)


    def get_current_trial_elapsed_seconds(self) -> int:
        if self.trial_start_monotonic is None:
            return 0
        return int(time.monotonic() - self.trial_start_monotonic)
        
    # def on_next_config_clicked(self):
    #     self.current_trial_index += 1
    #     load_trial_settings(self)

    def on_next_config_clicked(self):
        if self.trial_hw_busy:
            print("Trial hardware busy; ignoring Next Config.")
            return

        self.current_trial_index += 1
        load_trial_settings(self)

    # def on_previous_config_clicked(self):
    #     self.current_trial_index -= 1
    #     load_trial_settings(self)

    def on_previous_config_clicked(self):
        if self.trial_hw_busy:
            print("Trial hardware busy; ignoring Previous Config.")
            return

        self.current_trial_index -= 1
        load_trial_settings(self)

    def closeEvent(self, event):
        try:
            if hasattr(self, "trial_hw_thread") and self.trial_hw_thread is not None:
                self.trial_hw_thread.quit()
                self.trial_hw_thread.wait(2000)
        finally:
            super().closeEvent(event)


    def collect_trial_conditions(self) -> dict:
        table = self.ui.tableWidget
        conditions = {}

        for row in range(table.rowCount()):
            combo = table.cellWidget(row, 0)
            electrode_config = combo.currentText().strip() if combo else ""

            if not electrode_config:
                continue

            waveform_widget = table.cellWidget(row, 1)
            waveform = (
                "Active" if waveform_widget.active_btn.isChecked()
                else "Sham"
            ) if waveform_widget else ""

            polarity_widget = table.cellWidget(row, 2)
            polarity = (
                "Normal" if polarity_widget.normal_btn.isChecked()
                else "Reversed"
            ) if polarity_widget else ""

            channel_item = table.item(row, 3)
            channel_text = channel_item.text().strip() if channel_item else ""
            channel = int(channel_text) if channel_text.isdigit() else channel_text

            conditions[row] = {
                "electrode_config": electrode_config,
                "waveform": waveform,
                "polarity": polarity,
                "channel": channel,
            }

        return conditions



    def manual_v_auto_change(self):

        if self.ui.radioButton_3.isChecked():
            print("Manual timing selected")
            self.ui.label_19.setEnabled(False)
            self.ui.label_72.setEnabled(False)
            self.ui.label_74.setEnabled(False)
            self.ui.label_20.setEnabled(False)
            self.ui.label_76.setEnabled(False)
            self.ui.label_73.setEnabled(False)
            self.ui.label_75.setEnabled(False)
            self.ui.label_77.setEnabled(False)
            self.ui.label_51.setEnabled(False)
            self.ui.spinBox_2.setEnabled(False)
            self.ui.spinBox_3.setEnabled(False)
            self.ui.spinBox_4.setEnabled(False)
            self.ui.spinBox_5.setEnabled(False)
            self.ui.doubleSpinBox_17.setEnabled(False)

        elif self.ui.radioButton_7.isChecked():
            print("Auto timing selected")

            self.ui.label_19.setEnabled(True)
            self.ui.label_72.setEnabled(True)
            self.ui.label_74.setEnabled(True)
            self.ui.label_20.setEnabled(True)
            self.ui.label_76.setEnabled(True)
            self.ui.label_73.setEnabled(True)
            self.ui.label_75.setEnabled(True)
            self.ui.label_77.setEnabled(True)
            self.ui.label_51.setEnabled(True)
            self.ui.spinBox_2.setEnabled(True)
            self.ui.spinBox_3.setEnabled(True)
            self.ui.spinBox_4.setEnabled(True)
            self.ui.spinBox_5.setEnabled(True)
            self.ui.doubleSpinBox_17.setEnabled(True)


    def update_d188_channel_for_row(self, row: int):
        combo = self.ui.tableWidget.cellWidget(row, 0)

        if combo is None:
            channel_text = ""
        else:
            montage = combo.currentText().strip()

            channel_map = {
                "": "",
                "DV-I": "1",
                "DO-C": "2",
                "DO-I": "3",
            }

            channel_text = channel_map.get(montage, "")

        item = self.ui.tableWidget.item(row, 3)
        if item is None:
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row, 3, item)

        item.setText(channel_text)


    def make_active_sham_widget(self):
        widget = QWidget()

        layout = QHBoxLayout(widget)
        layout.setContentsMargins(4, 2, 4, 2)
        layout.setSpacing(8)

        active_btn = QRadioButton("Active")
        sham_btn = QRadioButton("Sham")

        # Group them so only one can be selected
        button_group = QButtonGroup(widget)
        button_group.addButton(active_btn)
        button_group.addButton(sham_btn)

        # Optional default
        active_btn.setChecked(True)

        # Keep a reference alive on the widget
        widget.button_group = button_group
        widget.active_btn = active_btn
        widget.sham_btn = sham_btn

        layout.addWidget(active_btn)
        layout.addWidget(sham_btn)
        layout.addStretch()

        return widget
    

    def make_normal_reversed_widget(self):
        widget = QWidget()

        layout = QHBoxLayout(widget)
        layout.setContentsMargins(4, 2, 4, 2)
        layout.setSpacing(8)

        normal_btn = QRadioButton("Normal")
        reversed_btn = QRadioButton("Reversed")

        # Group them so only one can be selected
        button_group = QButtonGroup(widget)
        button_group.addButton(normal_btn)
        button_group.addButton(reversed_btn)

        # Optional default
        normal_btn.setChecked(True)

        # Keep a reference alive on the widget
        widget.button_group = button_group
        widget.normal_btn = normal_btn
        widget.reversed_btn = reversed_btn

        layout.addWidget(normal_btn)
        layout.addWidget(reversed_btn)
        layout.addStretch()

        return widget

    from pathlib import Path


    def browse_load_file(self):
        start_dir = Path.cwd() / "Trial_Programs"
        start_dir.mkdir(parents=True, exist_ok=True)

        path, selected_filter = QFileDialog.getOpenFileName(
            self,
            "Load File",
            str(start_dir),
            "CSV Files (*.csv);;All Files (*)"
        )

        if not path:
            return

        path = Path(path)
        self.ui.lineEdit.setText(str(path))
        print(f"Loading file: {path}")

        df = pd.read_csv(path)

        required_cols = {"RowType", "Montage", "Mode", "Polarity", "Setting", "Value"}
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError(f"CSV is missing required columns: {sorted(missing)}")

        table = self.ui.tableWidget

        # ----------------------------
        # Split table rows vs setting rows
        # ----------------------------
        table_df = df[df["RowType"] == "table"].reset_index(drop=True)
        settings_df = df[df["RowType"] == "setting"].reset_index(drop=True)

        # ----------------------------
        # Restore table rows
        # ----------------------------
        while table.rowCount() < len(table_df):
            table.insertRow(table.rowCount())

        for row in range(len(table_df)):
            montage_val = "" if pd.isna(table_df.at[row, "Montage"]) else str(table_df.at[row, "Montage"]).strip()
            mode_val = "" if pd.isna(table_df.at[row, "Mode"]) else str(table_df.at[row, "Mode"]).strip().lower()
            polarity_val = "" if pd.isna(table_df.at[row, "Polarity"]) else str(table_df.at[row, "Polarity"]).strip().lower()

            # Column 0: Montage combo
            combo = table.cellWidget(row, 0)
            if combo is None:
                combo = QComboBox()
                combo.addItems(["", "DV-I", "DO-I", "DO-C"])
                table.setCellWidget(row, 0, combo)

            idx = combo.findText(montage_val)
            if idx >= 0:
                combo.setCurrentIndex(idx)
            else:
                combo.setCurrentIndex(0)

            # Column 1: Active / Sham
            mode_widget = table.cellWidget(row, 1)
            if mode_widget is None:
                mode_widget = self.make_active_sham_widget()
                table.setCellWidget(row, 1, mode_widget)

            if mode_val == "active":
                mode_widget.active_btn.setChecked(True)
            elif mode_val == "sham":
                mode_widget.sham_btn.setChecked(True)

            # Column 2: Normal / Reversed
            pol_widget = table.cellWidget(row, 2)
            if pol_widget is None:
                pol_widget = self.make_normal_reversed_widget()
                table.setCellWidget(row, 2, pol_widget)

            if polarity_val == "normal":
                pol_widget.normal_btn.setChecked(True)
            elif polarity_val == "reversed":
                pol_widget.reversed_btn.setChecked(True)

        # Clear extra table rows beyond CSV length
        for row in range(len(table_df), table.rowCount()):
            combo = table.cellWidget(row, 0)
            if combo is not None:
                combo.setCurrentIndex(0)

            mode_widget = table.cellWidget(row, 1)
            if mode_widget is not None:
                mode_widget.active_btn.setChecked(True)

            pol_widget = table.cellWidget(row, 2)
            if pol_widget is not None:
                pol_widget.normal_btn.setChecked(True)

        # ----------------------------
        # Restore extra settings
        # ----------------------------
        settings_map = {}

        for _, setting_row in settings_df.iterrows():
            key = "" if pd.isna(setting_row["Setting"]) else str(setting_row["Setting"]).strip()
            value = "" if pd.isna(setting_row["Value"]) else setting_row["Value"]
            settings_map[key] = value

        if "Number of Trials" in settings_map:
            self.ui.spinBox_2.setValue(int(float(settings_map["Number of Trials"])))

        if "Timing" in settings_map:
            timing_value = str(settings_map["Timing"]).strip().lower()
            if timing_value == "manual":
                self.ui.radioButton_3.setChecked(True)
            elif timing_value == "auto":
                self.ui.radioButton_7.setChecked(True)

        if "Trial Length" in settings_map:
            self.ui.spinBox_3.setValue(int(float(settings_map["Trial Length"])))

        if "Rest Period" in settings_map:
            self.ui.spinBox_4.setValue(int(float(settings_map["Rest Period"])))

        if "Max Intensity" in settings_map:
            self.ui.doubleSpinBox_17.setValue(float(settings_map["Max Intensity"]))

        if "% of Max" in settings_map:
            self.ui.spinBox_5.setValue(int(float(settings_map["% of Max"])))

        if "Starting Current" in settings_map:
            self.ui.trial_starting_current.setValue(float(settings_map["Starting Current"]))

        if "Current Increment" in settings_map:
            increment_text = str(settings_map["Current Increment"]).strip()
            idx = self.ui.comboBox.findText(increment_text)
            if idx >= 0:
                self.ui.comboBox.setCurrentIndex(idx)

        print(f"Loaded CSV from: {path}")



    def browse_save_file(self):
        start_dir = Path.cwd() / "Trial_Programs"
        start_dir.mkdir(parents=True, exist_ok=True)

        path, selected_filter = QFileDialog.getSaveFileName(
            self,
            "Save File",
            str(start_dir),
            "CSV Files (*.csv);;All Files (*)"
        )

        if not path:
            return

        path = Path(path)

        if path.suffix.lower() != ".csv":
            path = path.with_suffix(".csv")

        self.ui.lineEdit_2.setText(str(path))
        print(f"File saved here: {path}")

        rows = []

        # ----------------------------
        # Table rows
        # ----------------------------
        for row in range(self.ui.tableWidget.rowCount()):
            combo = self.ui.tableWidget.cellWidget(row, 0)
            montage = combo.currentText() if isinstance(combo, QComboBox) else ""

            mode_widget = self.ui.tableWidget.cellWidget(row, 1)
            if mode_widget is not None:
                if mode_widget.active_btn.isChecked():
                    mode = "Active"
                elif mode_widget.sham_btn.isChecked():
                    mode = "Sham"
                else:
                    mode = ""
            else:
                mode = ""

            pol_widget = self.ui.tableWidget.cellWidget(row, 2)
            if pol_widget is not None:
                if pol_widget.normal_btn.isChecked():
                    polarity = "Normal"
                elif pol_widget.reversed_btn.isChecked():
                    polarity = "Reversed"
                else:
                    polarity = ""
            else:
                polarity = ""

            rows.append({
                "RowType": "table",
                "Montage": montage,
                "Mode": mode,
                "Polarity": polarity,
                "Setting": "",
                "Value": "",
            })

        # ----------------------------
        # Extra settings rows
        # ----------------------------
        timing_widget = self.ui.manual_auto
        if self.ui.radioButton_3.isChecked():
            timing_value = "Manual"
        elif self.ui.radioButton_7.isChecked():
            timing_value = "Auto"
        else:
            timing_value = ""

        extra_settings = [
            ("Number of Trials", self.ui.spinBox_2.value()),
            ("Timing", timing_value),
            ("Trial Length", self.ui.spinBox_3.value()),
            ("Rest Period", self.ui.spinBox_4.value()),
            ("Max Intensity", self.ui.doubleSpinBox_17.value()),
            ("% of Max", self.ui.spinBox_5.value()),
            ("Starting Current", self.ui.trial_starting_current.value()),
            ("Current Increment", self.ui.comboBox.currentText()),
        ]

        for setting_name, setting_value in extra_settings:
            rows.append({
                "RowType": "setting",
                "Montage": "",
                "Mode": "",
                "Polarity": "",
                "Setting": setting_name,
                "Value": setting_value,
            })

        df = pd.DataFrame(rows)
        df.to_csv(path, index=False)
        print(f"Saved CSV to: {path}")


    def _set_burst_ui_running(self, running: bool):
        self.ui.pushButton_4.setEnabled(not running)
        self.ui.stop_button.setEnabled(running)

    def _cleanup_burst_thread_refs(self):
        self.burst_thread = None
        self.burst_worker = None

    def _collect_burst_mode_settings(self) -> dict:
        # Collect values from the UI
        num_stims = self.ui.num_stims.value()

        if self.ui.radioButton_4.isChecked():
            print("Period mode enabled for interstim delay")
            stim_period = self.ui.interstim_delay.value()
        else:
            print("Frequency mode enabled for interstim delay")
            stim_frequency = self.ui.interstim_delay.value()
            stim_period = 1 / stim_frequency if stim_frequency != 0 else 0
            print(f"stim_frequency = {stim_frequency} Hz")
            print(f"stim_period = {stim_period} seconds")

        stim_jitter = self.ui.jitter_on_3.isChecked()
        jitter_rate = self.ui.doubleSpinBox_24.value() if stim_jitter else 0

        pulses_per_stim = self.ui.spinBox.value()

        if self.ui.radioButton_2.isChecked():
            interpulse_period = self.ui.doubleSpinBox.value()
            print("Period mode enabled for interpulse delay")
        elif self.ui.radioButton.isChecked():
            print("Frequency mode enabled for interpulse delay")
            pulse_frequency = self.ui.doubleSpinBox.value()
            interpulse_period = 1000 / pulse_frequency if pulse_frequency != 0 else 0
            print(f"interpulse_period = {interpulse_period} ms")
        else:
            interpulse_period = 0

        channel_2_state = self.ui.radioButton_5.isChecked()
        channel_2_delay = self.ui.doubleSpinBox_3.value() if channel_2_state else 0

        ch1_ttl = self.ui.ch1_on_7.isChecked()
        ch2_ttl = self.ui.ch2_on_8.isChecked()

        ds5_control_tab_ch1 = self.ui.current_control_ch1burst.currentWidget().objectName()
        ds5_control_tab_ch2 = self.ui.current_control_ch2burst.currentWidget().objectName()

        if ds5_control_tab_ch1 == "tab_13":
            v_in = self.ui.comboBox_17.currentText()
            i_out = self.ui.comboBox_18.currentText()
            i_set = self.ui.doubleSpinBox_36.value()

            v_in = float(v_in)
            i_out = float(i_out)
            v_max = v_in * (i_set / i_out)
            v_min = 0
            self.ui.OutputMode_display_6.setText(f"{i_set}")
            self.ui.textBrowser_2.setText(f"{v_max}")
            self.ui.textBrowser.setText("0")
        else:
            v_min = self.ui.doubleSpinBox_37.value()
            v_max = self.ui.doubleSpinBox_38.value()

            self.ui.OutputMode_display_6.setText("N/A")
            self.ui.textBrowser_2.setText(f"{v_max}")
            self.ui.textBrowser.setText(f"{v_min}")

        if ds5_control_tab_ch2 == "tab_15":
            v_in = self.ui.comboBox_20.currentText()
            i_out = self.ui.comboBox_21.currentText()
            i_set = self.ui.doubleSpinBox_42.value()

            v_in = float(v_in)
            i_out = float(i_out)
            v_max_ch2 = v_in * (i_set / i_out)
            v_min_ch2 = 0
            self.ui.OutputMode_display_6.setText(f"{i_set}")
            self.ui.textBrowser_2.setText(f"{v_max_ch2}")
            self.ui.textBrowser.setText(f"{v_min_ch2}")
        else:
            v_min_ch2 = self.ui.doubleSpinBox_43.value()
            v_max_ch2 = self.ui.doubleSpinBox_44.value()

            self.ui.OutputMode_display_6.setText("N/A")
            self.ui.textBrowser_2.setText(f"{v_max_ch2}")
            self.ui.textBrowser.setText(f"{v_min_ch2}")

        ch1_waveform = self.ui.comboBox_19.currentText().strip().lower()
        if ch1_waveform == "custom":
            shape_1 = "arb"
        else:
            shape_1 = ch1_waveform

        ch2_waveform = self.ui.comboBox_22.currentText().strip().lower()
        if ch2_waveform == "custom":
            shape_2 = "arb"
        else:
            shape_2 = ch2_waveform

        ch1_pw = self.ui.doubleSpinBox_39.value()
        ch2_pw = self.ui.doubleSpinBox_47.value()

        charge_balance_ch1 = self.ui.ch1_on_11.isChecked()
        charge_balance_ch2 = self.ui.ch1_on_12.isChecked()

        ch1_pp = self.ui.doubleSpinBox_40.value()
        ch2_pp = self.ui.doubleSpinBox_45.value()

        auto_k_ch1 = self.ui.radioButton_34.isChecked()
        auto_k_ch2 = self.ui.radioButton_38.isChecked()

        k_ch1 = self.ui.doubleSpinBox_41.value() if auto_k_ch1 else None
        k_ch2 = self.ui.doubleSpinBox_46.value() if auto_k_ch2 else None

        ch1_reversed = self.ui.radioButton_36.isChecked()
        ch2_reversed = self.ui.radioButton_39.isChecked()

        print(
            f"num_stims={num_stims}, \n"
            f"interstim_delay={stim_period}, \n"
            f"interpulse_delay={interpulse_period}, \n"
            f"jitter={stim_jitter}, \n"
            f"jitter_rate={jitter_rate}, \n"
            f"burst_cycles={pulses_per_stim}, \n"
            f"ch2_state={channel_2_state}, \n"
            f"ch2_delay={channel_2_delay}, \n"
            f"ch1_ttl={ch1_ttl}, \n"
            f"ch2_ttl={ch2_ttl}, \n"
            f"shape_1={shape_1}, \n"
            f"shape_2={shape_2}, \n"
            f"v_min={v_min}, \n"
            f"v_max={v_max}, \n"
            f"v_min_ch2={v_min_ch2}, \n"
            f"v_max_ch2={v_max_ch2}, \n"
            f"pw_ch1={ch1_pw}, \n"
            f"pw_ch2={ch2_pw}, \n"
            f"charge_balance_ch1={charge_balance_ch1}, \n"
            f"charge_balance_ch2={charge_balance_ch2}, \n"
            f"auto_k_ch1={auto_k_ch1}, \n"
            f"auto_k_ch2={auto_k_ch2}, \n"
            f"k_ch1={k_ch1}, \n"
            f"k_ch2={k_ch2}, \n"
            f"ch1_reversed={ch1_reversed}, \n"
            f"ch2_reversed={ch2_reversed}"
        )

        burst_kwargs = dict(
            num_stims=num_stims,
            interstim_delay=stim_period,
            interpulse_delay=interpulse_period,
            jitter=stim_jitter,
            jitter_rate=jitter_rate,
            burst_cycles=pulses_per_stim,
            ch2_state=channel_2_state,
            ch2_delay=channel_2_delay,
            ch1_ttl=ch1_ttl,
            ch2_ttl=ch2_ttl,
            fg_ch1=dict(
                v_min=v_min,
                v_max=v_max,
                shape=shape_1,
                pw=ch1_pw,
                charge_balance=charge_balance_ch1,
                reverse=ch1_reversed,
            ),
            fg_ch2=dict(
                v_min=v_min_ch2,
                v_max=v_max_ch2,
                shape=shape_2,
                pw=ch2_pw,
                charge_balance=charge_balance_ch2,
                reverse=ch2_reversed,
            ),
        )

        return burst_kwargs

    def apply_burst_mode_settings(self):
        if self.burst_thread is not None:
            print("Burst mode is already running.")
            return

        burst_kwargs = self._collect_burst_mode_settings()

        self.burst_thread = QThread(self)
        self.burst_worker = BurstWorker(burst_kwargs)
        self.burst_worker.moveToThread(self.burst_thread)

        self.burst_thread.started.connect(self.burst_worker.run)
        self.burst_worker.finished.connect(self.burst_thread.quit)
        self.burst_worker.finished.connect(self.burst_worker.deleteLater)
        self.burst_thread.finished.connect(self.burst_thread.deleteLater)
        self.burst_thread.finished.connect(self._cleanup_burst_thread_refs)

        self.burst_worker.status.connect(self._on_burst_status)
        self.burst_worker.error.connect(self._on_burst_error)
        self.burst_worker.finished.connect(self._on_burst_finished)

        self._set_burst_ui_running(True)
        self.burst_thread.start()

    def stop_burst_mode(self):
        if self.burst_worker is not None:
            print("Stop requested from UI.")
            self.burst_worker.stop()

    @Slot()
    def _on_burst_finished(self):
        print("Burst worker finished.")
        self._set_burst_ui_running(False)

    @Slot(str)
    def _on_burst_status(self, message: str):
        print(message)

    @Slot(str)
    def _on_burst_error(self, error_text: str):
        print("Burst worker error:")
        print(error_text)

    def _switch_delay_freq_1(self, text: str):
        if self.ui.freq_select_stim.isChecked():
            self.ui.interstim_delay_2.setText("Frequency")
            self.ui.label_92.setText("Hz")
        else:
            self.ui.interstim_delay_2.setText("Interstim Delay")
            self.ui.label_92.setText("Seconds")

    def _switch_delay_freq_2(self, text: str):
        if self.ui.radioButton.isChecked():
            self.ui.label_29.setText("Frequency")
            self.ui.label_90.setText("Hz")
        else:
            self.ui.label_29.setText("Interpulse Delay")
            self.ui.label_90.setText("Milliseconds")

    def enable_jitter_1(self, text: str):
        if self.ui.jitter_on_3.isChecked():
            self.ui.widget_25.setEnabled(True)
        else:
            self.ui.widget_25.setEnabled(False)

    def enable_channel_2(self, text: str):
        if self.ui.radioButton_5.isChecked():
            self.ui.ch2_delay_widget.setEnabled(True)
        else:
            self.ui.ch2_delay_widget.setEnabled(False)

    def enable_ch1_waveform(self, text: str):
        if self.ui.ch1_on_7.isChecked():
            self.ui.waveform_ch1_burst_2.setEnabled(False)
        else:
            self.ui.waveform_ch1_burst_2.setEnabled(True)

    def enable_ch2_waveform(self, text: str):
        if self.ui.ch2_on_8.isChecked():
            self.ui.waveform_ch2_burst.setEnabled(False)
        else:
            self.ui.waveform_ch2_burst.setEnabled(True)

    def _update_groupbox_visibility3(self, text: str):
        self.ui.groupBox_26.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_39.setEnabled(text == "Custom" or text == "Pulse")

    def _update_groupbox_visibility4(self, text: str):
        self.ui.groupBox_28.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_47.setEnabled(text == "Custom" or text == "Pulse")

    def _update_groupbox_visibility(self, text: str):
        self.ui.groupBox_16.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_7.setEnabled(text == "Custom" or text == "Pulse")

    def _update_groupbox_visibility2(self, text: str):
        self.ui.groupBox_23.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_14.setEnabled(text == "Custom" or text == "Pulse")

    def on_radioButton_13_toggled(self, checked: bool):
        self.ui.doubleSpinBox_8.setEnabled(checked)

    def on_radioButton_17_toggled(self, checked: bool):
        self.ui.doubleSpinBox_4.setEnabled(checked)

    def on_pushButton_clicked(self):
        pass

    def on_tab_changed_ch1(self, index: int):
        page = self.ui.tabWidget.widget(index)
        page_name = page.objectName()

        if page_name == "tab":
            return 1
        else:
            return 0

    def on_tab_changed_ch2(self, index: int):
        page = self.ui.tabWidget_2.widget(index)
        page_name = page.objectName()

        if page_name == "tab_3":
            return 1
        else:
            return 0
        
    def tab_mode_change(self, index: int):
        page = self.ui.modeSelektor.widget(index)
        page_name = page.objectName()

        if page_name == "TrialMode":
            self.ui.system_status.hide()
        else:
            self.ui.system_status.show()




    def apply_ch1(self):
        freq_hz = self.ui.doubleSpinBox_2.value()
        d188_channel = self.ui.spinBox_7.value()

        print(d188_channel)

        self.ui.textBrowser_10.setText(f"{d188_channel}")

        ch_balance = True if self.ui.ch1_on_2.isChecked() else False

        page_name = self.ui.tabWidget.currentWidget().objectName()

        if page_name == "tab":
            v_in = self.ui.comboBox_3.currentText()
            i_out = self.ui.comboBox_4.currentText()
            i_set = self.ui.doubleSpinBox_5.value()

            v_in = float(v_in)
            i_out = float(i_out)
            v_out = v_in * (i_set / i_out)

            self.ui.OutputMode_display_6.setText(f"{i_set}")
            self.ui.textBrowser_2.setText(f"{v_out}")
            self.ui.textBrowser.setText("0")
        else:
            v_min = self.ui.doubleSpinBox_9.value()
            v_max = self.ui.doubleSpinBox_10.value()

            self.ui.OutputMode_display_6.setText("N/A")
            self.ui.textBrowser_2.setText(f"{v_max}")
            self.ui.textBrowser.setText(f"{v_min}")

        if self.ui.doubleSpinBox_7.isEnabled():
            pw = self.ui.doubleSpinBox_7.value()
            self.ui.textBrowser_5.setText(f"{pw}")
        else:
            self.ui.textBrowser_5.setText("N/A")

        wf_text = self.ui.comboBox_2.currentText().strip().lower()

        if wf_text == "custom":
            shape = "arb"
            custom = "yes"
        else:
            shape = wf_text
            custom = "no"

        state = 1 if self.ui.ch1_on.isChecked() else 0
        reverse = 1 if self.ui.radioButton_16.isChecked() else 0
        auto_k = 0 if self.ui.radioButton_13.isChecked() else 1

        kwargs = dict(
            shape=shape,
            custom=custom,
            channel=1,
            state=state,
            d188=True,
            d188_channel=d188_channel,
            charge_balance=ch_balance,
            reverse=reverse,
        )

        if freq_hz != 0:
            kwargs["freq"] = freq_hz
        try:
            kwargs["pw"] = pw
        except Exception:
            pass

        if page_name == "tab":
            kwargs["v_min"] = 0
            kwargs["v_max"] = v_out
        else:
            kwargs["v_min"] = v_min
            kwargs["v_max"] = v_max

        func_gen_control_stateful(**kwargs)

        self.ui.frequency_display_3.setText(f"{freq_hz}")

        if state == 1:
            self.ui.OutputMode_display_3.setText("On")
        else:
            self.ui.OutputMode_display_3.setText("Off")

    def apply_ch2(self):
        freq_hz = self.ui.doubleSpinBox_4.value()
        ch_balance2 = True if self.ui.ch1_on_4.isChecked() else False

        page_name = self.ui.tabWidget_2.currentWidget().objectName()

        if page_name == "tab_3":
            v_in = self.ui.comboBox_5.currentText()
            i_out = self.ui.comboBox_6.currentText()
            i_set = self.ui.doubleSpinBox_11.value()

            v_in = float(v_in)
            i_out = float(i_out)
            v_out = v_in * (i_set / i_out)
            self.ui.OutputMode_display_8.setText(f"{i_set}")
            self.ui.textBrowser_9.setText(f"{v_out}")
            self.ui.textBrowser_7.setText("0")
        else:
            v_min = self.ui.doubleSpinBox_12.value()
            v_max = self.ui.doubleSpinBox_13.value()

            self.ui.OutputMode_display_8.setText("N/A")
            self.ui.textBrowser_9.setText(f"{v_max}")
            self.ui.textBrowser_7.setText(f"{v_min}")

        if self.ui.doubleSpinBox_14.isEnabled():
            pw2 = self.ui.doubleSpinBox_14.value()
            self.ui.textBrowser_8.setText(f"{pw2}")
        else:
            self.ui.textBrowser_8.setText("N/A")

        wf_text = self.ui.comboBox_7.currentText().strip().lower()

        if wf_text == "custom":
            shape = "arb"
            custom = "yes"
        else:
            shape = wf_text
            custom = "no"

        state = 1 if self.ui.ch1_on_3.isChecked() else 0
        reverse = 1 if self.ui.radioButton_20.isChecked() else 0
        auto_k = 0 if self.ui.radioButton_17.isChecked() else 1

        kwargs = dict(
            shape=shape,
            custom=custom,
            channel=2,
            state=state,
            charge_balance=ch_balance2,
            reverse=reverse,
        )

        if freq_hz != 0:
            kwargs["freq"] = freq_hz
        try:
            kwargs["pw"] = pw2
        except Exception:
            pass

        if page_name == "tab_3":
            kwargs["v_min"] = 0
            kwargs["v_max"] = v_out
        else:
            kwargs["v_min"] = v_min
            kwargs["v_max"] = v_max

        try:
            func_gen_control_stateful(**kwargs)
        except Exception:
            pass

        self.ui.frequency_display_5.setText(f"{freq_hz}")

        if state == 1:
            self.ui.OutputMode_display_5.setText("On")
        else:
            self.ui.OutputMode_display_5.setText("Off")

    # def change_state(self):
    #     if self.ui.radioButton_8.isChecked():
    #         state = 1
    #     elif self.ui.radioButton_9.isChecked():
    #         state = 0 
        
    #     func_gen_control_stateful(state=state, channel=1)


    def change_state(self, checked=None):
        # Ignore the signal if we are not currently in a running trial
        if not getattr(self, "trial_running", False):
            return

        # Ignore the "False" half of the toggled signal to avoid double-triggering
        if checked is False:
            return

        # Do not allow overlapping hardware applies
        if getattr(self, "trial_hw_busy", False):
            print("Trial hardware busy; ignoring state change.")
            return

        # Need current trial settings available
        if not hasattr(self, "current_trial_settings") or not self.current_trial_settings:
            print("No current trial settings available; ignoring state change.")
            return

        print("Applying state change...")

        try:
            kwargs = build_trial_stateful_kwargs(self)
        except Exception as e:
            print(f"Failed to build trial hardware kwargs during state change: {e}")
            return

        self.request_trial_apply(kwargs)

    
    def set_trial_controls_enabled(self, enabled: bool):
        self.ui.next_config.setEnabled(enabled)
        self.ui.previous_config.setEnabled(enabled)
        self.ui.increase_intensity.setEnabled(enabled)
        self.ui.decrease_intensity.setEnabled(enabled)
        self.ui.log_button.setEnabled(enabled)
        self.ui.abprt_button.setEnabled(enabled)
        self.ui.radioButton_8.setEnabled(enabled)
        self.ui.radioButton_9.setEnabled(enabled)


    def request_trial_apply(self, kwargs: dict):
        if self.trial_hw_busy:
            print("Trial hardware apply already in progress.")
            return False

        self.trial_hw_busy = True
        self.set_trial_controls_enabled(False)
        self.request_trial_hardware_apply.emit(kwargs)
        return True


    def on_trial_hardware_status(self, message: str):
        print(message)


    def on_trial_hardware_finished(self):
        self.trial_hw_busy = False
        self.set_trial_controls_enabled(True)
        self.disable_descrease()


    def on_trial_hardware_error(self, err: str):
        print("Trial hardware error:")
        print(err)
        self.trial_hw_busy = False
        self.set_trial_controls_enabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ControllerMain()
    w.show()
    sys.exit(app.exec())