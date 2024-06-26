# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainApp(object):
    def setupUi(self, MainApp):
        if not MainApp.objectName():
            MainApp.setObjectName(u"MainApp")
        MainApp.setEnabled(True)
        MainApp.resize(960, 540)
        MainApp.setMinimumSize(QSize(960, 540))
        MainApp.setStyleSheet(u"font: 10pt \"SF Pro Bold\";")
        self.centralwidget = QWidget(MainApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sideBarGroup = QGroupBox(self.centralwidget)
        self.sideBarGroup.setObjectName(u"sideBarGroup")
        self.sideBarGroup.setMouseTracking(False)
        self.sideBarGroup.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(79, 79, 79);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.sideBarGroup)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.sideBarVertLayout = QVBoxLayout()
        self.sideBarVertLayout.setSpacing(15)
        self.sideBarVertLayout.setObjectName(u"sideBarVertLayout")
        self.homeButton = QPushButton(self.sideBarGroup)
        self.homeButton.setObjectName(u"homeButton")

        self.sideBarVertLayout.addWidget(self.homeButton)

        self.calibrationButton = QPushButton(self.sideBarGroup)
        self.calibrationButton.setObjectName(u"calibrationButton")

        self.sideBarVertLayout.addWidget(self.calibrationButton)

        self.trackingButton = QPushButton(self.sideBarGroup)
        self.trackingButton.setObjectName(u"trackingButton")

        self.sideBarVertLayout.addWidget(self.trackingButton)

        self.settingsButton = QPushButton(self.sideBarGroup)
        self.settingsButton.setObjectName(u"settingsButton")

        self.sideBarVertLayout.addWidget(self.settingsButton)

        self.verticalSpacer = QSpacerItem(20, 618, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sideBarVertLayout.addItem(self.verticalSpacer)

        self.quitButton = QPushButton(self.sideBarGroup)
        self.quitButton.setObjectName(u"quitButton")

        self.sideBarVertLayout.addWidget(self.quitButton)


        self.horizontalLayout.addLayout(self.sideBarVertLayout)


        self.gridLayout_2.addWidget(self.sideBarGroup, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.cord_frame = QFrame(self.centralwidget)
        self.cord_frame.setObjectName(u"cord_frame")
        self.cord_frame.setFrameShape(QFrame.StyledPanel)
        self.cord_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.cord_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.xCord_frame = QFrame(self.cord_frame)
        self.xCord_frame.setObjectName(u"xCord_frame")
        self.xCord_frame.setFrameShape(QFrame.StyledPanel)
        self.xCord_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.xCord_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.xLabel = QLabel(self.xCord_frame)
        self.xLabel.setObjectName(u"xLabel")

        self.horizontalLayout_5.addWidget(self.xLabel)

        self.xValue = QLineEdit(self.xCord_frame)
        self.xValue.setObjectName(u"xValue")
        self.xValue.setEnabled(True)
        self.xValue.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.xValue)


        self.verticalLayout_4.addWidget(self.xCord_frame)

        self.yCord_frame = QFrame(self.cord_frame)
        self.yCord_frame.setObjectName(u"yCord_frame")
        self.yCord_frame.setFrameShape(QFrame.StyledPanel)
        self.yCord_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.yCord_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.yLabel = QLabel(self.yCord_frame)
        self.yLabel.setObjectName(u"yLabel")

        self.horizontalLayout_6.addWidget(self.yLabel)

        self.yValue = QLineEdit(self.yCord_frame)
        self.yValue.setObjectName(u"yValue")
        self.yValue.setEnabled(True)
        self.yValue.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.yValue)


        self.verticalLayout_4.addWidget(self.yCord_frame)

        self.zCord_frame = QFrame(self.cord_frame)
        self.zCord_frame.setObjectName(u"zCord_frame")
        self.zCord_frame.setFrameShape(QFrame.StyledPanel)
        self.zCord_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.zCord_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.zLabel = QLabel(self.zCord_frame)
        self.zLabel.setObjectName(u"zLabel")

        self.horizontalLayout_7.addWidget(self.zLabel)

        self.zValue = QLineEdit(self.zCord_frame)
        self.zValue.setObjectName(u"zValue")
        self.zValue.setEnabled(True)
        self.zValue.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.zValue)


        self.verticalLayout_4.addWidget(self.zCord_frame)

        self.frame = QFrame(self.cord_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.VRstatus_label = QLabel(self.frame)
        self.VRstatus_label.setObjectName(u"VRstatus_label")

        self.verticalLayout_3.addWidget(self.VRstatus_label)


        self.verticalLayout_4.addWidget(self.frame)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.cord_frame)

        self.log_frame = QFrame(self.centralwidget)
        self.log_frame.setObjectName(u"log_frame")
        self.log_frame.setFrameShape(QFrame.StyledPanel)
        self.log_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.log_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.log_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.log_box = QListView(self.log_frame)
        self.log_box.setObjectName(u"log_box")

        self.verticalLayout_2.addWidget(self.log_box)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.log_frame)

        self.plotFrameContainer = QFrame(self.centralwidget)
        self.plotFrameContainer.setObjectName(u"plotFrameContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotFrameContainer.sizePolicy().hasHeightForWidth())
        self.plotFrameContainer.setSizePolicy(sizePolicy)
        self.plotFrameContainer.setMinimumSize(QSize(200, 200))
        self.plotFrameContainer.setSizeIncrement(QSize(1, 1))
        self.plotFrameContainer.setBaseSize(QSize(500, 500))
        self.plotFrameContainer.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"width: 200")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.plotFrameContainer)


        self.gridLayout_2.addLayout(self.formLayout, 0, 1, 1, 1)

        MainApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainApp)

        QMetaObject.connectSlotsByName(MainApp)
    # setupUi

    def retranslateUi(self, MainApp):
        MainApp.setWindowTitle(QCoreApplication.translate("MainApp", u"MainWindow", None))
        self.homeButton.setText(QCoreApplication.translate("MainApp", u"Home", None))
        self.calibrationButton.setText(QCoreApplication.translate("MainApp", u"Calibartion", None))
        self.trackingButton.setText(QCoreApplication.translate("MainApp", u"Tracking", None))
        self.settingsButton.setText(QCoreApplication.translate("MainApp", u"Settings", None))
        self.quitButton.setText(QCoreApplication.translate("MainApp", u"Quit", None))
        self.xLabel.setText(QCoreApplication.translate("MainApp", u"X: ", None))
        self.yLabel.setText(QCoreApplication.translate("MainApp", u"Y:", None))
        self.zLabel.setText(QCoreApplication.translate("MainApp", u"Z: ", None))
        self.VRstatus_label.setText(QCoreApplication.translate("MainApp", u"VR Disconnected", None))
        self.label.setText(QCoreApplication.translate("MainApp", u"Log", None))
    # retranslateUi

