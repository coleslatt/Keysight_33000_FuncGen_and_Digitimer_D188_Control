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
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpinBox, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)
import icons

class Ui_Controller_Main(object):
    def setupUi(self, Controller_Main):
        if not Controller_Main.objectName():
            Controller_Main.setObjectName(u"Controller_Main")
        Controller_Main.resize(1100, 742)
        Controller_Main.setMinimumSize(QSize(1100, 0))
        Controller_Main.setMaximumSize(QSize(1800, 16777215))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        Controller_Main.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/electrode_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Controller_Main.setWindowIcon(icon)
        Controller_Main.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(Controller_Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Controller_Main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -422, 1066, 701))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_14 = QGroupBox(self.groupBox_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_21 = QGridLayout(self.groupBox_14)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_40 = QLabel(self.groupBox_14)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_21.addWidget(self.label_40, 0, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_14)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_21.addWidget(self.label_30, 1, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox_14)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(100000)

        self.gridLayout_21.addWidget(self.spinBox_6, 1, 2, 1, 1)

        self.label_38 = QLabel(self.groupBox_14)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_21.addWidget(self.label_38, 1, 3, 1, 1)

        self.tabWidget = QTabWidget(self.groupBox_14)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_12 = QGridLayout(self.tab)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_15 = QGroupBox(self.tab)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_9 = QGridLayout(self.groupBox_15)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_15)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMinimum(0.000000000000000)
        self.doubleSpinBox_5.setMaximum(50.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_5, 3, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_15)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_9.addWidget(self.label_32, 0, 0, 1, 1)

        self.label_33 = QLabel(self.groupBox_15)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_9.addWidget(self.label_33, 3, 0, 1, 1)

        self.label_34 = QLabel(self.groupBox_15)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_9.addWidget(self.label_34, 0, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_15)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_9.addWidget(self.label_31, 2, 0, 1, 1)

        self.label_36 = QLabel(self.groupBox_15)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_9.addWidget(self.label_36, 3, 2, 1, 1)

        self.label_35 = QLabel(self.groupBox_15)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_9.addWidget(self.label_35, 2, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_15)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_9.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.groupBox_15)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_9.addWidget(self.comboBox_4, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_15, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_15 = QGridLayout(self.tab_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_16 = QGridLayout(self.groupBox_5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_16.addWidget(self.label_8, 1, 0, 1, 1)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.gridLayout_16.addWidget(self.doubleSpinBox_9, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_16.addWidget(self.label_7, 0, 0, 1, 1)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")

        self.gridLayout_16.addWidget(self.doubleSpinBox_10, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_16.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_16.addWidget(self.label_10, 1, 2, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_21.addWidget(self.tabWidget, 2, 0, 1, 5)

        self.label_37 = QLabel(self.groupBox_14)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_21.addWidget(self.label_37, 3, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_14)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_21.addWidget(self.comboBox_2, 3, 2, 1, 1)

        self.label_42 = QLabel(self.groupBox_14)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_21.addWidget(self.label_42, 4, 0, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_14)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout_21.addWidget(self.doubleSpinBox_7, 4, 2, 1, 1)

        self.label_44 = QLabel(self.groupBox_14)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_21.addWidget(self.label_44, 6, 0, 1, 2)

        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_10 = QGridLayout(self.groupBox_16)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox_16)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout_10.addWidget(self.doubleSpinBox_6, 3, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_16)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_10.addWidget(self.label_41, 5, 0, 1, 1)

        self.label_43 = QLabel(self.groupBox_16)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_10.addWidget(self.label_43, 3, 0, 1, 1)

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

        self.label_47 = QLabel(self.groupBox_16)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_10.addWidget(self.label_47, 3, 2, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_16, 8, 0, 1, 5)

        self.label_39 = QLabel(self.groupBox_14)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_21.addWidget(self.label_39, 9, 0, 1, 1)

        self.state_widget = QWidget(self.groupBox_14)
        self.state_widget.setObjectName(u"state_widget")
        self.gridLayout_8 = QGridLayout(self.state_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ch1_on = QRadioButton(self.state_widget)
        self.ch1_on.setObjectName(u"ch1_on")

        self.gridLayout_8.addWidget(self.ch1_on, 0, 0, 1, 1)

        self.ch1_off = QRadioButton(self.state_widget)
        self.ch1_off.setObjectName(u"ch1_off")

        self.gridLayout_8.addWidget(self.ch1_off, 0, 1, 1, 1)


        self.gridLayout_21.addWidget(self.state_widget, 0, 2, 1, 3)

        self.label_46 = QLabel(self.groupBox_14)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_21.addWidget(self.label_46, 4, 3, 1, 1)

        self.state_widget_3 = QWidget(self.groupBox_14)
        self.state_widget_3.setObjectName(u"state_widget_3")
        self.gridLayout_19 = QGridLayout(self.state_widget_3)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.ch1_off_2 = QRadioButton(self.state_widget_3)
        self.ch1_off_2.setObjectName(u"ch1_off_2")

        self.gridLayout_19.addWidget(self.ch1_off_2, 0, 2, 1, 1)

        self.ch1_on_2 = QRadioButton(self.state_widget_3)
        self.ch1_on_2.setObjectName(u"ch1_on_2")

        self.gridLayout_19.addWidget(self.ch1_on_2, 0, 1, 1, 1)


        self.gridLayout_21.addWidget(self.state_widget_3, 6, 2, 1, 3)

        self.widget_2 = QWidget(self.groupBox_14)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_15 = QRadioButton(self.widget_2)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.gridLayout_6.addWidget(self.radioButton_15, 0, 0, 1, 1)

        self.radioButton_16 = QRadioButton(self.widget_2)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.gridLayout_6.addWidget(self.radioButton_16, 0, 1, 1, 1)


        self.gridLayout_21.addWidget(self.widget_2, 9, 1, 1, 4)


        self.gridLayout_2.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 16777215))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximumSize(QSize(60, 50))
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(8)

        self.horizontalLayout_2.addWidget(self.spinBox_7)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout_2.addWidget(self.widget)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.groupBox_2)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_22 = QGridLayout(self.groupBox_21)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_48 = QLabel(self.groupBox_21)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_22.addWidget(self.label_48, 0, 0, 1, 1)

        self.label_49 = QLabel(self.groupBox_21)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_22.addWidget(self.label_49, 1, 0, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox_21)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(100000)

        self.gridLayout_22.addWidget(self.spinBox_8, 1, 2, 1, 1)

        self.label_52 = QLabel(self.groupBox_21)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_22.addWidget(self.label_52, 1, 3, 1, 1)

        self.tabWidget_2 = QTabWidget(self.groupBox_21)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(0, 0))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_14 = QGridLayout(self.tab_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_22 = QGroupBox(self.tab_3)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_11 = QGridLayout(self.groupBox_22)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.doubleSpinBox_11 = QDoubleSpinBox(self.groupBox_22)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setMinimum(0.000000000000000)
        self.doubleSpinBox_11.setMaximum(50.000000000000000)

        self.gridLayout_11.addWidget(self.doubleSpinBox_11, 3, 1, 1, 1)

        self.label_54 = QLabel(self.groupBox_22)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_11.addWidget(self.label_54, 0, 0, 1, 1)

        self.label_55 = QLabel(self.groupBox_22)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_11.addWidget(self.label_55, 3, 0, 1, 1)

        self.label_58 = QLabel(self.groupBox_22)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_11.addWidget(self.label_58, 0, 2, 1, 1)

        self.label_59 = QLabel(self.groupBox_22)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_11.addWidget(self.label_59, 2, 0, 1, 1)

        self.label_60 = QLabel(self.groupBox_22)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_11.addWidget(self.label_60, 3, 2, 1, 1)

        self.label_61 = QLabel(self.groupBox_22)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_11.addWidget(self.label_61, 2, 2, 1, 1)

        self.comboBox_5 = QComboBox(self.groupBox_22)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_11.addWidget(self.comboBox_5, 0, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox_22)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_11.addWidget(self.comboBox_6, 2, 1, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_17 = QGridLayout(self.tab_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_9 = QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_18 = QGridLayout(self.groupBox_9)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_18.addWidget(self.label_11, 1, 0, 1, 1)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")

        self.gridLayout_18.addWidget(self.doubleSpinBox_12, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_18.addWidget(self.label_12, 0, 0, 1, 1)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")

        self.gridLayout_18.addWidget(self.doubleSpinBox_13, 1, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_18.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_9)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_18.addWidget(self.label_14, 1, 2, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.gridLayout_22.addWidget(self.tabWidget_2, 2, 0, 1, 5)

        self.label_62 = QLabel(self.groupBox_21)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_22.addWidget(self.label_62, 3, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.groupBox_21)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_22.addWidget(self.comboBox_7, 3, 2, 1, 1)

        self.label_63 = QLabel(self.groupBox_21)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_22.addWidget(self.label_63, 4, 0, 1, 1)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.groupBox_21)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")

        self.gridLayout_22.addWidget(self.doubleSpinBox_14, 4, 2, 1, 1)

        self.label_64 = QLabel(self.groupBox_21)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_22.addWidget(self.label_64, 6, 0, 1, 2)

        self.groupBox_23 = QGroupBox(self.groupBox_21)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_20 = QGridLayout(self.groupBox_23)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.doubleSpinBox_15 = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")

        self.gridLayout_20.addWidget(self.doubleSpinBox_15, 3, 1, 1, 1)

        self.label_65 = QLabel(self.groupBox_23)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_20.addWidget(self.label_65, 5, 0, 1, 1)

        self.label_66 = QLabel(self.groupBox_23)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_20.addWidget(self.label_66, 3, 0, 1, 1)

        self.radioButton_17 = QRadioButton(self.groupBox_23)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.gridLayout_20.addWidget(self.radioButton_17, 5, 2, 1, 1)

        self.radioButton_18 = QRadioButton(self.groupBox_23)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.gridLayout_20.addWidget(self.radioButton_18, 5, 1, 1, 1)

        self.label_67 = QLabel(self.groupBox_23)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_20.addWidget(self.label_67, 6, 0, 1, 1)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")

        self.gridLayout_20.addWidget(self.doubleSpinBox_16, 6, 1, 1, 1)

        self.label_68 = QLabel(self.groupBox_23)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_20.addWidget(self.label_68, 3, 2, 1, 1)


        self.gridLayout_22.addWidget(self.groupBox_23, 8, 0, 1, 5)

        self.label_69 = QLabel(self.groupBox_21)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_22.addWidget(self.label_69, 9, 0, 1, 1)

        self.state_widget_2 = QWidget(self.groupBox_21)
        self.state_widget_2.setObjectName(u"state_widget_2")
        self.gridLayout_23 = QGridLayout(self.state_widget_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.ch1_on_3 = QRadioButton(self.state_widget_2)
        self.ch1_on_3.setObjectName(u"ch1_on_3")

        self.gridLayout_23.addWidget(self.ch1_on_3, 0, 0, 1, 1)

        self.ch1_off_3 = QRadioButton(self.state_widget_2)
        self.ch1_off_3.setObjectName(u"ch1_off_3")

        self.gridLayout_23.addWidget(self.ch1_off_3, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.state_widget_2, 0, 2, 1, 3)

        self.label_70 = QLabel(self.groupBox_21)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_22.addWidget(self.label_70, 4, 3, 1, 1)

        self.state_widget_4 = QWidget(self.groupBox_21)
        self.state_widget_4.setObjectName(u"state_widget_4")
        self.gridLayout_24 = QGridLayout(self.state_widget_4)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.ch1_off_4 = QRadioButton(self.state_widget_4)
        self.ch1_off_4.setObjectName(u"ch1_off_4")

        self.gridLayout_24.addWidget(self.ch1_off_4, 0, 2, 1, 1)

        self.ch1_on_4 = QRadioButton(self.state_widget_4)
        self.ch1_on_4.setObjectName(u"ch1_on_4")

        self.gridLayout_24.addWidget(self.ch1_on_4, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.state_widget_4, 6, 2, 1, 3)

        self.widget_3 = QWidget(self.groupBox_21)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radioButton_19 = QRadioButton(self.widget_3)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.gridLayout_7.addWidget(self.radioButton_19, 0, 0, 1, 1)

        self.radioButton_20 = QRadioButton(self.widget_3)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.gridLayout_7.addWidget(self.radioButton_20, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.widget_3, 9, 1, 1, 4)


        self.gridLayout_2.addWidget(self.groupBox_21, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 2)

        self.pushButton = QPushButton(Controller_Main)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.system_status = QGroupBox(Controller_Main)
        self.system_status.setObjectName(u"system_status")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_status.sizePolicy().hasHeightForWidth())
        self.system_status.setSizePolicy(sizePolicy)
        self.system_status.setMinimumSize(QSize(0, 400))
        self.system_status.setMaximumSize(QSize(2000, 400))
        self.gridLayout_29 = QGridLayout(self.system_status)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.d188_ch = QGroupBox(self.system_status)
        self.d188_ch.setObjectName(u"d188_ch")
        self.d188_ch.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.d188_ch.sizePolicy().hasHeightForWidth())
        self.d188_ch.setSizePolicy(sizePolicy1)
        self.d188_ch.setMinimumSize(QSize(0, 50))
        self.d188_ch.setMaximumSize(QSize(16777215, 50))
        self.d188_ch.setBaseSize(QSize(0, 100))
        self.gridLayout_30 = QGridLayout(self.d188_ch)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_28 = QLabel(self.d188_ch)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_30.addWidget(self.label_28, 0, 0, 1, 1)

        self.textBrowser_10 = QTextBrowser(self.d188_ch)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        sizePolicy1.setHeightForWidth(self.textBrowser_10.sizePolicy().hasHeightForWidth())
        self.textBrowser_10.setSizePolicy(sizePolicy1)
        self.textBrowser_10.setMaximumSize(QSize(50, 40))

        self.gridLayout_30.addWidget(self.textBrowser_10, 0, 1, 1, 1)


        self.gridLayout_29.addWidget(self.d188_ch, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.system_status)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_4 = QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.channel1_settings_2 = QGroupBox(self.groupBox_8)
        self.channel1_settings_2.setObjectName(u"channel1_settings_2")
        self.channel1_settings_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.channel1_settings_2.sizePolicy().hasHeightForWidth())
        self.channel1_settings_2.setSizePolicy(sizePolicy2)
        self.channel1_settings_2.setMinimumSize(QSize(180, 100))
        self.channel1_settings_2.setMaximumSize(QSize(16777215, 220))
        self.channel1_settings_2.setFlat(False)
        self.channel1_settings_2.setCheckable(False)
        self.gridLayout_25 = QGridLayout(self.channel1_settings_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.widget_6 = QWidget(self.channel1_settings_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.gridLayout_28 = QGridLayout(self.widget_6)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_57 = QLabel(self.widget_6)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_28.addWidget(self.label_57, 1, 0, 1, 1)

        self.label_22 = QLabel(self.widget_6)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_28.addWidget(self.label_22, 2, 3, 1, 1)

        self.textBrowser_7 = QTextBrowser(self.widget_6)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textBrowser_7.sizePolicy().hasHeightForWidth())
        self.textBrowser_7.setSizePolicy(sizePolicy3)

        self.gridLayout_28.addWidget(self.textBrowser_7, 0, 5, 1, 1)

        self.OutputMode_display_8 = QTextBrowser(self.widget_6)
        self.OutputMode_display_8.setObjectName(u"OutputMode_display_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.OutputMode_display_8.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_8.setSizePolicy(sizePolicy4)

        self.gridLayout_28.addWidget(self.OutputMode_display_8, 1, 5, 1, 2)

        self.OutputMode_display_5 = QTextBrowser(self.widget_6)
        self.OutputMode_display_5.setObjectName(u"OutputMode_display_5")
        sizePolicy3.setHeightForWidth(self.OutputMode_display_5.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_5.setSizePolicy(sizePolicy3)

        self.gridLayout_28.addWidget(self.OutputMode_display_5, 0, 2, 1, 1)

        self.frequency_display_5 = QTextBrowser(self.widget_6)
        self.frequency_display_5.setObjectName(u"frequency_display_5")
        self.frequency_display_5.setMinimumSize(QSize(70, 0))
        self.frequency_display_5.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoBulletList)
        self.frequency_display_5.setCursorWidth(1)

        self.gridLayout_28.addWidget(self.frequency_display_5, 1, 2, 1, 1)

        self.label_23 = QLabel(self.widget_6)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_28.addWidget(self.label_23, 1, 3, 1, 1)

        self.label_24 = QLabel(self.widget_6)
        self.label_24.setObjectName(u"label_24")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)

        self.gridLayout_28.addWidget(self.label_24, 2, 0, 2, 2)

        self.label_71 = QLabel(self.widget_6)
        self.label_71.setObjectName(u"label_71")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy6)
        self.label_71.setMinimumSize(QSize(100, 0))
        self.label_71.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_28.addWidget(self.label_71, 1, 4, 1, 1)

        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy7)
        self.label_25.setMinimumSize(QSize(90, 0))
        self.label_25.setBaseSize(QSize(90, 0))

        self.gridLayout_28.addWidget(self.label_25, 0, 4, 1, 1)

        self.output_mode_display_5 = QLabel(self.widget_6)
        self.output_mode_display_5.setObjectName(u"output_mode_display_5")
        self.output_mode_display_5.setMinimumSize(QSize(100, 0))

        self.gridLayout_28.addWidget(self.output_mode_display_5, 0, 0, 1, 1)

        self.textBrowser_8 = QTextBrowser(self.widget_6)
        self.textBrowser_8.setObjectName(u"textBrowser_8")

        self.gridLayout_28.addWidget(self.textBrowser_8, 2, 2, 1, 1)

        self.textBrowser_9 = QTextBrowser(self.widget_6)
        self.textBrowser_9.setObjectName(u"textBrowser_9")

        self.gridLayout_28.addWidget(self.textBrowser_9, 0, 6, 1, 1)

        self.label_26 = QLabel(self.widget_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_28.addWidget(self.label_26, 0, 7, 1, 1)

        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_28.addWidget(self.label_27, 1, 7, 1, 1)


        self.gridLayout_25.addWidget(self.widget_6, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.channel1_settings_2, 0, 1, 1, 1)

        self.graphicsView_2 = QGraphicsView(self.groupBox_8)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout_4.addWidget(self.graphicsView_2, 1, 1, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_8, 0, 2, 1, 1)

        self.groupBox_7 = QGroupBox(self.system_status)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_3 = QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphicsView = QGraphicsView(self.groupBox_7)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 1, 0, 1, 1)

        self.channel1_settings = QGroupBox(self.groupBox_7)
        self.channel1_settings.setObjectName(u"channel1_settings")
        self.channel1_settings.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.channel1_settings.sizePolicy().hasHeightForWidth())
        self.channel1_settings.setSizePolicy(sizePolicy2)
        self.channel1_settings.setMinimumSize(QSize(180, 100))
        self.channel1_settings.setMaximumSize(QSize(16777215, 220))
        self.channel1_settings.setFlat(False)
        self.channel1_settings.setCheckable(False)
        self.gridLayout_5 = QGridLayout(self.channel1_settings)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_4 = QWidget(self.channel1_settings)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.gridLayout_26 = QGridLayout(self.widget_4)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_50 = QLabel(self.widget_4)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_26.addWidget(self.label_50, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_26.addWidget(self.label_6, 2, 3, 1, 1)

        self.textBrowser = QTextBrowser(self.widget_4)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy3.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy3)

        self.gridLayout_26.addWidget(self.textBrowser, 0, 5, 1, 1)

        self.OutputMode_display_6 = QTextBrowser(self.widget_4)
        self.OutputMode_display_6.setObjectName(u"OutputMode_display_6")
        sizePolicy4.setHeightForWidth(self.OutputMode_display_6.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_6.setSizePolicy(sizePolicy4)

        self.gridLayout_26.addWidget(self.OutputMode_display_6, 1, 5, 1, 2)

        self.OutputMode_display_3 = QTextBrowser(self.widget_4)
        self.OutputMode_display_3.setObjectName(u"OutputMode_display_3")
        sizePolicy3.setHeightForWidth(self.OutputMode_display_3.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_3.setSizePolicy(sizePolicy3)

        self.gridLayout_26.addWidget(self.OutputMode_display_3, 0, 2, 1, 1)

        self.frequency_display_3 = QTextBrowser(self.widget_4)
        self.frequency_display_3.setObjectName(u"frequency_display_3")
        self.frequency_display_3.setMinimumSize(QSize(70, 0))
        self.frequency_display_3.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoBulletList)
        self.frequency_display_3.setCursorWidth(1)

        self.gridLayout_26.addWidget(self.frequency_display_3, 1, 2, 1, 1)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_26.addWidget(self.label_5, 1, 3, 1, 1)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)

        self.gridLayout_26.addWidget(self.label_4, 2, 0, 2, 2)

        self.label_53 = QLabel(self.widget_4)
        self.label_53.setObjectName(u"label_53")
        sizePolicy6.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy6)
        self.label_53.setMinimumSize(QSize(100, 0))
        self.label_53.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_26.addWidget(self.label_53, 1, 4, 1, 1)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        sizePolicy7.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy7)
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setBaseSize(QSize(90, 0))

        self.gridLayout_26.addWidget(self.label, 0, 4, 1, 1)

        self.output_mode_display_3 = QLabel(self.widget_4)
        self.output_mode_display_3.setObjectName(u"output_mode_display_3")
        self.output_mode_display_3.setMinimumSize(QSize(100, 0))

        self.gridLayout_26.addWidget(self.output_mode_display_3, 0, 0, 1, 1)

        self.textBrowser_5 = QTextBrowser(self.widget_4)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.gridLayout_26.addWidget(self.textBrowser_5, 2, 2, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.widget_4)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_26.addWidget(self.textBrowser_2, 0, 6, 1, 1)

        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_26.addWidget(self.label_15, 0, 7, 1, 1)

        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_26.addWidget(self.label_16, 1, 7, 1, 1)


        self.gridLayout_5.addWidget(self.widget_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.channel1_settings, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_7, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.system_status, 0, 0, 1, 2)

        self.pushButton_2 = QPushButton(Controller_Main)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)


        self.retranslateUi(Controller_Main)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Controller_Main)
    # setupUi

    def retranslateUi(self, Controller_Main):
        Controller_Main.setWindowTitle(QCoreApplication.translate("Controller_Main", u"Stimulation Control", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Controller_Main", u"Channel Settings", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
        self.label_40.setText(QCoreApplication.translate("Controller_Main", u"On/Off", None))
        self.label_30.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_38.setText(QCoreApplication.translate("Controller_Main", u"Hertz", None))
        self.groupBox_15.setTitle("")
        self.label_32.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.label_33.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_34.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_31.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_36.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.label_35.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Controller_Main", u"1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Controller_Main", u"5", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Controller_Main", u"10", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("Controller_Main", u"10", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Controller_Main", u"25", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Controller_Main", u"50", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Controller_Main", u"DS5 Control", None))
        self.groupBox_5.setTitle("")
        self.label_8.setText(QCoreApplication.translate("Controller_Main", u"Voltage High", None))
        self.label_7.setText(QCoreApplication.translate("Controller_Main", u"Voltage Low", None))
        self.label_9.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_10.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Controller_Main", u"FuncGen Control", None))
        self.label_37.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.label_42.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_44.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.label_41.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_43.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_13.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_14.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_45.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_47.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_39.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.ch1_on.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.ch1_off.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_46.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.ch1_off_2.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.ch1_on_2.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.radioButton_15.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.radioButton_16.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Controller_Main", u"D188 Channel", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2", None))
        self.label_48.setText(QCoreApplication.translate("Controller_Main", u"On/Off", None))
        self.label_49.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_52.setText(QCoreApplication.translate("Controller_Main", u"Hertz", None))
        self.groupBox_22.setTitle("")
        self.label_54.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.label_55.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_58.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_59.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_60.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.label_61.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Controller_Main", u"1", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Controller_Main", u"5", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("Controller_Main", u"10", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("Controller_Main", u"10", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Controller_Main", u"25", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Controller_Main", u"50", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Controller_Main", u"DS5 Control", None))
        self.groupBox_9.setTitle("")
        self.label_11.setText(QCoreApplication.translate("Controller_Main", u"Voltage High", None))
        self.label_12.setText(QCoreApplication.translate("Controller_Main", u"Voltage Low", None))
        self.label_13.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_14.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Controller_Main", u"FuncGen Control", None))
        self.label_62.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.label_63.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_64.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.label_65.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_66.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_17.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_18.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_67.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_68.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_69.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.ch1_on_3.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.ch1_off_3.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_70.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.ch1_off_4.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.ch1_on_4.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.radioButton_19.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.radioButton_20.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.pushButton.setText(QCoreApplication.translate("Controller_Main", u"Apply", None))
        self.system_status.setTitle(QCoreApplication.translate("Controller_Main", u"System Status", None))
        self.d188_ch.setTitle("")
        self.label_28.setText(QCoreApplication.translate("Controller_Main", u"D188 Channel", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
        self.channel1_settings_2.setTitle("")
        self.label_57.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_22.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_23.setText(QCoreApplication.translate("Controller_Main", u"Hz", None))
        self.label_24.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_71.setText(QCoreApplication.translate("Controller_Main", u"DS5 Current", None))
        self.label_25.setText(QCoreApplication.translate("Controller_Main", u"VMin/VMax", None))
        self.output_mode_display_5.setText(QCoreApplication.translate("Controller_Main", u"On/Off", None))
        self.label_26.setText(QCoreApplication.translate("Controller_Main", u"V", None))
        self.label_27.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
        self.channel1_settings.setTitle("")
        self.label_50.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_6.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_5.setText(QCoreApplication.translate("Controller_Main", u"Hz", None))
        self.label_4.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_53.setText(QCoreApplication.translate("Controller_Main", u"DS5 Current", None))
        self.label.setText(QCoreApplication.translate("Controller_Main", u"VMin/VMax", None))
        self.output_mode_display_3.setText(QCoreApplication.translate("Controller_Main", u"On/Off", None))
        self.label_15.setText(QCoreApplication.translate("Controller_Main", u"V", None))
        self.label_16.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.pushButton_2.setText(QCoreApplication.translate("Controller_Main", u"Reset", None))
    # retranslateUi

