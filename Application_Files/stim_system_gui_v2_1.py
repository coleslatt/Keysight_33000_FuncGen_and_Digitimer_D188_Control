# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stim_system_gui_version2.ui'
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
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)
import icons

class Ui_Controller_Main(object):
    def setupUi(self, Controller_Main):
        if not Controller_Main.objectName():
            Controller_Main.setObjectName(u"Controller_Main")
        Controller_Main.resize(1100, 943)
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
        self.modeSelektor = QTabWidget(Controller_Main)
        self.modeSelektor.setObjectName(u"modeSelektor")
        self.ContinuousMode = QWidget()
        self.ContinuousMode.setObjectName(u"ContinuousMode")
        self.gridLayout_54 = QGridLayout(self.ContinuousMode)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.scrollArea = QScrollArea(self.ContinuousMode)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -190, 1042, 707))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.channel2_settings = QGroupBox(self.groupBox_2)
        self.channel2_settings.setObjectName(u"channel2_settings")
        self.gridLayout_22 = QGridLayout(self.channel2_settings)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_49 = QLabel(self.channel2_settings)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_22.addWidget(self.label_49, 1, 0, 1, 1)

        self.label_64 = QLabel(self.channel2_settings)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_22.addWidget(self.label_64, 6, 0, 1, 2)

        self.label_62 = QLabel(self.channel2_settings)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_22.addWidget(self.label_62, 3, 0, 1, 1)

        self.label_48 = QLabel(self.channel2_settings)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_22.addWidget(self.label_48, 0, 0, 1, 1)

        self.state_widget_4 = QWidget(self.channel2_settings)
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

        self.comboBox_7 = QComboBox(self.channel2_settings)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_22.addWidget(self.comboBox_7, 3, 2, 1, 1)

        self.state_widget_2 = QWidget(self.channel2_settings)
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

        self.tabWidget_2 = QTabWidget(self.channel2_settings)
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

        self.label_70 = QLabel(self.channel2_settings)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_22.addWidget(self.label_70, 4, 3, 1, 1)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.channel2_settings)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")

        self.gridLayout_22.addWidget(self.doubleSpinBox_14, 4, 2, 1, 1)

        self.label_52 = QLabel(self.channel2_settings)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_22.addWidget(self.label_52, 1, 3, 1, 1)

        self.label_69 = QLabel(self.channel2_settings)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_22.addWidget(self.label_69, 9, 0, 1, 1)

        self.spinBox_8 = QSpinBox(self.channel2_settings)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(100000)

        self.gridLayout_22.addWidget(self.spinBox_8, 1, 2, 1, 1)

        self.groupBox_23 = QGroupBox(self.channel2_settings)
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

        self.label_63 = QLabel(self.channel2_settings)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_22.addWidget(self.label_63, 4, 0, 1, 1)

        self.widget_3 = QWidget(self.channel2_settings)
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


        self.gridLayout_2.addWidget(self.channel2_settings, 0, 1, 1, 1)

        self.channel1_settings_3 = QGroupBox(self.groupBox_2)
        self.channel1_settings_3.setObjectName(u"channel1_settings_3")
        self.gridLayout_21 = QGridLayout(self.channel1_settings_3)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_40 = QLabel(self.channel1_settings_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_21.addWidget(self.label_40, 0, 0, 1, 1)

        self.label_30 = QLabel(self.channel1_settings_3)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_21.addWidget(self.label_30, 1, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.channel1_settings_3)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(100000)

        self.gridLayout_21.addWidget(self.spinBox_6, 1, 2, 1, 1)

        self.label_38 = QLabel(self.channel1_settings_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_21.addWidget(self.label_38, 1, 3, 1, 1)

        self.tabWidget = QTabWidget(self.channel1_settings_3)
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

        self.label_37 = QLabel(self.channel1_settings_3)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_21.addWidget(self.label_37, 3, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.channel1_settings_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_21.addWidget(self.comboBox_2, 3, 2, 1, 1)

        self.label_42 = QLabel(self.channel1_settings_3)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_21.addWidget(self.label_42, 4, 0, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.channel1_settings_3)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout_21.addWidget(self.doubleSpinBox_7, 4, 2, 1, 1)

        self.label_44 = QLabel(self.channel1_settings_3)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_21.addWidget(self.label_44, 6, 0, 1, 2)

        self.groupBox_16 = QGroupBox(self.channel1_settings_3)
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

        self.label_39 = QLabel(self.channel1_settings_3)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_21.addWidget(self.label_39, 9, 0, 1, 1)

        self.state_widget = QWidget(self.channel1_settings_3)
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

        self.label_46 = QLabel(self.channel1_settings_3)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_21.addWidget(self.label_46, 4, 3, 1, 1)

        self.state_widget_3 = QWidget(self.channel1_settings_3)
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

        self.widget_2 = QWidget(self.channel1_settings_3)
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


        self.gridLayout_2.addWidget(self.channel1_settings_3, 0, 0, 1, 1)

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


        self.verticalLayout.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_54.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.ContinuousMode)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setMinimumSize(QSize(100, 50))
        self.gridLayout_75 = QGridLayout(self.widget_14)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.pushButton = QPushButton(self.widget_14)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_75.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_14)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_75.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.gridLayout_54.addWidget(self.widget_14, 1, 0, 1, 1)

        self.modeSelektor.addTab(self.ContinuousMode, "")
        self.BurstMode = QWidget()
        self.BurstMode.setObjectName(u"BurstMode")
        self.gridLayout_13 = QGridLayout(self.BurstMode)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget_15 = QWidget(self.BurstMode)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.widget_15.setMinimumSize(QSize(0, 50))
        self.gridLayout_76 = QGridLayout(self.widget_15)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.pushButton_3 = QPushButton(self.widget_15)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_76.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_15)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_76.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_15, 1, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.BurstMode)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1092, 1094))
        self.gridLayout_55 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.BurstModeSettings = QGroupBox(self.scrollAreaWidgetContents_2)
        self.BurstModeSettings.setObjectName(u"BurstModeSettings")
        self.gridLayout_39 = QGridLayout(self.BurstModeSettings)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.Channel2Delay = QWidget(self.BurstModeSettings)
        self.Channel2Delay.setObjectName(u"Channel2Delay")
        self.gridLayout_47 = QGridLayout(self.Channel2Delay)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.groupBox_11 = QGroupBox(self.Channel2Delay)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_44 = QGridLayout(self.groupBox_11)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_95 = QLabel(self.groupBox_11)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_44.addWidget(self.label_95, 0, 4, 1, 1)

        self.jitter_widge_2 = QWidget(self.groupBox_11)
        self.jitter_widge_2.setObjectName(u"jitter_widge_2")
        self.gridLayout_48 = QGridLayout(self.jitter_widge_2)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.jitter_widget_2 = QWidget(self.jitter_widge_2)
        self.jitter_widget_2.setObjectName(u"jitter_widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.jitter_widget_2.sizePolicy().hasHeightForWidth())
        self.jitter_widget_2.setSizePolicy(sizePolicy2)
        self.jitter_widget_2.setMinimumSize(QSize(0, 60))
        self.gridLayout_51 = QGridLayout(self.jitter_widget_2)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.widget_12 = QWidget(self.jitter_widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_52 = QGridLayout(self.widget_12)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_100 = QLabel(self.widget_12)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_52.addWidget(self.label_100, 0, 2, 1, 1)

        self.label_99 = QLabel(self.widget_12)
        self.label_99.setObjectName(u"label_99")
        sizePolicy2.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy2)
        self.label_99.setMinimumSize(QSize(0, 15))
        self.label_99.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_99.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_52.addWidget(self.label_99, 0, 0, 1, 1)

        self.doubleSpinBox_23 = QDoubleSpinBox(self.widget_12)
        self.doubleSpinBox_23.setObjectName(u"doubleSpinBox_23")

        self.gridLayout_52.addWidget(self.doubleSpinBox_23, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_52.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)


        self.gridLayout_51.addWidget(self.widget_12, 1, 1, 2, 1)

        self.Jitter_3 = QWidget(self.jitter_widget_2)
        self.Jitter_3.setObjectName(u"Jitter_3")
        self.gridLayout_53 = QGridLayout(self.Jitter_3)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.jitter_on_2 = QRadioButton(self.Jitter_3)
        self.jitter_on_2.setObjectName(u"jitter_on_2")

        self.gridLayout_53.addWidget(self.jitter_on_2, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.jitter_label_2 = QLabel(self.Jitter_3)
        self.jitter_label_2.setObjectName(u"jitter_label_2")
        sizePolicy2.setHeightForWidth(self.jitter_label_2.sizePolicy().hasHeightForWidth())
        self.jitter_label_2.setSizePolicy(sizePolicy2)
        self.jitter_label_2.setMinimumSize(QSize(0, 15))

        self.gridLayout_53.addWidget(self.jitter_label_2, 0, 1, 1, 1)

        self.jitter_off_2 = QRadioButton(self.Jitter_3)
        self.jitter_off_2.setObjectName(u"jitter_off_2")

        self.gridLayout_53.addWidget(self.jitter_off_2, 0, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_53.addItem(self.horizontalSpacer_9, 0, 4, 1, 1)


        self.gridLayout_51.addWidget(self.Jitter_3, 1, 0, 2, 1)


        self.gridLayout_48.addWidget(self.jitter_widget_2, 2, 0, 1, 1)

        self.line_2 = QFrame(self.jitter_widge_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_48.addWidget(self.line_2, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.jitter_widge_2, 1, 0, 1, 5)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.gridLayout_44.addWidget(self.doubleSpinBox_3, 0, 3, 1, 1)

        self.label_88 = QLabel(self.groupBox_11)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_44.addWidget(self.label_88, 0, 2, 1, 1)

        self.widget_9 = QWidget(self.groupBox_11)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_45 = QGridLayout(self.widget_9)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.radioButton_5 = QRadioButton(self.widget_9)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_45.addWidget(self.radioButton_5, 0, 1, 1, 1)

        self.label_21 = QLabel(self.widget_9)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_45.addWidget(self.label_21, 0, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.widget_9)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_45.addWidget(self.radioButton_6, 0, 2, 1, 1)


        self.gridLayout_44.addWidget(self.widget_9, 0, 1, 1, 1)


        self.gridLayout_47.addWidget(self.groupBox_11, 0, 0, 1, 2)


        self.gridLayout_39.addWidget(self.Channel2Delay, 2, 0, 1, 1)

        self.PulseSettings = QGroupBox(self.BurstModeSettings)
        self.PulseSettings.setObjectName(u"PulseSettings")
        self.gridLayout_40 = QGridLayout(self.PulseSettings)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.PulseSettings)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_40.addWidget(self.doubleSpinBox, 0, 8, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.widget_7 = QWidget(self.PulseSettings)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_41 = QGridLayout(self.widget_7)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_89 = QLabel(self.widget_7)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_41.addWidget(self.label_89, 1, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget_7)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_41.addWidget(self.radioButton_2, 1, 2, 1, 1)


        self.gridLayout_40.addWidget(self.widget_7, 0, 3, 1, 1)

        self.spinBox = QSpinBox(self.PulseSettings)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_40.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_90 = QLabel(self.PulseSettings)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_40.addWidget(self.label_90, 0, 9, 1, 1)

        self.label_29 = QLabel(self.PulseSettings)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_40.addWidget(self.label_29, 0, 7, 1, 1)

        self.radioButton = QRadioButton(self.PulseSettings)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_40.addWidget(self.radioButton, 0, 4, 1, 1)

        self.label_3 = QLabel(self.PulseSettings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_40.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.PulseSettings, 1, 0, 1, 1)

        self.StimSettings = QGroupBox(self.BurstModeSettings)
        self.StimSettings.setObjectName(u"StimSettings")
        self.gridLayout_42 = QGridLayout(self.StimSettings)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.horizontalSpacer_3 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.line = QFrame(self.StimSettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_42.addWidget(self.line, 1, 0, 1, 9)

        self.num_stims = QSpinBox(self.StimSettings)
        self.num_stims.setObjectName(u"num_stims")

        self.gridLayout_42.addWidget(self.num_stims, 0, 1, 1, 1)

        self.interstim_delay_2 = QLabel(self.StimSettings)
        self.interstim_delay_2.setObjectName(u"interstim_delay_2")

        self.gridLayout_42.addWidget(self.interstim_delay_2, 0, 6, 1, 1)

        self.num_stims_label = QLabel(self.StimSettings)
        self.num_stims_label.setObjectName(u"num_stims_label")

        self.gridLayout_42.addWidget(self.num_stims_label, 0, 0, 1, 1)

        self.interstim_delay = QDoubleSpinBox(self.StimSettings)
        self.interstim_delay.setObjectName(u"interstim_delay")

        self.gridLayout_42.addWidget(self.interstim_delay, 0, 7, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_4, 0, 5, 1, 1)

        self.freq_select_stim = QRadioButton(self.StimSettings)
        self.freq_select_stim.setObjectName(u"freq_select_stim")

        self.gridLayout_42.addWidget(self.freq_select_stim, 0, 4, 1, 1)

        self.widget_8 = QWidget(self.StimSettings)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_43 = QGridLayout(self.widget_8)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_91 = QLabel(self.widget_8)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_43.addWidget(self.label_91, 1, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.widget_8)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_43.addWidget(self.radioButton_4, 1, 2, 1, 1)


        self.gridLayout_42.addWidget(self.widget_8, 0, 3, 1, 1)

        self.label_92 = QLabel(self.StimSettings)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_42.addWidget(self.label_92, 0, 8, 1, 1)

        self.jitter_widget = QWidget(self.StimSettings)
        self.jitter_widget.setObjectName(u"jitter_widget")
        sizePolicy2.setHeightForWidth(self.jitter_widget.sizePolicy().hasHeightForWidth())
        self.jitter_widget.setSizePolicy(sizePolicy2)
        self.jitter_widget.setMinimumSize(QSize(0, 60))
        self.gridLayout_49 = QGridLayout(self.jitter_widget)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.widget_11 = QWidget(self.jitter_widget)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_50 = QGridLayout(self.widget_11)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.label_97 = QLabel(self.widget_11)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_97.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_50.addWidget(self.label_97, 0, 0, 1, 1)

        self.label_98 = QLabel(self.widget_11)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_50.addWidget(self.label_98, 0, 2, 1, 1)

        self.jitter_rate = QDoubleSpinBox(self.widget_11)
        self.jitter_rate.setObjectName(u"jitter_rate")

        self.gridLayout_50.addWidget(self.jitter_rate, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)


        self.gridLayout_49.addWidget(self.widget_11, 1, 1, 2, 1)

        self.Jitter = QWidget(self.jitter_widget)
        self.Jitter.setObjectName(u"Jitter")
        self.gridLayout_46 = QGridLayout(self.Jitter)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.jitter_on = QRadioButton(self.Jitter)
        self.jitter_on.setObjectName(u"jitter_on")

        self.gridLayout_46.addWidget(self.jitter_on, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.jitter_label = QLabel(self.Jitter)
        self.jitter_label.setObjectName(u"jitter_label")

        self.gridLayout_46.addWidget(self.jitter_label, 0, 1, 1, 1)

        self.jitter_off = QRadioButton(self.Jitter)
        self.jitter_off.setObjectName(u"jitter_off")

        self.gridLayout_46.addWidget(self.jitter_off, 0, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)


        self.gridLayout_49.addWidget(self.Jitter, 1, 0, 2, 1)


        self.gridLayout_42.addWidget(self.jitter_widget, 2, 0, 1, 9)


        self.gridLayout_39.addWidget(self.StimSettings, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.BurstModeSettings)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_74 = QGridLayout(self.groupBox_3)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.channel1_settings_4 = QGroupBox(self.groupBox_3)
        self.channel1_settings_4.setObjectName(u"channel1_settings_4")
        self.gridLayout_56 = QGridLayout(self.channel1_settings_4)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.widget_10 = QWidget(self.channel1_settings_4)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_64 = QGridLayout(self.widget_10)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.radioButton_27 = QRadioButton(self.widget_10)
        self.radioButton_27.setObjectName(u"radioButton_27")

        self.gridLayout_64.addWidget(self.radioButton_27, 0, 0, 1, 1)

        self.radioButton_28 = QRadioButton(self.widget_10)
        self.radioButton_28.setObjectName(u"radioButton_28")

        self.gridLayout_64.addWidget(self.radioButton_28, 0, 1, 1, 1)


        self.gridLayout_56.addWidget(self.widget_10, 8, 1, 1, 4)

        self.comboBox_13 = QComboBox(self.channel1_settings_4)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")

        self.gridLayout_56.addWidget(self.comboBox_13, 2, 2, 1, 1)

        self.label_114 = QLabel(self.channel1_settings_4)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_56.addWidget(self.label_114, 3, 0, 1, 1)

        self.doubleSpinBox_27 = QDoubleSpinBox(self.channel1_settings_4)
        self.doubleSpinBox_27.setObjectName(u"doubleSpinBox_27")

        self.gridLayout_56.addWidget(self.doubleSpinBox_27, 3, 2, 1, 1)

        self.label_113 = QLabel(self.channel1_settings_4)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_56.addWidget(self.label_113, 2, 0, 1, 1)

        self.tabWidget_3 = QTabWidget(self.channel1_settings_4)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setMinimumSize(QSize(0, 0))
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_57 = QGridLayout(self.tab_8)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.groupBox_17 = QGroupBox(self.tab_8)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_58 = QGridLayout(self.groupBox_17)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.doubleSpinBox_24 = QDoubleSpinBox(self.groupBox_17)
        self.doubleSpinBox_24.setObjectName(u"doubleSpinBox_24")
        self.doubleSpinBox_24.setMinimum(0.000000000000000)
        self.doubleSpinBox_24.setMaximum(50.000000000000000)

        self.gridLayout_58.addWidget(self.doubleSpinBox_24, 3, 1, 1, 1)

        self.label_103 = QLabel(self.groupBox_17)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_58.addWidget(self.label_103, 0, 0, 1, 1)

        self.label_104 = QLabel(self.groupBox_17)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_58.addWidget(self.label_104, 3, 0, 1, 1)

        self.label_105 = QLabel(self.groupBox_17)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_58.addWidget(self.label_105, 0, 2, 1, 1)

        self.label_106 = QLabel(self.groupBox_17)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_58.addWidget(self.label_106, 2, 0, 1, 1)

        self.label_107 = QLabel(self.groupBox_17)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_58.addWidget(self.label_107, 3, 2, 1, 1)

        self.label_108 = QLabel(self.groupBox_17)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_58.addWidget(self.label_108, 2, 2, 1, 1)

        self.comboBox_11 = QComboBox(self.groupBox_17)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_58.addWidget(self.comboBox_11, 0, 1, 1, 1)

        self.comboBox_12 = QComboBox(self.groupBox_17)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout_58.addWidget(self.comboBox_12, 2, 1, 1, 1)


        self.gridLayout_57.addWidget(self.groupBox_17, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_59 = QGridLayout(self.tab_10)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.groupBox_10 = QGroupBox(self.tab_10)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_60 = QGridLayout(self.groupBox_10)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.label_109 = QLabel(self.groupBox_10)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_60.addWidget(self.label_109, 1, 0, 1, 1)

        self.doubleSpinBox_25 = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_25.setObjectName(u"doubleSpinBox_25")

        self.gridLayout_60.addWidget(self.doubleSpinBox_25, 0, 1, 1, 1)

        self.label_110 = QLabel(self.groupBox_10)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_60.addWidget(self.label_110, 0, 0, 1, 1)

        self.doubleSpinBox_26 = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_26.setObjectName(u"doubleSpinBox_26")

        self.gridLayout_60.addWidget(self.doubleSpinBox_26, 1, 1, 1, 1)

        self.label_111 = QLabel(self.groupBox_10)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_60.addWidget(self.label_111, 0, 2, 1, 1)

        self.label_112 = QLabel(self.groupBox_10)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_60.addWidget(self.label_112, 1, 2, 1, 1)


        self.gridLayout_59.addWidget(self.groupBox_10, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_10, "")

        self.gridLayout_56.addWidget(self.tabWidget_3, 1, 0, 1, 5)

        self.groupBox_20 = QGroupBox(self.channel1_settings_4)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_61 = QGridLayout(self.groupBox_20)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.doubleSpinBox_28 = QDoubleSpinBox(self.groupBox_20)
        self.doubleSpinBox_28.setObjectName(u"doubleSpinBox_28")

        self.gridLayout_61.addWidget(self.doubleSpinBox_28, 3, 1, 1, 1)

        self.label_116 = QLabel(self.groupBox_20)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_61.addWidget(self.label_116, 5, 0, 1, 1)

        self.label_117 = QLabel(self.groupBox_20)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_61.addWidget(self.label_117, 3, 0, 1, 1)

        self.radioButton_25 = QRadioButton(self.groupBox_20)
        self.radioButton_25.setObjectName(u"radioButton_25")

        self.gridLayout_61.addWidget(self.radioButton_25, 5, 2, 1, 1)

        self.radioButton_26 = QRadioButton(self.groupBox_20)
        self.radioButton_26.setObjectName(u"radioButton_26")

        self.gridLayout_61.addWidget(self.radioButton_26, 5, 1, 1, 1)

        self.label_118 = QLabel(self.groupBox_20)
        self.label_118.setObjectName(u"label_118")

        self.gridLayout_61.addWidget(self.label_118, 6, 0, 1, 1)

        self.doubleSpinBox_29 = QDoubleSpinBox(self.groupBox_20)
        self.doubleSpinBox_29.setObjectName(u"doubleSpinBox_29")

        self.gridLayout_61.addWidget(self.doubleSpinBox_29, 6, 1, 1, 1)

        self.label_119 = QLabel(self.groupBox_20)
        self.label_119.setObjectName(u"label_119")

        self.gridLayout_61.addWidget(self.label_119, 3, 2, 1, 1)


        self.gridLayout_56.addWidget(self.groupBox_20, 7, 0, 1, 5)

        self.label_120 = QLabel(self.channel1_settings_4)
        self.label_120.setObjectName(u"label_120")

        self.gridLayout_56.addWidget(self.label_120, 8, 0, 1, 1)

        self.label_121 = QLabel(self.channel1_settings_4)
        self.label_121.setObjectName(u"label_121")

        self.gridLayout_56.addWidget(self.label_121, 3, 3, 1, 1)

        self.state_widget_7 = QWidget(self.channel1_settings_4)
        self.state_widget_7.setObjectName(u"state_widget_7")
        self.gridLayout_62 = QGridLayout(self.state_widget_7)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.ch1_on_7 = QRadioButton(self.state_widget_7)
        self.ch1_on_7.setObjectName(u"ch1_on_7")

        self.gridLayout_62.addWidget(self.ch1_on_7, 0, 1, 1, 1)

        self.ch1_off_7 = QRadioButton(self.state_widget_7)
        self.ch1_off_7.setObjectName(u"ch1_off_7")

        self.gridLayout_62.addWidget(self.ch1_off_7, 0, 2, 1, 1)

        self.label_96 = QLabel(self.state_widget_7)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_62.addWidget(self.label_96, 0, 0, 1, 1)


        self.gridLayout_56.addWidget(self.state_widget_7, 0, 0, 1, 3)

        self.state_widget_8 = QWidget(self.channel1_settings_4)
        self.state_widget_8.setObjectName(u"state_widget_8")
        self.gridLayout_63 = QGridLayout(self.state_widget_8)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.ch1_off_8 = QRadioButton(self.state_widget_8)
        self.ch1_off_8.setObjectName(u"ch1_off_8")

        self.gridLayout_63.addWidget(self.ch1_off_8, 0, 2, 1, 1)

        self.ch1_on_8 = QRadioButton(self.state_widget_8)
        self.ch1_on_8.setObjectName(u"ch1_on_8")

        self.gridLayout_63.addWidget(self.ch1_on_8, 0, 1, 1, 1)

        self.label_115 = QLabel(self.state_widget_8)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout_63.addWidget(self.label_115, 0, 0, 1, 1)


        self.gridLayout_56.addWidget(self.state_widget_8, 5, 0, 1, 4)


        self.gridLayout_74.addWidget(self.channel1_settings_4, 0, 0, 1, 1)

        self.channel1_settings_5 = QGroupBox(self.groupBox_3)
        self.channel1_settings_5.setObjectName(u"channel1_settings_5")
        self.gridLayout_65 = QGridLayout(self.channel1_settings_5)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.widget_13 = QWidget(self.channel1_settings_5)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_66 = QGridLayout(self.widget_13)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.radioButton_29 = QRadioButton(self.widget_13)
        self.radioButton_29.setObjectName(u"radioButton_29")

        self.gridLayout_66.addWidget(self.radioButton_29, 0, 0, 1, 1)

        self.radioButton_30 = QRadioButton(self.widget_13)
        self.radioButton_30.setObjectName(u"radioButton_30")

        self.gridLayout_66.addWidget(self.radioButton_30, 0, 1, 1, 1)


        self.gridLayout_65.addWidget(self.widget_13, 8, 1, 1, 4)

        self.comboBox_14 = QComboBox(self.channel1_settings_5)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.gridLayout_65.addWidget(self.comboBox_14, 2, 2, 1, 1)

        self.label_122 = QLabel(self.channel1_settings_5)
        self.label_122.setObjectName(u"label_122")

        self.gridLayout_65.addWidget(self.label_122, 3, 0, 1, 1)

        self.doubleSpinBox_30 = QDoubleSpinBox(self.channel1_settings_5)
        self.doubleSpinBox_30.setObjectName(u"doubleSpinBox_30")

        self.gridLayout_65.addWidget(self.doubleSpinBox_30, 3, 2, 1, 1)

        self.label_123 = QLabel(self.channel1_settings_5)
        self.label_123.setObjectName(u"label_123")

        self.gridLayout_65.addWidget(self.label_123, 2, 0, 1, 1)

        self.tabWidget_5 = QTabWidget(self.channel1_settings_5)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setMinimumSize(QSize(0, 0))
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_67 = QGridLayout(self.tab_11)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.groupBox_21 = QGroupBox(self.tab_11)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_68 = QGridLayout(self.groupBox_21)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.doubleSpinBox_31 = QDoubleSpinBox(self.groupBox_21)
        self.doubleSpinBox_31.setObjectName(u"doubleSpinBox_31")
        self.doubleSpinBox_31.setMinimum(0.000000000000000)
        self.doubleSpinBox_31.setMaximum(50.000000000000000)

        self.gridLayout_68.addWidget(self.doubleSpinBox_31, 3, 1, 1, 1)

        self.label_124 = QLabel(self.groupBox_21)
        self.label_124.setObjectName(u"label_124")

        self.gridLayout_68.addWidget(self.label_124, 0, 0, 1, 1)

        self.label_125 = QLabel(self.groupBox_21)
        self.label_125.setObjectName(u"label_125")

        self.gridLayout_68.addWidget(self.label_125, 3, 0, 1, 1)

        self.label_126 = QLabel(self.groupBox_21)
        self.label_126.setObjectName(u"label_126")

        self.gridLayout_68.addWidget(self.label_126, 0, 2, 1, 1)

        self.label_127 = QLabel(self.groupBox_21)
        self.label_127.setObjectName(u"label_127")

        self.gridLayout_68.addWidget(self.label_127, 2, 0, 1, 1)

        self.label_128 = QLabel(self.groupBox_21)
        self.label_128.setObjectName(u"label_128")

        self.gridLayout_68.addWidget(self.label_128, 3, 2, 1, 1)

        self.label_129 = QLabel(self.groupBox_21)
        self.label_129.setObjectName(u"label_129")

        self.gridLayout_68.addWidget(self.label_129, 2, 2, 1, 1)

        self.comboBox_15 = QComboBox(self.groupBox_21)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.gridLayout_68.addWidget(self.comboBox_15, 0, 1, 1, 1)

        self.comboBox_16 = QComboBox(self.groupBox_21)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.gridLayout_68.addWidget(self.comboBox_16, 2, 1, 1, 1)


        self.gridLayout_67.addWidget(self.groupBox_21, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_69 = QGridLayout(self.tab_12)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.groupBox_12 = QGroupBox(self.tab_12)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_70 = QGridLayout(self.groupBox_12)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.label_130 = QLabel(self.groupBox_12)
        self.label_130.setObjectName(u"label_130")

        self.gridLayout_70.addWidget(self.label_130, 1, 0, 1, 1)

        self.doubleSpinBox_32 = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_32.setObjectName(u"doubleSpinBox_32")

        self.gridLayout_70.addWidget(self.doubleSpinBox_32, 0, 1, 1, 1)

        self.label_131 = QLabel(self.groupBox_12)
        self.label_131.setObjectName(u"label_131")

        self.gridLayout_70.addWidget(self.label_131, 0, 0, 1, 1)

        self.doubleSpinBox_33 = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_33.setObjectName(u"doubleSpinBox_33")

        self.gridLayout_70.addWidget(self.doubleSpinBox_33, 1, 1, 1, 1)

        self.label_132 = QLabel(self.groupBox_12)
        self.label_132.setObjectName(u"label_132")

        self.gridLayout_70.addWidget(self.label_132, 0, 2, 1, 1)

        self.label_133 = QLabel(self.groupBox_12)
        self.label_133.setObjectName(u"label_133")

        self.gridLayout_70.addWidget(self.label_133, 1, 2, 1, 1)


        self.gridLayout_69.addWidget(self.groupBox_12, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_12, "")

        self.gridLayout_65.addWidget(self.tabWidget_5, 1, 0, 1, 5)

        self.groupBox_24 = QGroupBox(self.channel1_settings_5)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.gridLayout_71 = QGridLayout(self.groupBox_24)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.doubleSpinBox_34 = QDoubleSpinBox(self.groupBox_24)
        self.doubleSpinBox_34.setObjectName(u"doubleSpinBox_34")

        self.gridLayout_71.addWidget(self.doubleSpinBox_34, 3, 1, 1, 1)

        self.label_135 = QLabel(self.groupBox_24)
        self.label_135.setObjectName(u"label_135")

        self.gridLayout_71.addWidget(self.label_135, 5, 0, 1, 1)

        self.label_136 = QLabel(self.groupBox_24)
        self.label_136.setObjectName(u"label_136")

        self.gridLayout_71.addWidget(self.label_136, 3, 0, 1, 1)

        self.radioButton_31 = QRadioButton(self.groupBox_24)
        self.radioButton_31.setObjectName(u"radioButton_31")

        self.gridLayout_71.addWidget(self.radioButton_31, 5, 2, 1, 1)

        self.radioButton_32 = QRadioButton(self.groupBox_24)
        self.radioButton_32.setObjectName(u"radioButton_32")

        self.gridLayout_71.addWidget(self.radioButton_32, 5, 1, 1, 1)

        self.label_137 = QLabel(self.groupBox_24)
        self.label_137.setObjectName(u"label_137")

        self.gridLayout_71.addWidget(self.label_137, 6, 0, 1, 1)

        self.doubleSpinBox_35 = QDoubleSpinBox(self.groupBox_24)
        self.doubleSpinBox_35.setObjectName(u"doubleSpinBox_35")

        self.gridLayout_71.addWidget(self.doubleSpinBox_35, 6, 1, 1, 1)

        self.label_138 = QLabel(self.groupBox_24)
        self.label_138.setObjectName(u"label_138")

        self.gridLayout_71.addWidget(self.label_138, 3, 2, 1, 1)


        self.gridLayout_65.addWidget(self.groupBox_24, 7, 0, 1, 5)

        self.label_139 = QLabel(self.channel1_settings_5)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_65.addWidget(self.label_139, 8, 0, 1, 1)

        self.label_140 = QLabel(self.channel1_settings_5)
        self.label_140.setObjectName(u"label_140")

        self.gridLayout_65.addWidget(self.label_140, 3, 3, 1, 1)

        self.state_widget_10 = QWidget(self.channel1_settings_5)
        self.state_widget_10.setObjectName(u"state_widget_10")
        self.gridLayout_73 = QGridLayout(self.state_widget_10)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.ch1_on_10 = QRadioButton(self.state_widget_10)
        self.ch1_on_10.setObjectName(u"ch1_on_10")

        self.gridLayout_73.addWidget(self.ch1_on_10, 0, 2, 1, 1)

        self.ch1_off_10 = QRadioButton(self.state_widget_10)
        self.ch1_off_10.setObjectName(u"ch1_off_10")

        self.gridLayout_73.addWidget(self.ch1_off_10, 0, 3, 1, 1)

        self.label_101 = QLabel(self.state_widget_10)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_73.addWidget(self.label_101, 0, 1, 1, 1)


        self.gridLayout_65.addWidget(self.state_widget_10, 0, 0, 1, 3)

        self.state_widget_9 = QWidget(self.channel1_settings_5)
        self.state_widget_9.setObjectName(u"state_widget_9")
        self.gridLayout_72 = QGridLayout(self.state_widget_9)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.label_134 = QLabel(self.state_widget_9)
        self.label_134.setObjectName(u"label_134")

        self.gridLayout_72.addWidget(self.label_134, 0, 0, 1, 1)

        self.ch1_on_9 = QRadioButton(self.state_widget_9)
        self.ch1_on_9.setObjectName(u"ch1_on_9")

        self.gridLayout_72.addWidget(self.ch1_on_9, 0, 1, 1, 1)

        self.ch1_off_9 = QRadioButton(self.state_widget_9)
        self.ch1_off_9.setObjectName(u"ch1_off_9")

        self.gridLayout_72.addWidget(self.ch1_off_9, 0, 2, 1, 1)


        self.gridLayout_65.addWidget(self.state_widget_9, 5, 0, 1, 4)


        self.gridLayout_74.addWidget(self.channel1_settings_5, 0, 1, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_3, 3, 0, 1, 1)


        self.gridLayout_55.addWidget(self.BurstModeSettings, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_13.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.modeSelektor.addTab(self.BurstMode, "")

        self.gridLayout.addWidget(self.modeSelektor, 1, 0, 1, 2)

        self.system_status = QGroupBox(Controller_Main)
        self.system_status.setObjectName(u"system_status")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.system_status.sizePolicy().hasHeightForWidth())
        self.system_status.setSizePolicy(sizePolicy3)
        self.system_status.setMinimumSize(QSize(0, 400))
        self.system_status.setMaximumSize(QSize(2000, 400))
        self.gridLayout_29 = QGridLayout(self.system_status)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.d188_ch = QGroupBox(self.system_status)
        self.d188_ch.setObjectName(u"d188_ch")
        self.d188_ch.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.d188_ch.sizePolicy().hasHeightForWidth())
        self.d188_ch.setSizePolicy(sizePolicy4)
        self.d188_ch.setMinimumSize(QSize(0, 50))
        self.d188_ch.setMaximumSize(QSize(16777215, 50))
        self.d188_ch.setBaseSize(QSize(0, 100))
        self.gridLayout_30 = QGridLayout(self.d188_ch)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.textBrowser_10 = QTextBrowser(self.d188_ch)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        sizePolicy4.setHeightForWidth(self.textBrowser_10.sizePolicy().hasHeightForWidth())
        self.textBrowser_10.setSizePolicy(sizePolicy4)
        self.textBrowser_10.setMaximumSize(QSize(50, 40))

        self.gridLayout_30.addWidget(self.textBrowser_10, 0, 1, 1, 1)

        self.label_28 = QLabel(self.d188_ch)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_30.addWidget(self.label_28, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.d188_ch, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.system_status)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_4 = QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.channel1_settings_2 = QGroupBox(self.groupBox_8)
        self.channel1_settings_2.setObjectName(u"channel1_settings_2")
        self.channel1_settings_2.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.channel1_settings_2.sizePolicy().hasHeightForWidth())
        self.channel1_settings_2.setSizePolicy(sizePolicy5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textBrowser_7.sizePolicy().hasHeightForWidth())
        self.textBrowser_7.setSizePolicy(sizePolicy6)

        self.gridLayout_28.addWidget(self.textBrowser_7, 0, 5, 1, 1)

        self.OutputMode_display_8 = QTextBrowser(self.widget_6)
        self.OutputMode_display_8.setObjectName(u"OutputMode_display_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.OutputMode_display_8.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_8.setSizePolicy(sizePolicy7)

        self.gridLayout_28.addWidget(self.OutputMode_display_8, 1, 5, 1, 2)

        self.OutputMode_display_5 = QTextBrowser(self.widget_6)
        self.OutputMode_display_5.setObjectName(u"OutputMode_display_5")
        sizePolicy6.setHeightForWidth(self.OutputMode_display_5.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_5.setSizePolicy(sizePolicy6)

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
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy8)

        self.gridLayout_28.addWidget(self.label_24, 2, 0, 2, 2)

        self.label_71 = QLabel(self.widget_6)
        self.label_71.setObjectName(u"label_71")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy9)
        self.label_71.setMinimumSize(QSize(100, 0))
        self.label_71.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_28.addWidget(self.label_71, 1, 4, 1, 1)

        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy10)
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
        self.channel1_settings = QGroupBox(self.groupBox_7)
        self.channel1_settings.setObjectName(u"channel1_settings")
        self.channel1_settings.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.channel1_settings.sizePolicy().hasHeightForWidth())
        self.channel1_settings.setSizePolicy(sizePolicy5)
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
        sizePolicy6.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy6)

        self.gridLayout_26.addWidget(self.textBrowser, 0, 5, 1, 1)

        self.OutputMode_display_6 = QTextBrowser(self.widget_4)
        self.OutputMode_display_6.setObjectName(u"OutputMode_display_6")
        sizePolicy7.setHeightForWidth(self.OutputMode_display_6.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_6.setSizePolicy(sizePolicy7)

        self.gridLayout_26.addWidget(self.OutputMode_display_6, 1, 5, 1, 2)

        self.OutputMode_display_3 = QTextBrowser(self.widget_4)
        self.OutputMode_display_3.setObjectName(u"OutputMode_display_3")
        sizePolicy6.setHeightForWidth(self.OutputMode_display_3.sizePolicy().hasHeightForWidth())
        self.OutputMode_display_3.setSizePolicy(sizePolicy6)

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
        sizePolicy8.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy8)

        self.gridLayout_26.addWidget(self.label_4, 2, 0, 2, 2)

        self.label_53 = QLabel(self.widget_4)
        self.label_53.setObjectName(u"label_53")
        sizePolicy9.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy9)
        self.label_53.setMinimumSize(QSize(100, 0))
        self.label_53.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_26.addWidget(self.label_53, 1, 4, 1, 1)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        sizePolicy10.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy10)
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

        self.graphicsView = QGraphicsView(self.groupBox_7)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_7, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.system_status, 0, 0, 1, 2)


        self.retranslateUi(Controller_Main)

        self.modeSelektor.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Controller_Main)
    # setupUi

    def retranslateUi(self, Controller_Main):
        Controller_Main.setWindowTitle(QCoreApplication.translate("Controller_Main", u"Stimulation Control", None))
#if QT_CONFIG(tooltip)
        self.ContinuousMode.setToolTip(QCoreApplication.translate("Controller_Main", u"<html><head/><body><p>Continuous Mode</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Controller_Main", u"Channel Settings", None))
        self.channel2_settings.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2", None))
        self.label_49.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_64.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.label_62.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.label_48.setText(QCoreApplication.translate("Controller_Main", u"On/Off", None))
        self.ch1_off_4.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.ch1_on_4.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.ch1_on_3.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.ch1_off_3.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
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
        self.label_70.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_52.setText(QCoreApplication.translate("Controller_Main", u"Hertz", None))
        self.label_69.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.label_65.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_66.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_17.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_18.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_67.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_68.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_63.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.radioButton_19.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.radioButton_20.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.channel1_settings_3.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
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
        self.pushButton.setText(QCoreApplication.translate("Controller_Main", u"Apply", None))
        self.pushButton_2.setText(QCoreApplication.translate("Controller_Main", u"Reset", None))
        self.modeSelektor.setTabText(self.modeSelektor.indexOf(self.ContinuousMode), QCoreApplication.translate("Controller_Main", u"Continuous Mode", None))
        self.pushButton_3.setText(QCoreApplication.translate("Controller_Main", u"Reset", None))
        self.pushButton_4.setText(QCoreApplication.translate("Controller_Main", u"Start", None))
        self.BurstModeSettings.setTitle("")
        self.groupBox_11.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2 Delay Settings", None))
        self.label_95.setText(QCoreApplication.translate("Controller_Main", u"Milliseconds", None))
        self.label_100.setText(QCoreApplication.translate("Controller_Main", u"Seconds", None))
        self.label_99.setText(QCoreApplication.translate("Controller_Main", u"Jitter Rate (+/-)", None))
        self.jitter_on_2.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.jitter_label_2.setText(QCoreApplication.translate("Controller_Main", u"Jitter", None))
        self.jitter_off_2.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_88.setText(QCoreApplication.translate("Controller_Main", u"Channel 2 Delay", None))
        self.radioButton_5.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.label_21.setText(QCoreApplication.translate("Controller_Main", u"Channel 2 State", None))
        self.radioButton_6.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.PulseSettings.setTitle(QCoreApplication.translate("Controller_Main", u"Pulse Settings", None))
        self.label_89.setText(QCoreApplication.translate("Controller_Main", u"Frequency/Period", None))
        self.radioButton_2.setText(QCoreApplication.translate("Controller_Main", u"Period", None))
        self.label_90.setText(QCoreApplication.translate("Controller_Main", u"Milliseconds", None))
        self.label_29.setText(QCoreApplication.translate("Controller_Main", u"Interpulse Delay", None))
        self.radioButton.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_3.setText(QCoreApplication.translate("Controller_Main", u"Pulses per Stim", None))
        self.StimSettings.setTitle(QCoreApplication.translate("Controller_Main", u"Stim Settings", None))
        self.interstim_delay_2.setText(QCoreApplication.translate("Controller_Main", u"Interstim Delay", None))
        self.num_stims_label.setText(QCoreApplication.translate("Controller_Main", u"Number of Stims", None))
        self.freq_select_stim.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_91.setText(QCoreApplication.translate("Controller_Main", u"Frequency/Period", None))
        self.radioButton_4.setText(QCoreApplication.translate("Controller_Main", u"Period", None))
        self.label_92.setText(QCoreApplication.translate("Controller_Main", u"Seconds", None))
        self.label_97.setText(QCoreApplication.translate("Controller_Main", u"Jitter Rate (+/-)", None))
        self.label_98.setText(QCoreApplication.translate("Controller_Main", u"Seconds", None))
        self.jitter_on.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.jitter_label.setText(QCoreApplication.translate("Controller_Main", u"Jitter", None))
        self.jitter_off.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Controller_Main", u"Waveform Settings", None))
        self.channel1_settings_4.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
        self.radioButton_27.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.radioButton_28.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.label_114.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_113.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.groupBox_17.setTitle("")
        self.label_103.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.label_104.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_105.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_106.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_107.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.label_108.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("Controller_Main", u"1", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("Controller_Main", u"5", None))
        self.comboBox_11.setItemText(3, QCoreApplication.translate("Controller_Main", u"10", None))

        self.comboBox_12.setItemText(0, QCoreApplication.translate("Controller_Main", u"10", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("Controller_Main", u"25", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("Controller_Main", u"50", None))

        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("Controller_Main", u"DS5 Control", None))
        self.groupBox_10.setTitle("")
        self.label_109.setText(QCoreApplication.translate("Controller_Main", u"Voltage High", None))
        self.label_110.setText(QCoreApplication.translate("Controller_Main", u"Voltage Low", None))
        self.label_111.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_112.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("Controller_Main", u"FuncGen Control", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.label_116.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_117.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_25.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_26.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_118.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_119.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_120.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.label_121.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.ch1_on_7.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.ch1_off_7.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_96.setText(QCoreApplication.translate("Controller_Main", u"TTL", None))
        self.ch1_off_8.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.ch1_on_8.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_115.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.channel1_settings_5.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2", None))
        self.radioButton_29.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.radioButton_30.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_14.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.label_122.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_123.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.groupBox_21.setTitle("")
        self.label_124.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.label_125.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_126.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_127.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_128.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.label_129.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("Controller_Main", u"1", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.comboBox_15.setItemText(2, QCoreApplication.translate("Controller_Main", u"5", None))
        self.comboBox_15.setItemText(3, QCoreApplication.translate("Controller_Main", u"10", None))

        self.comboBox_16.setItemText(0, QCoreApplication.translate("Controller_Main", u"10", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("Controller_Main", u"25", None))
        self.comboBox_16.setItemText(2, QCoreApplication.translate("Controller_Main", u"50", None))

        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_11), QCoreApplication.translate("Controller_Main", u"DS5 Control", None))
        self.groupBox_12.setTitle("")
        self.label_130.setText(QCoreApplication.translate("Controller_Main", u"Voltage High", None))
        self.label_131.setText(QCoreApplication.translate("Controller_Main", u"Voltage Low", None))
        self.label_132.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_133.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_12), QCoreApplication.translate("Controller_Main", u"FuncGen Control", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.label_135.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_136.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_31.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_32.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_137.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_138.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_139.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.label_140.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.ch1_on_10.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.ch1_off_10.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_101.setText(QCoreApplication.translate("Controller_Main", u"TTL", None))
        self.label_134.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.ch1_on_9.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.ch1_off_9.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.modeSelektor.setTabText(self.modeSelektor.indexOf(self.BurstMode), QCoreApplication.translate("Controller_Main", u"Burst Mode", None))
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
    # retranslateUi

