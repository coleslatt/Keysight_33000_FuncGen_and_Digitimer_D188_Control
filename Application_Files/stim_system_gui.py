# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stim_system_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTextBrowser, QWidget)

import icons

class Ui_Controller_Main(object):
    def setupUi(self, Controller_Main):
        if not Controller_Main.objectName():
            Controller_Main.setObjectName(u"Controller_Main")
        Controller_Main.resize(897, 856)
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        Controller_Main.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/electrode_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Controller_Main.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Controller_Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Controller_Main)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_11 = QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_14 = QGroupBox(self.groupBox_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_8 = QGridLayout(self.groupBox_14)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.radioButton_9 = QRadioButton(self.groupBox_14)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_8.addWidget(self.radioButton_9, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_14)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_8.addWidget(self.comboBox_2, 5, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_14)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_8.addWidget(self.label_30, 1, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.groupBox_14)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_9 = QGridLayout(self.groupBox_15)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_31 = QLabel(self.groupBox_15)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_9.addWidget(self.label_31, 2, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_15)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_9.addWidget(self.spinBox_4, 0, 1, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_15)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.gridLayout_9.addWidget(self.doubleSpinBox_5, 3, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_15)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_9.addWidget(self.label_32, 0, 0, 1, 1)

        self.label_33 = QLabel(self.groupBox_15)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_9.addWidget(self.label_33, 3, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox_15)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout_9.addWidget(self.spinBox_5, 2, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_15)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_9.addWidget(self.label_34, 0, 2, 1, 1)

        self.label_35 = QLabel(self.groupBox_15)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_9.addWidget(self.label_35, 2, 2, 1, 1)

        self.label_36 = QLabel(self.groupBox_15)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_9.addWidget(self.label_36, 3, 2, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_15, 2, 0, 1, 3)

        self.label_37 = QLabel(self.groupBox_14)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_8.addWidget(self.label_37, 5, 0, 1, 1)

        self.label_38 = QLabel(self.groupBox_14)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_8.addWidget(self.label_38, 1, 2, 1, 1)

        self.radioButton_10 = QRadioButton(self.groupBox_14)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout_8.addWidget(self.radioButton_10, 0, 2, 1, 1)

        self.label_39 = QLabel(self.groupBox_14)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_8.addWidget(self.label_39, 7, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox_14)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout_8.addWidget(self.spinBox_6, 1, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_14)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_8.addWidget(self.label_40, 0, 0, 1, 1)

        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_10 = QGridLayout(self.groupBox_16)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox_16)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout_10.addWidget(self.doubleSpinBox_6, 3, 1, 1, 1)

        self.radioButton_11 = QRadioButton(self.groupBox_16)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.gridLayout_10.addWidget(self.radioButton_11, 4, 2, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_16)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout_10.addWidget(self.doubleSpinBox_7, 0, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_16)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_10.addWidget(self.label_41, 5, 0, 1, 1)

        self.label_42 = QLabel(self.groupBox_16)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_10.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_43 = QLabel(self.groupBox_16)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_10.addWidget(self.label_43, 3, 0, 1, 1)

        self.radioButton_12 = QRadioButton(self.groupBox_16)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.gridLayout_10.addWidget(self.radioButton_12, 4, 1, 1, 1)

        self.label_44 = QLabel(self.groupBox_16)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_10.addWidget(self.label_44, 4, 0, 1, 1)

        self.radioButton_13 = QRadioButton(self.groupBox_16)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout_10.addWidget(self.radioButton_13, 5, 2, 1, 1)

        self.radioButton_14 = QRadioButton(self.groupBox_16)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.gridLayout_10.addWidget(self.radioButton_14, 5, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_16)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_10.addWidget(self.label_45, 6, 0, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox_16)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.gridLayout_10.addWidget(self.doubleSpinBox_8, 6, 1, 1, 1)

        self.label_46 = QLabel(self.groupBox_16)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_10.addWidget(self.label_46, 0, 2, 1, 1)

        self.label_47 = QLabel(self.groupBox_16)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_10.addWidget(self.label_47, 3, 2, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_16, 6, 0, 1, 3)

        self.radioButton_15 = QRadioButton(self.groupBox_14)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.gridLayout_8.addWidget(self.radioButton_15, 7, 1, 1, 1)

        self.radioButton_16 = QRadioButton(self.groupBox_14)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.gridLayout_8.addWidget(self.radioButton_16, 7, 2, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_2.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 5, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_4)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_6.addWidget(self.spinBox_2, 0, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_6.addWidget(self.doubleSpinBox, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 3, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox_4)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_6.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 2, 1, 1)

        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 2, 2, 1, 1)

        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 3, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 2, 0, 1, 3)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 1, 2, 1, 1)

        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 0, 2, 1, 1)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 7, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_3)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_7 = QGridLayout(self.groupBox_13)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.gridLayout_7.addWidget(self.doubleSpinBox_3, 3, 1, 1, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_13)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_7.addWidget(self.radioButton_4, 4, 2, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout_7.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_13)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_7.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_13)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_7.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_13)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_7.addWidget(self.label_24, 3, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox_13)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_7.addWidget(self.radioButton_3, 4, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_13)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 4, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.groupBox_13)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_7.addWidget(self.radioButton_6, 5, 2, 1, 1)

        self.radioButton_5 = QRadioButton(self.groupBox_13)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_7.addWidget(self.radioButton_5, 5, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_13)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_7.addWidget(self.label_28, 6, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.gridLayout_7.addWidget(self.doubleSpinBox_4, 6, 1, 1, 1)

        self.label_48 = QLabel(self.groupBox_13)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_7.addWidget(self.label_48, 0, 2, 1, 1)

        self.label_49 = QLabel(self.groupBox_13)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_7.addWidget(self.label_49, 3, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_13, 6, 0, 1, 3)

        self.radioButton_7 = QRadioButton(self.groupBox_3)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout_2.addWidget(self.radioButton_7, 7, 1, 1, 1)

        self.radioButton_8 = QRadioButton(self.groupBox_3)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout_2.addWidget(self.radioButton_8, 7, 2, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.pushButton = QPushButton(Controller_Main)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(Controller_Main)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.groupBox = QGroupBox(Controller_Main)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(2000, 260))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setEnabled(True)
        self.formLayout_5 = QFormLayout(self.groupBox_8)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.output_mode_display = QLabel(self.groupBox_8)
        self.output_mode_display.setObjectName(u"output_mode_display")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.output_mode_display)

        self.OutputMode_display = QTextBrowser(self.groupBox_8)
        self.OutputMode_display.setObjectName(u"OutputMode_display")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.OutputMode_display)

        self.label_13 = QLabel(self.groupBox_8)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.frequency_display = QTextBrowser(self.groupBox_8)
        self.frequency_display.setObjectName(u"frequency_display")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.frequency_display)


        self.gridLayout_4.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.graphicsView_3 = QGraphicsView(self.groupBox_5)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.gridLayout_4.addWidget(self.graphicsView_3, 3, 0, 1, 2)

        self.groupBox_9 = QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.formLayout_6 = QFormLayout(self.groupBox_9)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_14 = QLabel(self.groupBox_9)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.label_15 = QLabel(self.groupBox_9)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.ch1freq_6 = QTextBrowser(self.groupBox_9)
        self.ch1freq_6.setObjectName(u"ch1freq_6")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.FieldRole, self.ch1freq_6)

        self.textBrowser_3 = QTextBrowser(self.groupBox_9)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.textBrowser_3)


        self.gridLayout_4.addWidget(self.groupBox_9, 0, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.groupBox_10 = QGroupBox(self.groupBox)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_5 = QGridLayout(self.groupBox_10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView_4 = QGraphicsView(self.groupBox_10)
        self.graphicsView_4.setObjectName(u"graphicsView_4")

        self.gridLayout_5.addWidget(self.graphicsView_4, 3, 0, 1, 2)

        self.groupBox_11 = QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.formLayout_7 = QFormLayout(self.groupBox_11)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_16 = QLabel(self.groupBox_11)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.label_17 = QLabel(self.groupBox_11)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.ch1freq_7 = QTextBrowser(self.groupBox_11)
        self.ch1freq_7.setObjectName(u"ch1freq_7")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.ch1freq_7)

        self.textBrowser_4 = QTextBrowser(self.groupBox_11)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.textBrowser_4)


        self.gridLayout_5.addWidget(self.groupBox_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_10)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.groupBox_10)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setEnabled(True)
        self.formLayout_8 = QFormLayout(self.groupBox_12)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.output_mode_display_2 = QLabel(self.groupBox_12)
        self.output_mode_display_2.setObjectName(u"output_mode_display_2")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.output_mode_display_2)

        self.OutputMode_display_2 = QTextBrowser(self.groupBox_12)
        self.OutputMode_display_2.setObjectName(u"OutputMode_display_2")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.OutputMode_display_2)

        self.label_18 = QLabel(self.groupBox_12)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.frequency_display_2 = QTextBrowser(self.groupBox_12)
        self.frequency_display_2.setObjectName(u"frequency_display_2")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.FieldRole, self.frequency_display_2)


        self.gridLayout_5.addWidget(self.groupBox_12, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_10)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)


        self.retranslateUi(Controller_Main)

        QMetaObject.connectSlotsByName(Controller_Main)
    # setupUi

    def retranslateUi(self, Controller_Main):
        Controller_Main.setWindowTitle(QCoreApplication.translate("Controller_Main", u"Stimulation Control", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Controller_Main", u"Channel Settings", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
        self.radioButton_9.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.label_30.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Controller_Main", u"Voltage", None))
        self.label_31.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_32.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.label_33.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_34.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_35.setText(QCoreApplication.translate("Controller_Main", u"Amps", None))
        self.label_36.setText(QCoreApplication.translate("Controller_Main", u"Amps", None))
        self.label_37.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.label_38.setText(QCoreApplication.translate("Controller_Main", u"Hertz", None))
        self.radioButton_10.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_39.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.label_40.setText(QCoreApplication.translate("Controller_Main", u"On/Off", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.radioButton_11.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.label_41.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_42.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_43.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_12.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_44.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.radioButton_13.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_14.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_45.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_46.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_47.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.radioButton_15.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.radioButton_16.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2", None))
        self.radioButton_2.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.label_3.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Controller_Main", u"Voltage", None))
        self.label_6.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_5.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.label_19.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_20.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_21.setText(QCoreApplication.translate("Controller_Main", u"Amps", None))
        self.label_22.setText(QCoreApplication.translate("Controller_Main", u"Amps", None))
        self.label_4.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.label_27.setText(QCoreApplication.translate("Controller_Main", u"Hertz", None))
        self.radioButton.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_29.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.label.setText(QCoreApplication.translate("Controller_Main", u"On/Off", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.radioButton_4.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.label_26.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_23.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_24.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_3.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_25.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.radioButton_6.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_5.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_28.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_48.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_49.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.radioButton_7.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.radioButton_8.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.pushButton.setText(QCoreApplication.translate("Controller_Main", u"Apply", None))
        self.pushButton_2.setText(QCoreApplication.translate("Controller_Main", u"Reset", None))
        self.groupBox.setTitle(QCoreApplication.translate("Controller_Main", u"System Status", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
        self.groupBox_8.setTitle("")
        self.output_mode_display.setText(QCoreApplication.translate("Controller_Main", u"Output Mode", None))
        self.label_13.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.groupBox_9.setTitle("")
        self.label_14.setText(QCoreApplication.translate("Controller_Main", u"D188 Channel", None))
        self.label_15.setText(QCoreApplication.translate("Controller_Main", u"Output Current", None))
        self.label_11.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2", None))
        self.groupBox_11.setTitle("")
        self.label_16.setText(QCoreApplication.translate("Controller_Main", u"D188 Channel", None))
        self.label_17.setText(QCoreApplication.translate("Controller_Main", u"Output Current", None))
        self.label_12.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.groupBox_12.setTitle("")
        self.output_mode_display_2.setText(QCoreApplication.translate("Controller_Main", u"Output Mode", None))
        self.label_18.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
    # retranslateUi

