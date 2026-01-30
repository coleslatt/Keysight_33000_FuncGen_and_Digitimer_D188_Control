# Custom controller main window

import sys
from PySide6.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QDialog
from FuncGen_Selector_Function import func_gen_control, func_gen_control_stateful

from stim_system_gui2 import Ui_Controller_Main

class ControllerMain(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Controller_Main()
        self.ui.setupUi(self)

        # Logic for custom waveform option visibility
        # 1) Start hidden
        self.ui.groupBox_16.setEnabled(False)
        self.ui.groupBox_23.setEnabled(False)
        self.ui.doubleSpinBox_8.setEnabled(False)
        self.ui.doubleSpinBox_16.setEnabled(False)
        self.ui.doubleSpinBox_7.setEnabled(False)
        self.ui.doubleSpinBox_14.setEnabled(False)


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

        # Set limits for spin boxes
        for sb in self.findChildren(QSpinBox):
            sb.setMaximum(10000000)
            sb.setMinimum(-10000000)
    
        # Set limits for double spin boxes
        for sb in self.findChildren(QDoubleSpinBox):
            sb.setMaximum(10000000)
            sb.setMinimum(-10000000)
            sb.setDecimals(3)

        # Existing button logic
        self.ui.pushButton.clicked.connect(self.apply_ch1)
        self.ui.pushButton.clicked.connect(self.apply_ch2)

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
        
        # 1) Read values from UI
        freq_hz = self.ui.spinBox_6.value()  # Frequency (Hz)
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
        freq_hz = self.ui.spinBox_8.value()  # Frequency (Hz)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ControllerMain()
    w.show()
    sys.exit(app.exec())
