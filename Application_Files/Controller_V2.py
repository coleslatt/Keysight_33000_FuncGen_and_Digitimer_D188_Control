# Custom controller main window

import sys
from PySide6.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QDialog
from FuncGen_Selector_Function_2 import func_gen_control, func_gen_control_stateful
from burst_mode_function import burst_mode

from stim_system_gui_v2 import Ui_Controller_Main

from PySide6.QtCore import QObject, QEvent
from PySide6 import QtCore, QtWidgets

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

class ControllerMain(QDialog):
    def __init__(self):

        super().__init__()
        self.ui = Ui_Controller_Main()
        self.ui.setupUi(self)

        self.no_wheel_filter = NoWheelFilter()

        for w in self.findChildren(QSpinBox):
            w.installEventFilter(self.no_wheel_filter)

        for w in self.findChildren(QDoubleSpinBox):
            w.installEventFilter(self.no_wheel_filter)

        enable_name_tooltips(self)

    # Burst Mode Defaults and Settings
        
        #region Continuous mode default settings
        self.ui.groupBox_16.setEnabled(False)
        self.ui.groupBox_23.setEnabled(False)
        self.ui.doubleSpinBox_8.setEnabled(False)
        self.ui.doubleSpinBox_16.setEnabled(False)
        self.ui.doubleSpinBox_7.setEnabled(False)
        self.ui.doubleSpinBox_14.setEnabled(False)
        self.ui.ch1_off.setChecked(True)
        self.ui.ch1_off_3.setChecked(True)
        
        self.ui.doubleSpinBox_7.setMinimum(0.001) # Pulse Width Ch1 minimum
        self.ui.doubleSpinBox_14.setMinimum(0.001) # Pulse Width Ch2 minimum

        self.ui.doubleSpinBox_5.setValue(1.0) # Set default current to 1 mA for CH1
        self.ui.doubleSpinBox_11.setValue(1.0) # Set default current to 1 mA for CH2
        self.ui.doubleSpinBox_2.setValue(60) # Set default frequency to 60 Hz for CH1
        self.ui.doubleSpinBox_4.setValue(60) # Set default frequency to 60 Hz for CH2

        #endregion

        #region Continuous mode dynamic UI logic
        # 2) React to combo box changes (CH1)
        self.ui.comboBox_2.currentTextChanged.connect(
            self._update_groupbox_visibility
        )

        # 2) React to combo box changes (CH2)
        self.ui.comboBox_7.currentTextChanged.connect(
            self._update_groupbox_visibility2
        )

        self.ui.tabWidget.currentChanged.connect(self.on_tab_changed_ch1)
        self.ui.tabWidget_2.currentChanged.connect(self.on_tab_changed_ch2)
        self.ui.radioButton_13.toggled.connect(self.on_radioButton_13_toggled)
        self.ui.radioButton_17.toggled.connect(self.on_radioButton_17_toggled)

        #endregion

        #region Limits for Continuous Mode
        # Set limits for spin boxes
        for sb in self.findChildren(QSpinBox):
            sb.setMaximum(10000000)
            sb.setMinimum(-10000000)
    
        # Set limits for double spin boxes
        for sb in self.findChildren(QDoubleSpinBox):
            sb.setMaximum(10000000)
            sb.setMinimum(-10000000)
            sb.setDecimals(3)

        self.ui.doubleSpinBox_7.setMinimum(0.01) # Pulse Width minimum for CH1
        self.ui.doubleSpinBox_14.setMinimum(0.01) # Pulse Width minimum for CH2

        #endregion

        # Existing button logic
        self.ui.pushButton.clicked.connect(self.apply_ch1) 
        self.ui.pushButton.clicked.connect(self.apply_ch2)

        

        

    # Burst Mode Defaults and Settings

        #region Default burst mode settings

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

        self.ui.doubleSpinBox_38.setValue(5) # CH1 Vmax default
        self.ui.doubleSpinBox_37.setValue(0) # CH1 Vmin default
        self.ui.doubleSpinBox_36.setValue(0.001) # CH1 Iset default for current calc
        self.ui.doubleSpinBox_42.setValue(0.001) # CH2 Iset default for current calc

        self.ui.doubleSpinBox_44.setValue(5) # CH2 Vmax default
        self.ui.doubleSpinBox_43.setValue(0) # CH2 Vmin default

        self.ui.comboBox_19.setCurrentText("Pulse") # CH1 waveform default
        self.ui.comboBox_22.setCurrentText("Pulse") # CH2 waveform default

        self.ui.doubleSpinBox_39.setValue(1) # CH1 Pulse Width default
        self.ui.doubleSpinBox_47.setValue(1) # CH2 Pulse Width default

        self.ui.ch1_off_11.setChecked(True) # CH1 Charge Balance default
        self.ui.ch2_chargebalance.setChecked(True) # CH2 Charge Balance default

        self.ui.radioButton_35.setChecked(True) # CH1 Polarity Normal default
        self.ui.radioButton_40.setChecked(True) # CH2 Polarity Normal default

        self.ui.groupBox_26.setEnabled(False) # CH1 Custom Waveform settings hidden by default
        self.ui.groupBox_28.setEnabled(False) # CH2 Custom Waveform settings hidden by default

        #endregion

        #region Burst mode dynamic UI logic
        
        self.ui.radioButton_4.toggled.connect(self._switch_delay_freq_1)
        self.ui.freq_select_stim.toggled.connect(self._switch_delay_freq_1)

        self.ui.radioButton_2.toggled.connect(self._switch_delay_freq_2)
        self.ui.radioButton.toggled.connect(self._switch_delay_freq_2)

        self.ui.jitter_on_3.toggled.connect(self.enable_jitter_1)
        self.ui.jitter_off_3.toggled.connect(self.enable_jitter_1)

        # self.ui.jitter_on_2.toggled.connect(self.enable_jitter_2)
        # self.ui.jitter_off_2.toggled.connect(self.enable_jitter_2)

        self.ui.radioButton_5.toggled.connect(self.enable_channel_2)
        self.ui.radioButton_6.toggled.connect(self.enable_channel_2)

        self.ui.ch1_on_7.toggled.connect(self.enable_ch1_waveform)
        self.ui.ch1_off_7.toggled.connect(self.enable_ch1_waveform)

        self.ui.ch2_on_8.toggled.connect(self.enable_ch2_waveform)
        self.ui.ch2_off_8.toggled.connect(self.enable_ch2_waveform)

        # 1) React to shape value changes (CH1)
        self.ui.comboBox_19.currentTextChanged.connect(
            self._update_groupbox_visibility3
        )

        # 2) React to shape value changes (CH2)
        self.ui.comboBox_22.currentTextChanged.connect(
            self._update_groupbox_visibility4
        )

        # Burst mode apply settings button
        self.ui.pushButton_4.clicked.connect(self.apply_burst_mode_settings)

        #endregion

        #region Enforce Limits

        self.ui.num_stims.setMinimum(1)
        self.ui.interstim_delay.setMinimum(0)
        self.ui.doubleSpinBox_24.setMinimum(0) # Jitter rate minimum
        self.ui.doubleSpinBox_36.setMinimum(0.001) # Iset minimum for CH1 current calc
        self.ui.doubleSpinBox_42.setMinimum(0.001) # Iset minimum for CH2 current calc
        self.ui.spinBox.setMinimum(1) # Pulses per stim minimum
        self.ui.doubleSpinBox.setMinimum(0) # Interpulse delay or frequency minimum depending on mode
        self.ui.doubleSpinBox_3.setMinimum(0) # CH2 delay minimum
        # self.ui.doubleSpinBox.setRange(0.0, 5.0)


        #endregion
    def apply_burst_mode_settings(self):
        # This function will read all the burst mode settings from the UI and apply them to the hardware
        
        # Collect values from the UI
        num_stims = self.ui.num_stims.value() # Number of stimuli in the burst

        if self.ui.radioButton_4.isChecked(): # Period or Frequency
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

        if self.ui.radioButton_2.isChecked(): # Period or Frequency
            interpulse_period = self.ui.doubleSpinBox.value()
            print("Period mode enabled for interpulse delay")

        elif self.ui.radioButton.isChecked():

            print("Frequency mode enabled for interpulse delay")
            pulse_frequency = self.ui.doubleSpinBox.value()
            interpulse_period = 1000 / (pulse_frequency ) if pulse_frequency != 0 else 0

            print(f"interpulse_period = {interpulse_period} seconds")

        
        channel_2_state = self.ui.radioButton_5.isChecked()
        channel_2_delay = self.ui.doubleSpinBox_3.value() if channel_2_state else 0

        # Channel waveform settings
        ch1_ttl = self.ui.ch1_on_7.isChecked()
        ch2_ttl = self.ui.ch2_on_8.isChecked()

        ds5_control_tab_ch1 = self.ui.current_control_ch1burst.currentWidget().objectName()
        ds5_control_tab_ch2 = self.ui.current_control_ch2burst.currentWidget().objectName()

        if ds5_control_tab_ch1 == "tab_13":
            
            # print("page_name = tab")
            v_in  = self.ui.comboBox_17.currentText()
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

            self.ui.OutputMode_display_6.setText(f"N/A")
            self.ui.textBrowser_2.setText(f"{v_max}")
            self.ui.textBrowser.setText(f"{v_min}") 


        if ds5_control_tab_ch2 == "tab_15":

            v_in  = self.ui.comboBox_20.currentText()
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

            self.ui.OutputMode_display_6.setText(f"N/A")
            self.ui.textBrowser_2.setText(f"{v_max_ch2}")
            self.ui.textBrowser.setText(f"{v_min_ch2}") 

        ch1_waveform = self.ui.comboBox_19.currentText().strip().lower()
        if ch1_waveform == "custom":
            shape_1 = "arb"       # func_gen_control expects 'arb' or 'arbitrary' for arbitrary mode
            custom_1 = "yes"      # your function uses 'yes'/'no' strings :contentReference[oaicite:4]{index=4}
        else:
            shape_1 = ch1_waveform     # "sine", "square", "pulse"
            custom_1 = "no"
        # 

        ch2_waveform = self.ui.comboBox_22.currentText().strip().lower()
        if ch2_waveform == "custom":
            shape_2 = "arb"       # func_gen_control expects 'arb' or 'arbitrary' for arbitrary mode
            custom_2 = "yes"      # your function uses 'yes'/'no' strings :contentReference[oaicite:4]{index=4}
        else:
            shape_2 = ch2_waveform     # "sine", "square", "pulse"
            custom_2 = "no"

        ch1_pw = self.ui.doubleSpinBox_39.value()
        ch2_pw = self.ui.doubleSpinBox_47.value()

        charge_balance_ch1 = self.ui.ch1_on_11.isChecked()
        charge_balance_ch2 = self.ui.ch1_on_12.isChecked()

        ch1_pp = self.ui.doubleSpinBox_40.value()
        ch2_pp = self.ui.doubleSpinBox_45.value()

        auto_k_ch1 = self.ui.radioButton_34.isChecked()
        auto_k_ch2 = self.ui.radioButton_38.isChecked()

        k_ch1 = self.ui.doubleSpinBox_41.value() if auto_k_ch1 else None
        k_ch2 = self.ui.doubleSpinBox_46.value() if auto_k_ch1 else None

        ch1_reversed = True if self.ui.radioButton_36.isChecked() else False
        ch2_reversed = True if self.ui.radioButton_39.isChecked() else False


        print(f"num_stims={num_stims}, \ninterstim_delay={stim_period}, \ninterpulse_delay={interpulse_period}, \njitter={stim_jitter}, \njitter_rate={jitter_rate}, \nburst_cycles={pulses_per_stim}, \nch2_state={channel_2_state}, \nch2_delay={channel_2_delay}, \nch1_ttl={ch1_ttl}, \nch2_ttl={ch2_ttl}, \nshape_1={shape_1}, \nshape_2={shape_2}, \nv_min={v_min}, \nv_max={v_max}, \nv_min_ch2={v_min_ch2}, \nv_max_ch2={v_max_ch2}, \npw_ch1={ch1_pw}, \npw_ch2={ch2_pw}, \ncharge_balance_ch1={charge_balance_ch1}, \ncharge_balance_ch2={charge_balance_ch2}, \nauto_k_ch1={auto_k_ch1}, \nauto_k_ch2={auto_k_ch2}, \nk_ch1={k_ch1}, \nk_ch2={k_ch2}, \nch1_reversed={ch1_reversed}, \nch2_reversed={ch2_reversed}")

        func_gen_control_stateful(reset= True)

        burst_mode(
            num_stims=num_stims, # Number of stims
            interstim_delay = stim_period, # Delay in between stims in seconds!
            interpulse_delay = interpulse_period,   # CH2 10 ms after CH1, or delay in between pulses in ms
            jitter=stim_jitter, # 1=ON, 0=0FF
            jitter_rate=jitter_rate, # +/- Jitter of interstim delay
            burst_cycles = pulses_per_stim, # Number of pulses per stim
            ch2_state = channel_2_state,
            ch2_delay = channel_2_delay,
            ch1_ttl=ch1_ttl, 
            ch2_ttl=ch2_ttl,
            fg_ch1=dict(
                v_min=v_min,
                v_max=v_max,
                shape=shape_1,
                pw=ch1_pw,               # ms (per your func_gen_control convention)
                charge_balance=charge_balance_ch1,
                reverse=ch1_reversed,
            ),

            fg_ch2=dict(
                v_min=v_min_ch2,
                v_max=v_max_ch2,
                shape=shape_2,
                pw=ch2_pw,               # ms (per your func_gen_control convention)
                charge_balance=charge_balance_ch2,
                reverse=ch2_reversed,
            ),
        )

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

    # def enable_jitter_2(self, text: str):
    #     if self.ui.jitter_on_2.isChecked():
    #         self.ui.widget_12.setEnabled(True)
    #     else:
    #         self.ui.widget_12.setEnabled(False)
    
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
        
    
    # 3) Custom Waveform Visibility logic (CH1)
    def _update_groupbox_visibility3(self, text: str):
        self.ui.groupBox_26.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_39.setEnabled(text == "Custom" or text == "Pulse")

        # 3) Custom Waveform Visibility logic (CH1)
    def _update_groupbox_visibility4(self, text: str):
        self.ui.groupBox_28.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_47.setEnabled(text == "Custom" or text == "Pulse")
        

    # 3) Custom Waveform Visibility logic (CH1)
    def _update_groupbox_visibility(self, text: str):
        self.ui.groupBox_16.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_7.setEnabled(text == "Custom" or text == "Pulse")

    # 3) Custom Waveform Visibility logic (CH2)
    def _update_groupbox_visibility2(self, text: str):
        self.ui.groupBox_23.setEnabled(text == "Custom")
        self.ui.doubleSpinBox_14.setEnabled(text == "Custom" or text == "Pulse")

    # Auto K enable spinboxes (CH1)
    def on_radioButton_13_toggled(self, checked: bool):
        self.ui.doubleSpinBox_8.setEnabled(checked)

    # Auto K enable spinboxes (CH2)
    def on_radioButton_17_toggled(self, checked: bool):
        self.ui.doubleSpinBox_4.setEnabled(checked)

    def on_pushButton_clicked(self):
        pass  # your existing logic

    def on_tab_changed_ch1(self, index: int):

        page = self.ui.tabWidget.widget(index)
        page_name = page.objectName()
        # print(page_name)

        if page_name == "tab":
            return 1
        else:
            return 0
        
    def on_tab_changed_ch2(self, index: int):

        page = self.ui.tabWidget_2.widget(index)
        page_name = page.objectName()
        # print(page_name)

        if page_name == "tab_3":
            return 1
        else:
            return 0
        
    def apply_ch1(self):
        
        #region Read UI and Call func_gen_control for CH1
        # 1) Read values from UI
        freq_hz = self.ui.doubleSpinBox_2.value()  # Frequency (Hz)
        # current = self.ui.doubleSpinBox_5.value()  # Current (mA)
        d188_channel = self.ui.spinBox_7.value()  # D188 Channel Number

        print(d188_channel)

        self.ui.textBrowser_10.setText(f"{d188_channel}")

        ch_balance = True if self.ui.ch1_on_2.isChecked() else False  #  Charge Balance

        # Current Calc/Processing

        page_name = self.ui.tabWidget.currentWidget().objectName()

        if page_name == "tab":

            # print("page_name = tab")

            v_in  = self.ui.comboBox_3.currentText()
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

            self.ui.OutputMode_display_6.setText(f"N/A")
            self.ui.textBrowser_2.setText(f"{v_max}")
            self.ui.textBrowser.setText(f"{v_min}") 

        if self.ui.doubleSpinBox_7.isEnabled():
            pw = self.ui.doubleSpinBox_7.value()
            self.ui.textBrowser_5.setText(f"{pw}")
        else:
            self.ui.textBrowser_5.setText("N/A")

        
        #endregion
        
        # 2) Map waveform dropdown text -> func_gen_control "shape"/"custom"
        wf_text = self.ui.comboBox_2.currentText().strip().lower()  # Sine/Square/Pulse/Custom :contentReference[oaicite:2]{index=2}

        if wf_text == "custom":
            shape = "arb"       # func_gen_control expects 'arb' or 'arbitrary' for arbitrary mode
            custom = "yes"      # your function uses 'yes'/'no' strings :contentReference[oaicite:4]{index=4}
        else:
            shape = wf_text     # "sine", "square", "pulse"
            custom = "no"

        # On/Off (Channel 1)
        state = 1 if self.ui.ch1_on.isChecked() else 0  # "On" vs "Off" 

        print(state)

        # Reverse (Channel 1)
        reverse = 1 if self.ui.radioButton_16.isChecked() else 0  # "On" vs "Off" 

        print(f' reverse = {reverse}')
    
        # Auto K (Channel 1)
        auto_k = 0 if self.ui.radioButton_13.isChecked() else 1  # "On" vs "Off" 

        kwargs = dict(
            shape=shape,
            custom=custom,
            channel=1,
            state=state,
            d188 = True,
            d188_channel=d188_channel,
            charge_balance=ch_balance,
            reverse = reverse,
            # auto_k = auto_k
        )

        if freq_hz != 0:
            kwargs["freq"] = freq_hz
        try:
            kwargs["pw"] = pw
        except:
            pass
        
        if page_name == "tab":
            kwargs["v_min"] = 0
            kwargs["v_max"] = v_out
        else:
            kwargs["v_min"] = v_min
            kwargs["v_max"] = v_max

        func_gen_control_stateful(**kwargs)


        # # 4) Call your existing hardware function
        # try:
        #     func_gen_control_stateful(**kwargs)
        # except:
        #     print("Error: Function Generator not connected")

        # Assigning System Status Display
        self.ui.frequency_display_3.setText(f"{freq_hz}")
        # self.ui.OutputMode_display_6.setText(f"{current}")

        if state==1:
            self.ui.OutputMode_display_3.setText("On")
        else:
            self.ui.OutputMode_display_3.setText("Off") 

    def apply_ch2(self):
        
        # 1) Read values from UI
        freq_hz = self.ui.doubleSpinBox_4.value()  # Frequency (Hz)
        # current = self.ui.doubleSpinBox.value()  # Current (mA)
        ch_balance2 = True if self.ui.ch1_on_4.isChecked() else False  #  Charge Balance

                # Current Calc/Processing

        page_name = self.ui.tabWidget_2.currentWidget().objectName()

        if page_name == "tab_3":

            v_in  = self.ui.comboBox_5.currentText()
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

            self.ui.OutputMode_display_8.setText(f"N/A")
            self.ui.textBrowser_9.setText(f"{v_max}")
            self.ui.textBrowser_7.setText(f"{v_min}") 

        if self.ui.doubleSpinBox_14.isEnabled():
            pw2 = self.ui.doubleSpinBox_14.value()
            self.ui.textBrowser_8.setText(f"{pw2}")
        else:
            self.ui.textBrowser_8.setText("N/A")


        # 2) Map waveform dropdown text -> func_gen_control "shape"/"custom"
        wf_text = self.ui.comboBox_7.currentText().strip().lower()  # Sine/Square/Pulse/Custom :contentReference[oaicite:2]{index=2}

        if wf_text == "custom":
            shape = "arb"       # func_gen_control expects 'arb' or 'arbitrary' for arbitrary mode :contentReference[oaicite:3]{index=3}
            custom = "yes"      # your function uses 'yes'/'no' strings :contentReference[oaicite:4]{index=4}
        else:
            shape = wf_text     # "sine", "square", "pulse"
            custom = "no"

        # print(f"Waveform Shape CH2: {shape}")

        # 3) On/Off (Channel 2)
        state = 1 if self.ui.ch1_on_3.isChecked() else 0  # "On" vs "Off" :contentReference[oaicite:5]{index=5}

        # Reverse (Channel 1)
        reverse = 1 if self.ui.radioButton_20.isChecked() else 0  # "On" vs "Off" 

        # Auto K (Channel 2)
        auto_k = 0 if self.ui.radioButton_17.isChecked() else 1  # "On" vs "Off" 

        kwargs = dict(
            shape=shape,
            custom=custom,
            channel=2,
            state=state,
            charge_balance=ch_balance2,
            reverse = reverse,
            # auto_k = auto_k
        )

        if freq_hz != 0:
            kwargs["freq"] = freq_hz
        try:
            kwargs["pw"] = pw2
        except:
            pass

        if page_name == "tab_3":
            kwargs["v_min"] = 0
            kwargs["v_max"] = v_out
        else:
            kwargs["v_min"] = v_min
            kwargs["v_max"] = v_max

        # 4) Call your existing hardware function
        try:
            func_gen_control_stateful(**kwargs)
        except:
            # print("Error: Function Generator not connected")
            pass

        self.ui.frequency_display_5.setText(f"{freq_hz}")

        if state==1:
            self.ui.OutputMode_display_5.setText("On")
        else:
            self.ui.OutputMode_display_5.setText("Off")

# Burst Mode Functions and Defaults



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ControllerMain()
    w.show()
    sys.exit(app.exec())
