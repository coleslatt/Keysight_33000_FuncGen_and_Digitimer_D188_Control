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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import Icons_rc

class Ui_Controller_Main(object):
    def setupUi(self, Controller_Main):
        if not Controller_Main.objectName():
            Controller_Main.setObjectName(u"Controller_Main")
        Controller_Main.resize(1100, 998)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Controller_Main.sizePolicy().hasHeightForWidth())
        Controller_Main.setSizePolicy(sizePolicy)
        Controller_Main.setMinimumSize(QSize(1100, 800))
        Controller_Main.setMaximumSize(QSize(1800, 16777215))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        Controller_Main.setFont(font)
        Controller_Main.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        icon = QIcon()
        icon.addFile(u":/Icons/electrode_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Controller_Main.setWindowIcon(icon)
        Controller_Main.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(Controller_Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.system_status = QGroupBox(Controller_Main)
        self.system_status.setObjectName(u"system_status")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.system_status.sizePolicy().hasHeightForWidth())
        self.system_status.setSizePolicy(sizePolicy1)
        self.system_status.setMinimumSize(QSize(0, 400))
        self.system_status.setMaximumSize(QSize(2000, 400))
        self.gridLayout_29 = QGridLayout(self.system_status)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.groupBox_7 = QGroupBox(self.system_status)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_3 = QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.channel1_settings = QGroupBox(self.groupBox_7)
        self.channel1_settings.setObjectName(u"channel1_settings")
        self.channel1_settings.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy3)

        self.gridLayout_26.addWidget(self.textBrowser, 0, 5, 1, 1)

        self.OutputMode_display_6 = QTextBrowser(self.widget_4)
        self.OutputMode_display_6.setObjectName(u"OutputMode_display_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)

        self.gridLayout_26.addWidget(self.label_4, 2, 0, 2, 2)

        self.label_53 = QLabel(self.widget_4)
        self.label_53.setObjectName(u"label_53")
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setMinimumSize(QSize(100, 0))
        self.label_53.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_26.addWidget(self.label_53, 1, 4, 1, 1)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
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

        self.groupBox_8 = QGroupBox(self.system_status)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_4 = QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.channel1_settings_2 = QGroupBox(self.groupBox_8)
        self.channel1_settings_2.setObjectName(u"channel1_settings_2")
        self.channel1_settings_2.setEnabled(True)
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
        sizePolicy3.setHeightForWidth(self.textBrowser_7.sizePolicy().hasHeightForWidth())
        self.textBrowser_7.setSizePolicy(sizePolicy3)

        self.gridLayout_28.addWidget(self.textBrowser_7, 0, 5, 1, 1)

        self.OutputMode_display_8 = QTextBrowser(self.widget_6)
        self.OutputMode_display_8.setObjectName(u"OutputMode_display_8")
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
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)

        self.gridLayout_28.addWidget(self.label_24, 2, 0, 2, 2)

        self.label_71 = QLabel(self.widget_6)
        self.label_71.setObjectName(u"label_71")
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMinimumSize(QSize(100, 0))
        self.label_71.setTextFormat(Qt.TextFormat.MarkdownText)

        self.gridLayout_28.addWidget(self.label_71, 1, 4, 1, 1)

        self.label_25 = QLabel(self.widget_6)
        self.label_25.setObjectName(u"label_25")
        sizePolicy6.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy6)
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

        self.d188_ch = QGroupBox(self.system_status)
        self.d188_ch.setObjectName(u"d188_ch")
        self.d188_ch.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.d188_ch.sizePolicy().hasHeightForWidth())
        self.d188_ch.setSizePolicy(sizePolicy7)
        self.d188_ch.setMinimumSize(QSize(0, 50))
        self.d188_ch.setMaximumSize(QSize(16777215, 50))
        self.d188_ch.setBaseSize(QSize(0, 100))
        self.gridLayout_30 = QGridLayout(self.d188_ch)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.textBrowser_10 = QTextBrowser(self.d188_ch)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        sizePolicy7.setHeightForWidth(self.textBrowser_10.sizePolicy().hasHeightForWidth())
        self.textBrowser_10.setSizePolicy(sizePolicy7)
        self.textBrowser_10.setMaximumSize(QSize(50, 40))

        self.gridLayout_30.addWidget(self.textBrowser_10, 0, 1, 1, 1)

        self.label_28 = QLabel(self.d188_ch)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_30.addWidget(self.label_28, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.d188_ch, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.system_status, 0, 0, 1, 2)

        self.stackedWidget = QStackedWidget(Controller_Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 100))
        self.trial_running_page = QWidget()
        self.trial_running_page.setObjectName(u"trial_running_page")
        self.gridLayout_94 = QGridLayout(self.trial_running_page)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.groupBox_6 = QGroupBox(self.trial_running_page)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_95 = QGridLayout(self.groupBox_6)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_95.addItem(self.horizontalSpacer_10, 9, 1, 1, 1)

        self.condition_label = QLabel(self.groupBox_6)
        self.condition_label.setObjectName(u"condition_label")
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(36)
        self.condition_label.setFont(font1)
        self.condition_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_95.addWidget(self.condition_label, 3, 0, 1, 4)

        self.widget_31 = QWidget(self.groupBox_6)
        self.widget_31.setObjectName(u"widget_31")
        self.gridLayout_96 = QGridLayout(self.widget_31)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_96.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.abprt_button = QPushButton(self.widget_31)
        self.abprt_button.setObjectName(u"abprt_button")

        self.gridLayout_96.addWidget(self.abprt_button, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_96.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)


        self.gridLayout_95.addWidget(self.widget_31, 0, 1, 1, 1)

        self.trial_number = QLabel(self.groupBox_6)
        self.trial_number.setObjectName(u"trial_number")
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(24)
        self.trial_number.setFont(font2)
        self.trial_number.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_95.addWidget(self.trial_number, 5, 0, 1, 4)

        self.increase_intensity = QPushButton(self.groupBox_6)
        self.increase_intensity.setObjectName(u"increase_intensity")

        self.gridLayout_95.addWidget(self.increase_intensity, 9, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_95.addItem(self.verticalSpacer_3, 1, 0, 1, 4)

        self.decrease_intensity = QPushButton(self.groupBox_6)
        self.decrease_intensity.setObjectName(u"decrease_intensity")

        self.gridLayout_95.addWidget(self.decrease_intensity, 9, 0, 1, 1)

        self.previous_config = QPushButton(self.groupBox_6)
        self.previous_config.setObjectName(u"previous_config")

        self.gridLayout_95.addWidget(self.previous_config, 0, 0, 1, 1)

        self.widget_37 = QWidget(self.groupBox_6)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy8)
        self.widget_37.setMinimumSize(QSize(0, 0))
        self.gridLayout_103 = QGridLayout(self.widget_37)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.widget_38 = QWidget(self.widget_37)
        self.widget_38.setObjectName(u"widget_38")
        self.gridLayout_104 = QGridLayout(self.widget_38)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.trial_timer_label = QLabel(self.widget_38)
        self.trial_timer_label.setObjectName(u"trial_timer_label")

        self.gridLayout_104.addWidget(self.trial_timer_label, 0, 0, 1, 1)

        self.totaltime_label = QLabel(self.widget_38)
        self.totaltime_label.setObjectName(u"totaltime_label")

        self.gridLayout_104.addWidget(self.totaltime_label, 1, 0, 1, 1)

        self.trial_timer = QLabel(self.widget_38)
        self.trial_timer.setObjectName(u"trial_timer")

        self.gridLayout_104.addWidget(self.trial_timer, 0, 1, 1, 1)

        self.totaltime_2 = QLabel(self.widget_38)
        self.totaltime_2.setObjectName(u"totaltime_2")

        self.gridLayout_104.addWidget(self.totaltime_2, 1, 1, 1, 1)


        self.gridLayout_103.addWidget(self.widget_38, 0, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_103.addItem(self.horizontalSpacer_18, 0, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_103.addItem(self.horizontalSpacer_19, 0, 2, 1, 1)


        self.gridLayout_95.addWidget(self.widget_37, 6, 0, 1, 4)

        self.widget_35 = QWidget(self.groupBox_6)
        self.widget_35.setObjectName(u"widget_35")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_35.sizePolicy().hasHeightForWidth())
        self.widget_35.setSizePolicy(sizePolicy9)
        self.widget_35.setMinimumSize(QSize(0, 30))
        self.gridLayout_101 = QGridLayout(self.widget_35)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_101.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.widget_36 = QWidget(self.widget_35)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy10)
        self.gridLayout_102 = QGridLayout(self.widget_36)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.radioButton_8 = QRadioButton(self.widget_36)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout_102.addWidget(self.radioButton_8, 0, 1, 1, 1)

        self.radioButton_9 = QRadioButton(self.widget_36)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_102.addWidget(self.radioButton_9, 0, 2, 1, 1)

        self.label_79 = QLabel(self.widget_36)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_102.addWidget(self.label_79, 0, 0, 1, 1)


        self.gridLayout_101.addWidget(self.widget_36, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_101.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)


        self.gridLayout_95.addWidget(self.widget_35, 2, 0, 1, 4)

        self.next_config = QPushButton(self.groupBox_6)
        self.next_config.setObjectName(u"next_config")

        self.gridLayout_95.addWidget(self.next_config, 0, 3, 1, 1)

        self.widget_32 = QWidget(self.groupBox_6)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_97 = QGridLayout(self.widget_32)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_97.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_97.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_97.addItem(self.horizontalSpacer_15, 1, 2, 1, 1)

        self.log_button = QPushButton(self.widget_32)
        self.log_button.setObjectName(u"log_button")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.log_button.sizePolicy().hasHeightForWidth())
        self.log_button.setSizePolicy(sizePolicy11)
        self.log_button.setMinimumSize(QSize(50, 50))

        self.gridLayout_97.addWidget(self.log_button, 3, 1, 1, 1)

        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        self.gridLayout_98 = QGridLayout(self.widget_33)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.label_82 = QLabel(self.widget_33)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_98.addWidget(self.label_82, 0, 2, 1, 1)

        self.int_label = QLabel(self.widget_33)
        self.int_label.setObjectName(u"int_label")

        self.gridLayout_98.addWidget(self.int_label, 0, 0, 1, 1)

        self.current_output = QTextBrowser(self.widget_33)
        self.current_output.setObjectName(u"current_output")
        sizePolicy3.setHeightForWidth(self.current_output.sizePolicy().hasHeightForWidth())
        self.current_output.setSizePolicy(sizePolicy3)
        self.current_output.setMaximumSize(QSize(100, 30))

        self.gridLayout_98.addWidget(self.current_output, 0, 1, 1, 1)

        self.widget_34 = QWidget(self.widget_33)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy10.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy10)
        self.widget_34.setMinimumSize(QSize(0, 50))
        self.gridLayout_106 = QGridLayout(self.widget_34)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.inc_up = QPushButton(self.widget_34)
        self.inc_up.setObjectName(u"inc_up")
        sizePolicy3.setHeightForWidth(self.inc_up.sizePolicy().hasHeightForWidth())
        self.inc_up.setSizePolicy(sizePolicy3)
        self.inc_up.setMaximumSize(QSize(40, 40))

        self.gridLayout_106.addWidget(self.inc_up, 0, 1, 1, 1)

        self.inc_down = QPushButton(self.widget_34)
        self.inc_down.setObjectName(u"inc_down")
        sizePolicy3.setHeightForWidth(self.inc_down.sizePolicy().hasHeightForWidth())
        self.inc_down.setSizePolicy(sizePolicy3)
        self.inc_down.setMaximumSize(QSize(40, 40))

        self.gridLayout_106.addWidget(self.inc_down, 0, 0, 1, 1)


        self.gridLayout_98.addWidget(self.widget_34, 1, 1, 1, 1)


        self.gridLayout_97.addWidget(self.widget_33, 1, 1, 1, 1)


        self.gridLayout_95.addWidget(self.widget_32, 7, 0, 1, 4)


        self.gridLayout_94.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.trial_running_page)
        self.trial_settings_page = QWidget()
        self.trial_settings_page.setObjectName(u"trial_settings_page")
        self.gridLayout_93 = QGridLayout(self.trial_settings_page)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.modeSelektor = QTabWidget(self.trial_settings_page)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1018, 701))
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

        self.groupBox_23 = QGroupBox(self.channel2_settings)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_20 = QGridLayout(self.groupBox_23)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_68 = QLabel(self.groupBox_23)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_20.addWidget(self.label_68, 3, 2, 1, 1)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")

        self.gridLayout_20.addWidget(self.doubleSpinBox_15, 3, 1, 1, 1)

        self.radioButton_18 = QRadioButton(self.groupBox_23)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.gridLayout_20.addWidget(self.radioButton_18, 5, 1, 1, 1)

        self.label_65 = QLabel(self.groupBox_23)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_20.addWidget(self.label_65, 5, 0, 1, 1)

        self.label_67 = QLabel(self.groupBox_23)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_20.addWidget(self.label_67, 6, 0, 1, 1)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.groupBox_23)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")

        self.gridLayout_20.addWidget(self.doubleSpinBox_16, 6, 1, 1, 1)

        self.label_66 = QLabel(self.groupBox_23)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_20.addWidget(self.label_66, 3, 0, 1, 1)

        self.radioButton_17 = QRadioButton(self.groupBox_23)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.gridLayout_20.addWidget(self.radioButton_17, 5, 2, 1, 1)


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


        self.gridLayout_22.addWidget(self.widget_3, 9, 2, 1, 3)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.channel2_settings)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.gridLayout_22.addWidget(self.doubleSpinBox_4, 1, 2, 1, 1)


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


        self.gridLayout_21.addWidget(self.widget_2, 9, 2, 1, 3)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.channel1_settings_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout_21.addWidget(self.doubleSpinBox_2, 1, 2, 1, 1)


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
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy12.setHorizontalStretch(30)
        sizePolicy12.setVerticalStretch(30)
        sizePolicy12.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy12)
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
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(50)
        sizePolicy13.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy13)
        self.widget_15.setMinimumSize(QSize(0, 50))
        self.gridLayout_76 = QGridLayout(self.widget_15)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.pushButton_3 = QPushButton(self.widget_15)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_76.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_15)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_76.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.stop_button = QPushButton(self.widget_15)
        self.stop_button.setObjectName(u"stop_button")

        self.gridLayout_76.addWidget(self.stop_button, 0, 2, 1, 1)


        self.gridLayout_13.addWidget(self.widget_15, 1, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.BurstMode)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy14)
        self.scrollArea_2.setMinimumSize(QSize(1, 0))
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1018, 1185))
        self.gridLayout_55 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.BurstModeSettings = QGroupBox(self.scrollAreaWidgetContents_2)
        self.BurstModeSettings.setObjectName(u"BurstModeSettings")
        self.gridLayout_39 = QGridLayout(self.BurstModeSettings)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.groupBox_11 = QGroupBox(self.BurstModeSettings)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_44 = QGridLayout(self.groupBox_11)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.widget_9 = QWidget(self.groupBox_11)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_45 = QGridLayout(self.widget_9)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_21 = QLabel(self.widget_9)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_45.addWidget(self.label_21, 0, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.widget_9)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_45.addWidget(self.radioButton_6, 0, 2, 1, 1)

        self.radioButton_5 = QRadioButton(self.widget_9)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_45.addWidget(self.radioButton_5, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_9, 0, 0, 1, 1)

        self.ch2_delay_widget = QWidget(self.groupBox_11)
        self.ch2_delay_widget.setObjectName(u"ch2_delay_widget")
        self.gridLayout_48 = QGridLayout(self.ch2_delay_widget)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.ch2_delay_widget)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.gridLayout_48.addWidget(self.doubleSpinBox_3, 0, 1, 1, 1)

        self.label_95 = QLabel(self.ch2_delay_widget)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_48.addWidget(self.label_95, 0, 2, 1, 1)

        self.label_88 = QLabel(self.ch2_delay_widget)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_48.addWidget(self.label_88, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.ch2_delay_widget, 0, 3, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_11, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.BurstModeSettings)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_61 = QGridLayout(self.groupBox_3)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.channel1_settings_burst = QGroupBox(self.groupBox_3)
        self.channel1_settings_burst.setObjectName(u"channel1_settings_burst")
        self.gridLayout_33 = QGridLayout(self.channel1_settings_burst)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.waveform_ch1_burst_2 = QWidget(self.channel1_settings_burst)
        self.waveform_ch1_burst_2.setObjectName(u"waveform_ch1_burst_2")
        self.waveform_ch1_burst_2.setMinimumSize(QSize(0, 550))
        self.gridLayout_36 = QGridLayout(self.waveform_ch1_burst_2)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.current_control_ch1burst = QTabWidget(self.waveform_ch1_burst_2)
        self.current_control_ch1burst.setObjectName(u"current_control_ch1burst")
        self.current_control_ch1burst.setMinimumSize(QSize(0, 0))
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_77 = QGridLayout(self.tab_13)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.groupBox_25 = QGroupBox(self.tab_13)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.gridLayout_78 = QGridLayout(self.groupBox_25)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.doubleSpinBox_36 = QDoubleSpinBox(self.groupBox_25)
        self.doubleSpinBox_36.setObjectName(u"doubleSpinBox_36")
        self.doubleSpinBox_36.setMinimum(0.000000000000000)
        self.doubleSpinBox_36.setMaximum(50.000000000000000)

        self.gridLayout_78.addWidget(self.doubleSpinBox_36, 3, 1, 1, 1)

        self.label_141 = QLabel(self.groupBox_25)
        self.label_141.setObjectName(u"label_141")

        self.gridLayout_78.addWidget(self.label_141, 0, 0, 1, 1)

        self.label_142 = QLabel(self.groupBox_25)
        self.label_142.setObjectName(u"label_142")

        self.gridLayout_78.addWidget(self.label_142, 3, 0, 1, 1)

        self.label_143 = QLabel(self.groupBox_25)
        self.label_143.setObjectName(u"label_143")

        self.gridLayout_78.addWidget(self.label_143, 0, 2, 1, 1)

        self.label_144 = QLabel(self.groupBox_25)
        self.label_144.setObjectName(u"label_144")

        self.gridLayout_78.addWidget(self.label_144, 2, 0, 1, 1)

        self.label_145 = QLabel(self.groupBox_25)
        self.label_145.setObjectName(u"label_145")

        self.gridLayout_78.addWidget(self.label_145, 3, 2, 1, 1)

        self.label_146 = QLabel(self.groupBox_25)
        self.label_146.setObjectName(u"label_146")

        self.gridLayout_78.addWidget(self.label_146, 2, 2, 1, 1)

        self.comboBox_18 = QComboBox(self.groupBox_25)
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.gridLayout_78.addWidget(self.comboBox_18, 2, 1, 1, 1)

        self.comboBox_17 = QComboBox(self.groupBox_25)
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.gridLayout_78.addWidget(self.comboBox_17, 0, 1, 1, 1)


        self.gridLayout_77.addWidget(self.groupBox_25, 0, 0, 1, 1)

        self.current_control_ch1burst.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_79 = QGridLayout(self.tab_14)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.groupBox_13 = QGroupBox(self.tab_14)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_80 = QGridLayout(self.groupBox_13)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.label_147 = QLabel(self.groupBox_13)
        self.label_147.setObjectName(u"label_147")

        self.gridLayout_80.addWidget(self.label_147, 1, 0, 1, 1)

        self.doubleSpinBox_37 = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_37.setObjectName(u"doubleSpinBox_37")

        self.gridLayout_80.addWidget(self.doubleSpinBox_37, 0, 1, 1, 1)

        self.label_148 = QLabel(self.groupBox_13)
        self.label_148.setObjectName(u"label_148")

        self.gridLayout_80.addWidget(self.label_148, 0, 0, 1, 1)

        self.doubleSpinBox_38 = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_38.setObjectName(u"doubleSpinBox_38")

        self.gridLayout_80.addWidget(self.doubleSpinBox_38, 1, 1, 1, 1)

        self.label_149 = QLabel(self.groupBox_13)
        self.label_149.setObjectName(u"label_149")

        self.gridLayout_80.addWidget(self.label_149, 0, 2, 1, 1)

        self.label_150 = QLabel(self.groupBox_13)
        self.label_150.setObjectName(u"label_150")

        self.gridLayout_80.addWidget(self.label_150, 1, 2, 1, 1)


        self.gridLayout_79.addWidget(self.groupBox_13, 0, 0, 1, 1)

        self.current_control_ch1burst.addTab(self.tab_14, "")

        self.gridLayout_36.addWidget(self.current_control_ch1burst, 0, 0, 1, 1)

        self.widget_10 = QWidget(self.waveform_ch1_burst_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 0))
        self.gridLayout_34 = QGridLayout(self.widget_10)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.groupBox_26 = QGroupBox(self.widget_10)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.gridLayout_82 = QGridLayout(self.groupBox_26)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.doubleSpinBox_40 = QDoubleSpinBox(self.groupBox_26)
        self.doubleSpinBox_40.setObjectName(u"doubleSpinBox_40")

        self.gridLayout_82.addWidget(self.doubleSpinBox_40, 3, 1, 1, 1)

        self.label_155 = QLabel(self.groupBox_26)
        self.label_155.setObjectName(u"label_155")

        self.gridLayout_82.addWidget(self.label_155, 5, 0, 1, 1)

        self.label_156 = QLabel(self.groupBox_26)
        self.label_156.setObjectName(u"label_156")

        self.gridLayout_82.addWidget(self.label_156, 3, 0, 1, 1)

        self.radioButton_33 = QRadioButton(self.groupBox_26)
        self.radioButton_33.setObjectName(u"radioButton_33")

        self.gridLayout_82.addWidget(self.radioButton_33, 5, 2, 1, 1)

        self.radioButton_34 = QRadioButton(self.groupBox_26)
        self.radioButton_34.setObjectName(u"radioButton_34")

        self.gridLayout_82.addWidget(self.radioButton_34, 5, 1, 1, 1)

        self.label_157 = QLabel(self.groupBox_26)
        self.label_157.setObjectName(u"label_157")

        self.gridLayout_82.addWidget(self.label_157, 6, 0, 1, 1)

        self.doubleSpinBox_41 = QDoubleSpinBox(self.groupBox_26)
        self.doubleSpinBox_41.setObjectName(u"doubleSpinBox_41")

        self.gridLayout_82.addWidget(self.doubleSpinBox_41, 6, 1, 1, 1)

        self.label_158 = QLabel(self.groupBox_26)
        self.label_158.setObjectName(u"label_158")

        self.gridLayout_82.addWidget(self.label_158, 3, 2, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_26, 0, 0, 1, 1)


        self.gridLayout_36.addWidget(self.widget_10, 4, 0, 1, 1)

        self.widget_5 = QWidget(self.waveform_ch1_burst_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.gridLayout_31 = QGridLayout(self.widget_5)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_152 = QLabel(self.widget_5)
        self.label_152.setObjectName(u"label_152")

        self.gridLayout_31.addWidget(self.label_152, 0, 0, 1, 1)

        self.doubleSpinBox_39 = QDoubleSpinBox(self.widget_5)
        self.doubleSpinBox_39.setObjectName(u"doubleSpinBox_39")

        self.gridLayout_31.addWidget(self.doubleSpinBox_39, 0, 1, 1, 1)

        self.label_153 = QLabel(self.widget_5)
        self.label_153.setObjectName(u"label_153")

        self.gridLayout_31.addWidget(self.label_153, 0, 2, 1, 1)


        self.gridLayout_36.addWidget(self.widget_5, 2, 0, 1, 1)

        self.widget_16 = QWidget(self.waveform_ch1_burst_2)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 0))
        self.gridLayout_27 = QGridLayout(self.widget_16)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_151 = QLabel(self.widget_16)
        self.label_151.setObjectName(u"label_151")

        self.gridLayout_27.addWidget(self.label_151, 0, 0, 1, 1)

        self.comboBox_19 = QComboBox(self.widget_16)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.gridLayout_27.addWidget(self.comboBox_19, 0, 1, 1, 1)

        self.widget_19 = QWidget(self.widget_16)
        self.widget_19.setObjectName(u"widget_19")

        self.gridLayout_27.addWidget(self.widget_19, 0, 2, 1, 1)


        self.gridLayout_36.addWidget(self.widget_16, 1, 0, 1, 1)

        self.widget_17 = QWidget(self.waveform_ch1_burst_2)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 0))
        self.gridLayout_32 = QGridLayout(self.widget_17)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.state_widget_11 = QWidget(self.widget_17)
        self.state_widget_11.setObjectName(u"state_widget_11")
        self.gridLayout_81 = QGridLayout(self.state_widget_11)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.ch1_off_11 = QRadioButton(self.state_widget_11)
        self.ch1_off_11.setObjectName(u"ch1_off_11")

        self.gridLayout_81.addWidget(self.ch1_off_11, 0, 2, 1, 1)

        self.ch1_on_11 = QRadioButton(self.state_widget_11)
        self.ch1_on_11.setObjectName(u"ch1_on_11")

        self.gridLayout_81.addWidget(self.ch1_on_11, 0, 1, 1, 1)

        self.label_154 = QLabel(self.state_widget_11)
        self.label_154.setObjectName(u"label_154")

        self.gridLayout_81.addWidget(self.label_154, 0, 0, 1, 1)


        self.gridLayout_32.addWidget(self.state_widget_11, 0, 0, 1, 1)


        self.gridLayout_36.addWidget(self.widget_17, 3, 0, 1, 1)

        self.widget_18 = QWidget(self.waveform_ch1_burst_2)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 0))
        self.gridLayout_35 = QGridLayout(self.widget_18)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.radioButton_36 = QRadioButton(self.widget_18)
        self.radioButton_36.setObjectName(u"radioButton_36")

        self.gridLayout_35.addWidget(self.radioButton_36, 0, 2, 1, 1)

        self.label_159 = QLabel(self.widget_18)
        self.label_159.setObjectName(u"label_159")

        self.gridLayout_35.addWidget(self.label_159, 0, 0, 1, 1)

        self.radioButton_35 = QRadioButton(self.widget_18)
        self.radioButton_35.setObjectName(u"radioButton_35")

        self.gridLayout_35.addWidget(self.radioButton_35, 0, 1, 1, 1)


        self.gridLayout_36.addWidget(self.widget_18, 5, 0, 1, 1)


        self.gridLayout_33.addWidget(self.waveform_ch1_burst_2, 3, 0, 1, 2)

        self.ttl_ch1_1 = QWidget(self.channel1_settings_burst)
        self.ttl_ch1_1.setObjectName(u"ttl_ch1_1")
        self.gridLayout_62 = QGridLayout(self.ttl_ch1_1)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.label_96 = QLabel(self.ttl_ch1_1)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_62.addWidget(self.label_96, 0, 0, 1, 1)

        self.ch1_on_7 = QRadioButton(self.ttl_ch1_1)
        self.ch1_on_7.setObjectName(u"ch1_on_7")

        self.gridLayout_62.addWidget(self.ch1_on_7, 0, 1, 1, 1)

        self.ch1_off_7 = QRadioButton(self.ttl_ch1_1)
        self.ch1_off_7.setObjectName(u"ch1_off_7")

        self.gridLayout_62.addWidget(self.ch1_off_7, 0, 2, 1, 1)


        self.gridLayout_33.addWidget(self.ttl_ch1_1, 0, 0, 2, 2)


        self.gridLayout_61.addWidget(self.channel1_settings_burst, 0, 0, 1, 1)

        self.channel2_settings_burst_2 = QGroupBox(self.groupBox_3)
        self.channel2_settings_burst_2.setObjectName(u"channel2_settings_burst_2")
        self.gridLayout_37 = QGridLayout(self.channel2_settings_burst_2)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.waveform_ch2_burst = QWidget(self.channel2_settings_burst_2)
        self.waveform_ch2_burst.setObjectName(u"waveform_ch2_burst")
        self.waveform_ch2_burst.setMinimumSize(QSize(0, 550))
        self.gridLayout_38 = QGridLayout(self.waveform_ch2_burst)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.current_control_ch2burst = QTabWidget(self.waveform_ch2_burst)
        self.current_control_ch2burst.setObjectName(u"current_control_ch2burst")
        self.current_control_ch2burst.setMinimumSize(QSize(0, 0))
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_83 = QGridLayout(self.tab_15)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.groupBox_27 = QGroupBox(self.tab_15)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.gridLayout_84 = QGridLayout(self.groupBox_27)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.label_163 = QLabel(self.groupBox_27)
        self.label_163.setObjectName(u"label_163")

        self.gridLayout_84.addWidget(self.label_163, 2, 0, 1, 1)

        self.doubleSpinBox_42 = QDoubleSpinBox(self.groupBox_27)
        self.doubleSpinBox_42.setObjectName(u"doubleSpinBox_42")
        self.doubleSpinBox_42.setMinimum(0.000000000000000)
        self.doubleSpinBox_42.setMaximum(50.000000000000000)

        self.gridLayout_84.addWidget(self.doubleSpinBox_42, 3, 1, 1, 1)

        self.label_161 = QLabel(self.groupBox_27)
        self.label_161.setObjectName(u"label_161")

        self.gridLayout_84.addWidget(self.label_161, 3, 0, 1, 1)

        self.label_165 = QLabel(self.groupBox_27)
        self.label_165.setObjectName(u"label_165")

        self.gridLayout_84.addWidget(self.label_165, 2, 2, 1, 1)

        self.label_160 = QLabel(self.groupBox_27)
        self.label_160.setObjectName(u"label_160")

        self.gridLayout_84.addWidget(self.label_160, 0, 0, 1, 1)

        self.comboBox_21 = QComboBox(self.groupBox_27)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.gridLayout_84.addWidget(self.comboBox_21, 2, 1, 1, 1)

        self.label_164 = QLabel(self.groupBox_27)
        self.label_164.setObjectName(u"label_164")

        self.gridLayout_84.addWidget(self.label_164, 3, 2, 1, 1)

        self.comboBox_20 = QComboBox(self.groupBox_27)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.gridLayout_84.addWidget(self.comboBox_20, 0, 1, 1, 1)

        self.label_162 = QLabel(self.groupBox_27)
        self.label_162.setObjectName(u"label_162")

        self.gridLayout_84.addWidget(self.label_162, 0, 2, 1, 1)


        self.gridLayout_83.addWidget(self.groupBox_27, 0, 0, 1, 1)

        self.current_control_ch2burst.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_85 = QGridLayout(self.tab_16)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.groupBox_14 = QGroupBox(self.tab_16)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_86 = QGridLayout(self.groupBox_14)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.label_166 = QLabel(self.groupBox_14)
        self.label_166.setObjectName(u"label_166")

        self.gridLayout_86.addWidget(self.label_166, 1, 0, 1, 1)

        self.doubleSpinBox_43 = QDoubleSpinBox(self.groupBox_14)
        self.doubleSpinBox_43.setObjectName(u"doubleSpinBox_43")

        self.gridLayout_86.addWidget(self.doubleSpinBox_43, 0, 1, 1, 1)

        self.label_167 = QLabel(self.groupBox_14)
        self.label_167.setObjectName(u"label_167")

        self.gridLayout_86.addWidget(self.label_167, 0, 0, 1, 1)

        self.doubleSpinBox_44 = QDoubleSpinBox(self.groupBox_14)
        self.doubleSpinBox_44.setObjectName(u"doubleSpinBox_44")

        self.gridLayout_86.addWidget(self.doubleSpinBox_44, 1, 1, 1, 1)

        self.label_168 = QLabel(self.groupBox_14)
        self.label_168.setObjectName(u"label_168")

        self.gridLayout_86.addWidget(self.label_168, 0, 2, 1, 1)

        self.label_169 = QLabel(self.groupBox_14)
        self.label_169.setObjectName(u"label_169")

        self.gridLayout_86.addWidget(self.label_169, 1, 2, 1, 1)


        self.gridLayout_85.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.current_control_ch2burst.addTab(self.tab_16, "")

        self.gridLayout_38.addWidget(self.current_control_ch2burst, 0, 0, 1, 1)

        self.widget_13 = QWidget(self.waveform_ch2_burst)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 0))
        self.gridLayout_56 = QGridLayout(self.widget_13)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.groupBox_28 = QGroupBox(self.widget_13)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.gridLayout_87 = QGridLayout(self.groupBox_28)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.doubleSpinBox_45 = QDoubleSpinBox(self.groupBox_28)
        self.doubleSpinBox_45.setObjectName(u"doubleSpinBox_45")

        self.gridLayout_87.addWidget(self.doubleSpinBox_45, 3, 1, 1, 1)

        self.label_170 = QLabel(self.groupBox_28)
        self.label_170.setObjectName(u"label_170")

        self.gridLayout_87.addWidget(self.label_170, 5, 0, 1, 1)

        self.label_171 = QLabel(self.groupBox_28)
        self.label_171.setObjectName(u"label_171")

        self.gridLayout_87.addWidget(self.label_171, 3, 0, 1, 1)

        self.radioButton_37 = QRadioButton(self.groupBox_28)
        self.radioButton_37.setObjectName(u"radioButton_37")

        self.gridLayout_87.addWidget(self.radioButton_37, 5, 2, 1, 1)

        self.radioButton_38 = QRadioButton(self.groupBox_28)
        self.radioButton_38.setObjectName(u"radioButton_38")

        self.gridLayout_87.addWidget(self.radioButton_38, 5, 1, 1, 1)

        self.label_172 = QLabel(self.groupBox_28)
        self.label_172.setObjectName(u"label_172")

        self.gridLayout_87.addWidget(self.label_172, 6, 0, 1, 1)

        self.doubleSpinBox_46 = QDoubleSpinBox(self.groupBox_28)
        self.doubleSpinBox_46.setObjectName(u"doubleSpinBox_46")

        self.gridLayout_87.addWidget(self.doubleSpinBox_46, 6, 1, 1, 1)

        self.label_173 = QLabel(self.groupBox_28)
        self.label_173.setObjectName(u"label_173")

        self.gridLayout_87.addWidget(self.label_173, 3, 2, 1, 1)


        self.gridLayout_56.addWidget(self.groupBox_28, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.widget_13, 4, 0, 1, 1)

        self.widget_20 = QWidget(self.waveform_ch2_burst)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 0))
        self.gridLayout_57 = QGridLayout(self.widget_20)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.label_174 = QLabel(self.widget_20)
        self.label_174.setObjectName(u"label_174")

        self.gridLayout_57.addWidget(self.label_174, 0, 0, 1, 1)

        self.doubleSpinBox_47 = QDoubleSpinBox(self.widget_20)
        self.doubleSpinBox_47.setObjectName(u"doubleSpinBox_47")

        self.gridLayout_57.addWidget(self.doubleSpinBox_47, 0, 1, 1, 1)

        self.label_175 = QLabel(self.widget_20)
        self.label_175.setObjectName(u"label_175")

        self.gridLayout_57.addWidget(self.label_175, 0, 2, 1, 1)


        self.gridLayout_38.addWidget(self.widget_20, 2, 0, 1, 1)

        self.widget_21 = QWidget(self.waveform_ch2_burst)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(0, 0))
        self.gridLayout_58 = QGridLayout(self.widget_21)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.label_176 = QLabel(self.widget_21)
        self.label_176.setObjectName(u"label_176")

        self.gridLayout_58.addWidget(self.label_176, 0, 0, 1, 1)

        self.comboBox_22 = QComboBox(self.widget_21)
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.setObjectName(u"comboBox_22")

        self.gridLayout_58.addWidget(self.comboBox_22, 0, 1, 1, 1)

        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")

        self.gridLayout_58.addWidget(self.widget_22, 0, 2, 1, 1)


        self.gridLayout_38.addWidget(self.widget_21, 1, 0, 1, 1)

        self.widget_23 = QWidget(self.waveform_ch2_burst)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(0, 0))
        self.gridLayout_59 = QGridLayout(self.widget_23)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.state_widget_12 = QWidget(self.widget_23)
        self.state_widget_12.setObjectName(u"state_widget_12")
        self.gridLayout_88 = QGridLayout(self.state_widget_12)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.ch2_chargebalance = QRadioButton(self.state_widget_12)
        self.ch2_chargebalance.setObjectName(u"ch2_chargebalance")

        self.gridLayout_88.addWidget(self.ch2_chargebalance, 0, 2, 1, 1)

        self.ch1_on_12 = QRadioButton(self.state_widget_12)
        self.ch1_on_12.setObjectName(u"ch1_on_12")

        self.gridLayout_88.addWidget(self.ch1_on_12, 0, 1, 1, 1)

        self.label_177 = QLabel(self.state_widget_12)
        self.label_177.setObjectName(u"label_177")

        self.gridLayout_88.addWidget(self.label_177, 0, 0, 1, 1)


        self.gridLayout_59.addWidget(self.state_widget_12, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.widget_23, 3, 0, 1, 1)

        self.widget_24 = QWidget(self.waveform_ch2_burst)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(0, 0))
        self.gridLayout_60 = QGridLayout(self.widget_24)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.radioButton_39 = QRadioButton(self.widget_24)
        self.radioButton_39.setObjectName(u"radioButton_39")

        self.gridLayout_60.addWidget(self.radioButton_39, 0, 2, 1, 1)

        self.label_178 = QLabel(self.widget_24)
        self.label_178.setObjectName(u"label_178")

        self.gridLayout_60.addWidget(self.label_178, 0, 0, 1, 1)

        self.radioButton_40 = QRadioButton(self.widget_24)
        self.radioButton_40.setObjectName(u"radioButton_40")

        self.gridLayout_60.addWidget(self.radioButton_40, 0, 1, 1, 1)


        self.gridLayout_38.addWidget(self.widget_24, 5, 0, 1, 1)


        self.gridLayout_37.addWidget(self.waveform_ch2_burst, 3, 0, 1, 2)

        self.ttl_ch2 = QWidget(self.channel2_settings_burst_2)
        self.ttl_ch2.setObjectName(u"ttl_ch2")
        self.gridLayout_63 = QGridLayout(self.ttl_ch2)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.label_101 = QLabel(self.ttl_ch2)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_63.addWidget(self.label_101, 0, 0, 1, 1)

        self.ch2_on_8 = QRadioButton(self.ttl_ch2)
        self.ch2_on_8.setObjectName(u"ch2_on_8")

        self.gridLayout_63.addWidget(self.ch2_on_8, 0, 1, 1, 1)

        self.ch2_off_8 = QRadioButton(self.ttl_ch2)
        self.ch2_off_8.setObjectName(u"ch2_off_8")

        self.gridLayout_63.addWidget(self.ch2_off_8, 0, 2, 1, 1)


        self.gridLayout_37.addWidget(self.ttl_ch2, 0, 0, 2, 2)


        self.gridLayout_61.addWidget(self.channel2_settings_burst_2, 0, 1, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_3, 3, 0, 1, 1)

        self.PulseSettings = QGroupBox(self.BurstModeSettings)
        self.PulseSettings.setObjectName(u"PulseSettings")
        self.gridLayout_40 = QGridLayout(self.PulseSettings)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
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

        self.radioButton = QRadioButton(self.widget_7)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_41.addWidget(self.radioButton, 1, 3, 1, 1)


        self.gridLayout_40.addWidget(self.widget_7, 0, 3, 1, 1)

        self.spinBox = QSpinBox(self.PulseSettings)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_40.addWidget(self.spinBox, 0, 1, 1, 1)

        self.interpulsedelay_widget = QWidget(self.PulseSettings)
        self.interpulsedelay_widget.setObjectName(u"interpulsedelay_widget")
        sizePolicy.setHeightForWidth(self.interpulsedelay_widget.sizePolicy().hasHeightForWidth())
        self.interpulsedelay_widget.setSizePolicy(sizePolicy)
        self.interpulsedelay_widget.setMinimumSize(QSize(350, 0))
        self.gridLayout_49 = QGridLayout(self.interpulsedelay_widget)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.doubleSpinBox = QDoubleSpinBox(self.interpulsedelay_widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_49.addWidget(self.doubleSpinBox, 0, 1, 1, 1)

        self.widget_29 = QWidget(self.interpulsedelay_widget)
        self.widget_29.setObjectName(u"widget_29")
        self.gridLayout_53 = QGridLayout(self.widget_29)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.label_90 = QLabel(self.widget_29)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_53.addWidget(self.label_90, 0, 0, 1, 1)


        self.gridLayout_49.addWidget(self.widget_29, 0, 2, 1, 1)

        self.widget_12 = QWidget(self.interpulsedelay_widget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(130, 0))
        self.gridLayout_52 = QGridLayout(self.widget_12)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_29 = QLabel(self.widget_12)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_52.addWidget(self.label_29, 0, 0, 1, 1)


        self.gridLayout_49.addWidget(self.widget_12, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.interpulsedelay_widget, 0, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.label_3 = QLabel(self.PulseSettings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_40.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.PulseSettings, 1, 0, 1, 1)

        self.StimSettings = QGroupBox(self.BurstModeSettings)
        self.StimSettings.setObjectName(u"StimSettings")
        self.gridLayout_42 = QGridLayout(self.StimSettings)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.widget_11 = QWidget(self.StimSettings)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy15)
        self.widget_11.setMinimumSize(QSize(0, 0))
        self.gridLayout_46 = QGridLayout(self.widget_11)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.jitter_widget_3 = QWidget(self.widget_11)
        self.jitter_widget_3.setObjectName(u"jitter_widget_3")
        sizePolicy10.setHeightForWidth(self.jitter_widget_3.sizePolicy().hasHeightForWidth())
        self.jitter_widget_3.setSizePolicy(sizePolicy10)
        self.jitter_widget_3.setMinimumSize(QSize(0, 60))
        self.gridLayout_64 = QGridLayout(self.jitter_widget_3)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.widget_25 = QWidget(self.jitter_widget_3)
        self.widget_25.setObjectName(u"widget_25")
        self.gridLayout_65 = QGridLayout(self.widget_25)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.label_102 = QLabel(self.widget_25)
        self.label_102.setObjectName(u"label_102")
        sizePolicy10.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy10)
        self.label_102.setMinimumSize(QSize(0, 15))
        self.label_102.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_102.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_65.addWidget(self.label_102, 0, 0, 1, 1)

        self.doubleSpinBox_24 = QDoubleSpinBox(self.widget_25)
        self.doubleSpinBox_24.setObjectName(u"doubleSpinBox_24")

        self.gridLayout_65.addWidget(self.doubleSpinBox_24, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_65.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.label_103 = QLabel(self.widget_25)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_65.addWidget(self.label_103, 0, 2, 1, 1)


        self.gridLayout_64.addWidget(self.widget_25, 1, 3, 2, 1)

        self.Jitter_4 = QWidget(self.jitter_widget_3)
        self.Jitter_4.setObjectName(u"Jitter_4")
        self.gridLayout_66 = QGridLayout(self.Jitter_4)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.jitter_on_3 = QRadioButton(self.Jitter_4)
        self.jitter_on_3.setObjectName(u"jitter_on_3")

        self.gridLayout_66.addWidget(self.jitter_on_3, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_66.addItem(self.horizontalSpacer_11, 0, 3, 1, 1)

        self.jitter_label_3 = QLabel(self.Jitter_4)
        self.jitter_label_3.setObjectName(u"jitter_label_3")
        sizePolicy10.setHeightForWidth(self.jitter_label_3.sizePolicy().hasHeightForWidth())
        self.jitter_label_3.setSizePolicy(sizePolicy10)
        self.jitter_label_3.setMinimumSize(QSize(0, 15))

        self.gridLayout_66.addWidget(self.jitter_label_3, 0, 0, 1, 1)

        self.jitter_off_3 = QRadioButton(self.Jitter_4)
        self.jitter_off_3.setObjectName(u"jitter_off_3")

        self.gridLayout_66.addWidget(self.jitter_off_3, 0, 2, 1, 1)


        self.gridLayout_64.addWidget(self.Jitter_4, 1, 1, 2, 1)


        self.gridLayout_46.addWidget(self.jitter_widget_3, 0, 0, 1, 1)


        self.gridLayout_42.addWidget(self.widget_11, 2, 0, 1, 7)

        self.widget_26 = QWidget(self.StimSettings)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(250, 0))
        self.widget_26.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout_47 = QGridLayout(self.widget_26)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(70, 0))
        self.gridLayout_51 = QGridLayout(self.widget_28)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_92 = QLabel(self.widget_28)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_51.addWidget(self.label_92, 0, 0, 1, 1)


        self.gridLayout_47.addWidget(self.widget_28, 1, 2, 1, 1)

        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy)
        self.widget_27.setMinimumSize(QSize(130, 0))
        self.widget_27.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.gridLayout_50 = QGridLayout(self.widget_27)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.interstim_delay_2 = QLabel(self.widget_27)
        self.interstim_delay_2.setObjectName(u"interstim_delay_2")
        self.interstim_delay_2.setMinimumSize(QSize(66, 0))

        self.gridLayout_50.addWidget(self.interstim_delay_2, 0, 0, 1, 1)


        self.gridLayout_47.addWidget(self.widget_27, 1, 0, 1, 1)

        self.interstim_delay = QDoubleSpinBox(self.widget_26)
        self.interstim_delay.setObjectName(u"interstim_delay")

        self.gridLayout_47.addWidget(self.interstim_delay, 1, 1, 1, 1)


        self.gridLayout_42.addWidget(self.widget_26, 0, 6, 1, 1)

        self.num_stims = QSpinBox(self.StimSettings)
        self.num_stims.setObjectName(u"num_stims")
        self.num_stims.setMinimum(1)

        self.gridLayout_42.addWidget(self.num_stims, 0, 1, 1, 1)

        self.widget_8 = QWidget(self.StimSettings)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_43 = QGridLayout(self.widget_8)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.radioButton_4 = QRadioButton(self.widget_8)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_43.addWidget(self.radioButton_4, 1, 2, 1, 1)

        self.label_91 = QLabel(self.widget_8)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_43.addWidget(self.label_91, 1, 0, 1, 1)

        self.freq_select_stim = QRadioButton(self.widget_8)
        self.freq_select_stim.setObjectName(u"freq_select_stim")

        self.gridLayout_43.addWidget(self.freq_select_stim, 1, 3, 1, 1)


        self.gridLayout_42.addWidget(self.widget_8, 0, 3, 1, 1)

        self.line = QFrame(self.StimSettings)
        self.line.setObjectName(u"line")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy16)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_42.addWidget(self.line, 1, 0, 1, 7)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.num_stims_label = QLabel(self.StimSettings)
        self.num_stims_label.setObjectName(u"num_stims_label")

        self.gridLayout_42.addWidget(self.num_stims_label, 0, 0, 1, 1)

        self.random_freq_widget = QWidget(self.StimSettings)
        self.random_freq_widget.setObjectName(u"random_freq_widget")
        self.random_freq_widget.setMinimumSize(QSize(200, 0))
        self.gridLayout_111 = QGridLayout(self.random_freq_widget)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.rand_freq_onoff = QWidget(self.random_freq_widget)
        self.rand_freq_onoff.setObjectName(u"rand_freq_onoff")
        self.gridLayout_110 = QGridLayout(self.rand_freq_onoff)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.rf_on = QRadioButton(self.rand_freq_onoff)
        self.rf_on.setObjectName(u"rf_on")
        sizePolicy9.setHeightForWidth(self.rf_on.sizePolicy().hasHeightForWidth())
        self.rf_on.setSizePolicy(sizePolicy9)

        self.gridLayout_110.addWidget(self.rf_on, 0, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_110.addItem(self.horizontalSpacer_22, 0, 3, 1, 1)

        self.jitter_label_5 = QLabel(self.rand_freq_onoff)
        self.jitter_label_5.setObjectName(u"jitter_label_5")
        sizePolicy10.setHeightForWidth(self.jitter_label_5.sizePolicy().hasHeightForWidth())
        self.jitter_label_5.setSizePolicy(sizePolicy10)
        self.jitter_label_5.setMinimumSize(QSize(100, 15))

        self.gridLayout_110.addWidget(self.jitter_label_5, 0, 0, 1, 1)

        self.rf_off = QRadioButton(self.rand_freq_onoff)
        self.rf_off.setObjectName(u"rf_off")
        sizePolicy9.setHeightForWidth(self.rf_off.sizePolicy().hasHeightForWidth())
        self.rf_off.setSizePolicy(sizePolicy9)

        self.gridLayout_110.addWidget(self.rf_off, 0, 2, 1, 1)


        self.gridLayout_111.addWidget(self.rand_freq_onoff, 1, 0, 1, 1)

        self.rf_settings = QWidget(self.random_freq_widget)
        self.rf_settings.setObjectName(u"rf_settings")
        self.rf_settings.setMinimumSize(QSize(100, 0))
        self.gridLayout_112 = QGridLayout(self.rf_settings)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.label_84 = QLabel(self.rf_settings)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_112.addWidget(self.label_84, 0, 3, 1, 1)

        self.rf_lower = QDoubleSpinBox(self.rf_settings)
        self.rf_lower.setObjectName(u"rf_lower")
        sizePolicy3.setHeightForWidth(self.rf_lower.sizePolicy().hasHeightForWidth())
        self.rf_lower.setSizePolicy(sizePolicy3)
        self.rf_lower.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_112.addWidget(self.rf_lower, 0, 1, 1, 1)

        self.rf_upper = QDoubleSpinBox(self.rf_settings)
        self.rf_upper.setObjectName(u"rf_upper")
        sizePolicy3.setHeightForWidth(self.rf_upper.sizePolicy().hasHeightForWidth())
        self.rf_upper.setSizePolicy(sizePolicy3)
        self.rf_upper.setMaximumSize(QSize(90, 16777215))

        self.gridLayout_112.addWidget(self.rf_upper, 0, 2, 1, 1)

        self.label_83 = QLabel(self.rf_settings)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(100, 0))

        self.gridLayout_112.addWidget(self.label_83, 0, 0, 1, 1)


        self.gridLayout_111.addWidget(self.rf_settings, 1, 5, 1, 1)

        self.line_2 = QFrame(self.random_freq_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_111.addWidget(self.line_2, 0, 0, 1, 6)


        self.gridLayout_42.addWidget(self.random_freq_widget, 3, 0, 1, 6)


        self.gridLayout_39.addWidget(self.StimSettings, 0, 0, 1, 1)


        self.gridLayout_55.addWidget(self.BurstModeSettings, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_13.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.modeSelektor.addTab(self.BurstMode, "")
        self.TrialMode = QWidget()
        self.TrialMode.setObjectName(u"TrialMode")
        self.gridLayout_67 = QGridLayout(self.TrialMode)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.scrollArea_3 = QScrollArea(self.TrialMode)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1018, 839))
        self.gridLayout_92 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.trial_window = QGroupBox(self.scrollAreaWidgetContents_3)
        self.trial_window.setObjectName(u"trial_window")
        self.gridLayout_68 = QGridLayout(self.trial_window)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.load_save_groupBox = QGroupBox(self.trial_window)
        self.load_save_groupBox.setObjectName(u"load_save_groupBox")
        self.gridLayout_69 = QGridLayout(self.load_save_groupBox)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.load_widget = QWidget(self.load_save_groupBox)
        self.load_widget.setObjectName(u"load_widget")
        self.gridLayout_70 = QGridLayout(self.load_widget)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.label_17 = QLabel(self.load_widget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_70.addWidget(self.label_17, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_70.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.lineEdit = QLineEdit(self.load_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_70.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.load_widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_70.addWidget(self.pushButton_5, 1, 2, 1, 1)


        self.gridLayout_69.addWidget(self.load_widget, 0, 0, 1, 1)

        self.save_widget = QWidget(self.load_save_groupBox)
        self.save_widget.setObjectName(u"save_widget")
        self.gridLayout_71 = QGridLayout(self.save_widget)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.label_18 = QLabel(self.save_widget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_71.addWidget(self.label_18, 1, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_71.addItem(self.horizontalSpacer_7, 1, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.save_widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_71.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.save_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_71.addWidget(self.pushButton_6, 1, 2, 1, 1)


        self.gridLayout_69.addWidget(self.save_widget, 1, 0, 1, 1)


        self.gridLayout_68.addWidget(self.load_save_groupBox, 0, 0, 1, 1)

        self.trial_settings = QGroupBox(self.trial_window)
        self.trial_settings.setObjectName(u"trial_settings")
        self.gridLayout_73 = QGridLayout(self.trial_settings)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.left_column = QWidget(self.trial_settings)
        self.left_column.setObjectName(u"left_column")
        self.gridLayout_74 = QGridLayout(self.left_column)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.spinBox_4 = QSpinBox(self.left_column)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_74.addWidget(self.spinBox_4, 6, 2, 1, 1)

        self.label_78 = QLabel(self.left_column)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_74.addWidget(self.label_78, 0, 1, 1, 1)

        self.label_73 = QLabel(self.left_column)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_74.addWidget(self.label_73, 5, 3, 1, 1)

        self.spinBox_2 = QSpinBox(self.left_column)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_74.addWidget(self.spinBox_2, 3, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.left_column)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_74.addWidget(self.spinBox_3, 5, 2, 1, 1)

        self.label_20 = QLabel(self.left_column)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_74.addWidget(self.label_20, 1, 1, 1, 1)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.left_column)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")

        self.gridLayout_74.addWidget(self.doubleSpinBox_17, 1, 2, 1, 1)

        self.label_56 = QLabel(self.left_column)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_74.addWidget(self.label_56, 3, 3, 1, 1)

        self.label_51 = QLabel(self.left_column)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_74.addWidget(self.label_51, 1, 3, 1, 1)

        self.label_19 = QLabel(self.left_column)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_74.addWidget(self.label_19, 3, 1, 1, 1)

        self.label_75 = QLabel(self.left_column)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_74.addWidget(self.label_75, 6, 3, 1, 1)

        self.label_74 = QLabel(self.left_column)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_74.addWidget(self.label_74, 6, 1, 1, 1)

        self.manual_auto = QWidget(self.left_column)
        self.manual_auto.setObjectName(u"manual_auto")
        self.gridLayout_91 = QGridLayout(self.manual_auto)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.radioButton_7 = QRadioButton(self.manual_auto)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout_91.addWidget(self.radioButton_7, 0, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.manual_auto)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_91.addWidget(self.radioButton_3, 0, 2, 1, 1)


        self.gridLayout_74.addWidget(self.manual_auto, 0, 2, 1, 2)

        self.label_72 = QLabel(self.left_column)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_74.addWidget(self.label_72, 5, 1, 1, 1)

        self.label_76 = QLabel(self.left_column)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_74.addWidget(self.label_76, 2, 1, 1, 1)

        self.spinBox_5 = QSpinBox(self.left_column)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout_74.addWidget(self.spinBox_5, 2, 2, 1, 1)

        self.label_77 = QLabel(self.left_column)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_74.addWidget(self.label_77, 2, 3, 1, 1)


        self.gridLayout_73.addWidget(self.left_column, 0, 0, 1, 1)

        self.right_column = QWidget(self.trial_settings)
        self.right_column.setObjectName(u"right_column")
        self.gridLayout_89 = QGridLayout(self.right_column)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.ds5_settings_trial = QWidget(self.right_column)
        self.ds5_settings_trial.setObjectName(u"ds5_settings_trial")
        self.gridLayout_100 = QGridLayout(self.ds5_settings_trial)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.groupBox_29 = QGroupBox(self.ds5_settings_trial)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.gridLayout_99 = QGridLayout(self.groupBox_29)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.label_179 = QLabel(self.groupBox_29)
        self.label_179.setObjectName(u"label_179")

        self.gridLayout_99.addWidget(self.label_179, 0, 0, 1, 1)

        self.ds5_trial_input = QComboBox(self.groupBox_29)
        self.ds5_trial_input.addItem("")
        self.ds5_trial_input.addItem("")
        self.ds5_trial_input.addItem("")
        self.ds5_trial_input.addItem("")
        self.ds5_trial_input.setObjectName(u"ds5_trial_input")

        self.gridLayout_99.addWidget(self.ds5_trial_input, 0, 1, 1, 1)

        self.label_181 = QLabel(self.groupBox_29)
        self.label_181.setObjectName(u"label_181")

        self.gridLayout_99.addWidget(self.label_181, 0, 2, 1, 1)

        self.label_182 = QLabel(self.groupBox_29)
        self.label_182.setObjectName(u"label_182")

        self.gridLayout_99.addWidget(self.label_182, 2, 0, 1, 1)

        self.label_184 = QLabel(self.groupBox_29)
        self.label_184.setObjectName(u"label_184")

        self.gridLayout_99.addWidget(self.label_184, 2, 2, 1, 1)

        self.ds5_trial_output = QComboBox(self.groupBox_29)
        self.ds5_trial_output.addItem("")
        self.ds5_trial_output.addItem("")
        self.ds5_trial_output.addItem("")
        self.ds5_trial_output.setObjectName(u"ds5_trial_output")

        self.gridLayout_99.addWidget(self.ds5_trial_output, 2, 1, 1, 1)


        self.gridLayout_100.addWidget(self.groupBox_29, 0, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.ds5_settings_trial)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_105 = QGridLayout(self.groupBox_10)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.label_180 = QLabel(self.groupBox_10)
        self.label_180.setObjectName(u"label_180")

        self.gridLayout_105.addWidget(self.label_180, 0, 0, 1, 1)

        self.label_80 = QLabel(self.groupBox_10)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_105.addWidget(self.label_80, 1, 0, 1, 1)

        self.trial_starting_current = QSpinBox(self.groupBox_10)
        self.trial_starting_current.setObjectName(u"trial_starting_current")

        self.gridLayout_105.addWidget(self.trial_starting_current, 0, 1, 1, 1)

        self.label_183 = QLabel(self.groupBox_10)
        self.label_183.setObjectName(u"label_183")

        self.gridLayout_105.addWidget(self.label_183, 0, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox_10)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_105.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_81 = QLabel(self.groupBox_10)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_105.addWidget(self.label_81, 1, 2, 1, 1)


        self.gridLayout_100.addWidget(self.groupBox_10, 1, 0, 1, 1)


        self.gridLayout_89.addWidget(self.ds5_settings_trial, 2, 0, 1, 3)


        self.gridLayout_73.addWidget(self.right_column, 0, 1, 1, 1)


        self.gridLayout_68.addWidget(self.trial_settings, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.trial_window)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 300))
        self.gridLayout_72 = QGridLayout(self.groupBox_4)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.tableWidget = QTableWidget(self.groupBox_4)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.gridLayout_72.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_68.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.widget_30 = QWidget(self.trial_window)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(0, 50))
        self.gridLayout_90 = QGridLayout(self.widget_30)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.pushButton_7 = QPushButton(self.widget_30)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(111, 0))

        self.gridLayout_90.addWidget(self.pushButton_7, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_90.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_90.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)


        self.gridLayout_68.addWidget(self.widget_30, 3, 0, 1, 1)


        self.gridLayout_92.addWidget(self.trial_window, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_67.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.modeSelektor.addTab(self.TrialMode, "")

        self.gridLayout_93.addWidget(self.modeSelektor, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.trial_settings_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.retranslateUi(Controller_Main)

        self.stackedWidget.setCurrentIndex(1)
        self.modeSelektor.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.current_control_ch1burst.setCurrentIndex(0)
        self.current_control_ch2burst.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Controller_Main)
    # setupUi

    def retranslateUi(self, Controller_Main):
        Controller_Main.setWindowTitle(QCoreApplication.translate("Controller_Main", u"Stimulation Control", None))
        self.system_status.setTitle(QCoreApplication.translate("Controller_Main", u"System Status", None))
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
        self.d188_ch.setTitle("")
        self.label_28.setText(QCoreApplication.translate("Controller_Main", u"D188 Channel", None))
        self.groupBox_6.setTitle("")
        self.condition_label.setText(QCoreApplication.translate("Controller_Main", u"Active", None))
        self.abprt_button.setText(QCoreApplication.translate("Controller_Main", u"Abort", None))
        self.trial_number.setText(QCoreApplication.translate("Controller_Main", u"Trial 1/5", None))
        self.increase_intensity.setText(QCoreApplication.translate("Controller_Main", u"Increase Intensity", None))
        self.decrease_intensity.setText(QCoreApplication.translate("Controller_Main", u"Decrease Intensity", None))
        self.previous_config.setText(QCoreApplication.translate("Controller_Main", u"Previous Config", None))
        self.trial_timer_label.setText(QCoreApplication.translate("Controller_Main", u"Trial Time:", None))
        self.totaltime_label.setText(QCoreApplication.translate("Controller_Main", u"Total Time: ", None))
        self.trial_timer.setText(QCoreApplication.translate("Controller_Main", u"trial_placeholder", None))
        self.totaltime_2.setText(QCoreApplication.translate("Controller_Main", u"total_placeholder", None))
        self.radioButton_8.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.radioButton_9.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_79.setText(QCoreApplication.translate("Controller_Main", u"Stimulation", None))
        self.next_config.setText(QCoreApplication.translate("Controller_Main", u"Next Config", None))
        self.log_button.setText(QCoreApplication.translate("Controller_Main", u"Log", None))
        self.label_82.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.int_label.setText(QCoreApplication.translate("Controller_Main", u"Intensity:", None))
        self.inc_up.setText(QCoreApplication.translate("Controller_Main", u"+", None))
        self.inc_down.setText(QCoreApplication.translate("Controller_Main", u"-", None))
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
        self.label_68.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.radioButton_18.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_65.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_67.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_66.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_17.setText(QCoreApplication.translate("Controller_Main", u"No", None))
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
        self.stop_button.setText(QCoreApplication.translate("Controller_Main", u"Stop", None))
        self.BurstModeSettings.setTitle("")
        self.groupBox_11.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2 Delay Settings", None))
        self.label_21.setText(QCoreApplication.translate("Controller_Main", u"Channel 2 State", None))
        self.radioButton_6.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.radioButton_5.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.label_95.setText(QCoreApplication.translate("Controller_Main", u"Milliseconds", None))
        self.label_88.setText(QCoreApplication.translate("Controller_Main", u"Channel 2 Delay", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Controller_Main", u"Waveform Settings", None))
        self.channel1_settings_burst.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 1", None))
        self.groupBox_25.setTitle("")
        self.label_141.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.label_142.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_143.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_144.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_145.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.label_146.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.comboBox_18.setItemText(0, QCoreApplication.translate("Controller_Main", u"10", None))
        self.comboBox_18.setItemText(1, QCoreApplication.translate("Controller_Main", u"25", None))
        self.comboBox_18.setItemText(2, QCoreApplication.translate("Controller_Main", u"50", None))

        self.comboBox_17.setItemText(0, QCoreApplication.translate("Controller_Main", u"1", None))
        self.comboBox_17.setItemText(1, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.comboBox_17.setItemText(2, QCoreApplication.translate("Controller_Main", u"5", None))
        self.comboBox_17.setItemText(3, QCoreApplication.translate("Controller_Main", u"10", None))

        self.current_control_ch1burst.setTabText(self.current_control_ch1burst.indexOf(self.tab_13), QCoreApplication.translate("Controller_Main", u"DS5 Control", None))
        self.groupBox_13.setTitle("")
        self.label_147.setText(QCoreApplication.translate("Controller_Main", u"Voltage High", None))
        self.label_148.setText(QCoreApplication.translate("Controller_Main", u"Voltage Low", None))
        self.label_149.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_150.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.current_control_ch1burst.setTabText(self.current_control_ch1burst.indexOf(self.tab_14), QCoreApplication.translate("Controller_Main", u"FuncGen Control", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.label_155.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_156.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_33.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_34.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_157.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_158.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_152.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_153.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_151.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_19.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_19.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.ch1_off_11.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.ch1_on_11.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_154.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.radioButton_36.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.label_159.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.radioButton_35.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.label_96.setText(QCoreApplication.translate("Controller_Main", u"TTL", None))
        self.ch1_on_7.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.ch1_off_7.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.channel2_settings_burst_2.setTitle(QCoreApplication.translate("Controller_Main", u"Channel 2", None))
        self.groupBox_27.setTitle("")
        self.label_163.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_161.setText(QCoreApplication.translate("Controller_Main", u"Desired Current", None))
        self.label_165.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.label_160.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("Controller_Main", u"10", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("Controller_Main", u"25", None))
        self.comboBox_21.setItemText(2, QCoreApplication.translate("Controller_Main", u"50", None))

        self.label_164.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("Controller_Main", u"1", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.comboBox_20.setItemText(2, QCoreApplication.translate("Controller_Main", u"5", None))
        self.comboBox_20.setItemText(3, QCoreApplication.translate("Controller_Main", u"10", None))

        self.label_162.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.current_control_ch2burst.setTabText(self.current_control_ch2burst.indexOf(self.tab_15), QCoreApplication.translate("Controller_Main", u"DS5 Control", None))
        self.groupBox_14.setTitle("")
        self.label_166.setText(QCoreApplication.translate("Controller_Main", u"Voltage High", None))
        self.label_167.setText(QCoreApplication.translate("Controller_Main", u"Voltage Low", None))
        self.label_168.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_169.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.current_control_ch2burst.setTabText(self.current_control_ch2burst.indexOf(self.tab_16), QCoreApplication.translate("Controller_Main", u"FuncGen Control", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("Controller_Main", u"Custom Waveform", None))
        self.label_170.setText(QCoreApplication.translate("Controller_Main", u"Auto K", None))
        self.label_171.setText(QCoreApplication.translate("Controller_Main", u"Prepulse Width", None))
        self.radioButton_37.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.radioButton_38.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_172.setText(QCoreApplication.translate("Controller_Main", u"K Value", None))
        self.label_173.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_174.setText(QCoreApplication.translate("Controller_Main", u"Pulse Width", None))
        self.label_175.setText(QCoreApplication.translate("Controller_Main", u"ms", None))
        self.label_176.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None))
        self.comboBox_22.setItemText(0, QCoreApplication.translate("Controller_Main", u"Sine", None))
        self.comboBox_22.setItemText(1, QCoreApplication.translate("Controller_Main", u"Square", None))
        self.comboBox_22.setItemText(2, QCoreApplication.translate("Controller_Main", u"Pulse", None))
        self.comboBox_22.setItemText(3, QCoreApplication.translate("Controller_Main", u"Custom", None))

        self.ch2_chargebalance.setText(QCoreApplication.translate("Controller_Main", u"No", None))
        self.ch1_on_12.setText(QCoreApplication.translate("Controller_Main", u"Yes", None))
        self.label_177.setText(QCoreApplication.translate("Controller_Main", u"Charge Balance", None))
        self.radioButton_39.setText(QCoreApplication.translate("Controller_Main", u"Reversed", None))
        self.label_178.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None))
        self.radioButton_40.setText(QCoreApplication.translate("Controller_Main", u"Normal", None))
        self.label_101.setText(QCoreApplication.translate("Controller_Main", u"TTL", None))
        self.ch2_on_8.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.ch2_off_8.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.PulseSettings.setTitle(QCoreApplication.translate("Controller_Main", u"Pulse Settings", None))
        self.label_89.setText(QCoreApplication.translate("Controller_Main", u"Frequency/Period", None))
        self.radioButton_2.setText(QCoreApplication.translate("Controller_Main", u"Period", None))
        self.radioButton.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.label_90.setText(QCoreApplication.translate("Controller_Main", u"Milliseconds", None))
        self.label_29.setText(QCoreApplication.translate("Controller_Main", u"Interpulse Delay", None))
        self.label_3.setText(QCoreApplication.translate("Controller_Main", u"Pulses per Stim", None))
        self.StimSettings.setTitle(QCoreApplication.translate("Controller_Main", u"Stim Settings", None))
        self.label_102.setText(QCoreApplication.translate("Controller_Main", u"Jitter Rate (+/-)", None))
        self.label_103.setText(QCoreApplication.translate("Controller_Main", u"Seconds", None))
        self.jitter_on_3.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.jitter_label_3.setText(QCoreApplication.translate("Controller_Main", u"Jitter", None))
        self.jitter_off_3.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_92.setText(QCoreApplication.translate("Controller_Main", u"Seconds", None))
        self.interstim_delay_2.setText(QCoreApplication.translate("Controller_Main", u"Interstim Delay", None))
        self.radioButton_4.setText(QCoreApplication.translate("Controller_Main", u"Period", None))
        self.label_91.setText(QCoreApplication.translate("Controller_Main", u"Frequency/Period", None))
        self.freq_select_stim.setText(QCoreApplication.translate("Controller_Main", u"Frequency", None))
        self.num_stims_label.setText(QCoreApplication.translate("Controller_Main", u"Number of Stims", None))
        self.rf_on.setText(QCoreApplication.translate("Controller_Main", u"On", None))
        self.jitter_label_5.setText(QCoreApplication.translate("Controller_Main", u"Random Freq", None))
        self.rf_off.setText(QCoreApplication.translate("Controller_Main", u"Off", None))
        self.label_84.setText(QCoreApplication.translate("Controller_Main", u"Hz", None))
        self.label_83.setText(QCoreApplication.translate("Controller_Main", u"Upper/Lower", None))
        self.modeSelektor.setTabText(self.modeSelektor.indexOf(self.BurstMode), QCoreApplication.translate("Controller_Main", u"Burst Mode", None))
        self.trial_window.setTitle("")
        self.load_save_groupBox.setTitle(QCoreApplication.translate("Controller_Main", u"Save/Load Profile", None))
        self.label_17.setText(QCoreApplication.translate("Controller_Main", u"Load Profile", None))
        self.pushButton_5.setText(QCoreApplication.translate("Controller_Main", u"Browse", None))
        self.label_18.setText(QCoreApplication.translate("Controller_Main", u"Save Profile", None))
        self.pushButton_6.setText(QCoreApplication.translate("Controller_Main", u"Browse", None))
        self.trial_settings.setTitle(QCoreApplication.translate("Controller_Main", u"Trial Settings", None))
        self.label_78.setText(QCoreApplication.translate("Controller_Main", u"Timing", None))
        self.label_73.setText(QCoreApplication.translate("Controller_Main", u"Seconds", None))
        self.label_20.setText(QCoreApplication.translate("Controller_Main", u"Max Intensity", None))
        self.label_56.setText("")
        self.label_51.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.label_19.setText(QCoreApplication.translate("Controller_Main", u"Number of Trials", None))
        self.label_75.setText(QCoreApplication.translate("Controller_Main", u"Seconds", None))
        self.label_74.setText(QCoreApplication.translate("Controller_Main", u"Rest Period", None))
        self.radioButton_7.setText(QCoreApplication.translate("Controller_Main", u"Automatic", None))
        self.radioButton_3.setText(QCoreApplication.translate("Controller_Main", u"Manual", None))
        self.label_72.setText(QCoreApplication.translate("Controller_Main", u"Trial Length", None))
        self.label_76.setText(QCoreApplication.translate("Controller_Main", u"% of Max", None))
        self.label_77.setText(QCoreApplication.translate("Controller_Main", u"%", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("Controller_Main", u"DS5 Settings", None))
        self.label_179.setText(QCoreApplication.translate("Controller_Main", u"DS5 Input Voltage", None))
        self.ds5_trial_input.setItemText(0, QCoreApplication.translate("Controller_Main", u"1", None))
        self.ds5_trial_input.setItemText(1, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.ds5_trial_input.setItemText(2, QCoreApplication.translate("Controller_Main", u"5", None))
        self.ds5_trial_input.setItemText(3, QCoreApplication.translate("Controller_Main", u"10", None))

        self.label_181.setText(QCoreApplication.translate("Controller_Main", u"Volts", None))
        self.label_182.setText(QCoreApplication.translate("Controller_Main", u"DS5 Output Current", None))
        self.label_184.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.ds5_trial_output.setItemText(0, QCoreApplication.translate("Controller_Main", u"10", None))
        self.ds5_trial_output.setItemText(1, QCoreApplication.translate("Controller_Main", u"25", None))
        self.ds5_trial_output.setItemText(2, QCoreApplication.translate("Controller_Main", u"50", None))

        self.groupBox_10.setTitle(QCoreApplication.translate("Controller_Main", u"Current Settings", None))
        self.label_180.setText(QCoreApplication.translate("Controller_Main", u"Starting Current", None))
        self.label_80.setText(QCoreApplication.translate("Controller_Main", u"Current Increment", None))
        self.label_183.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Controller_Main", u"0.5", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Controller_Main", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Controller_Main", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Controller_Main", u"2.5", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Controller_Main", u"3", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Controller_Main", u"4", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Controller_Main", u"5", None))

        self.label_81.setText(QCoreApplication.translate("Controller_Main", u"mA", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Controller_Main", u"Conditions", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Controller_Main", u"Electrode Configuration", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Controller_Main", u"Waveform", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Controller_Main", u"Polarity", None));
        self.pushButton_7.setText(QCoreApplication.translate("Controller_Main", u"Start", None))
        self.modeSelektor.setTabText(self.modeSelektor.indexOf(self.TrialMode), QCoreApplication.translate("Controller_Main", u"Trial Mode", None))
    # retranslateUi

