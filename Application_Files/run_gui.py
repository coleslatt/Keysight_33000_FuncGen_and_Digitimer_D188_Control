# Demo for running the generated GUI

import sys
from PySide6.QtWidgets import QApplication, QWidget  # you can swap QWidget -> QDialog if desired

from stim_system_gui import Ui_Controller_Main

class ControllerMain(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Controller_Main()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ControllerMain()
    w.show()
    sys.exit(app.exec())
