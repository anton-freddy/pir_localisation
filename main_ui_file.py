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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1230, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.sideBarGroup = QGroupBox(self.centralwidget)
        self.sideBarGroup.setObjectName(u"sideBarGroup")
        self.sideBarGroup.setGeometry(QRect(0, 0, 138, 801))
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

        self.dataButton = QPushButton(self.sideBarGroup)
        self.dataButton.setObjectName(u"dataButton")

        self.sideBarVertLayout.addWidget(self.dataButton)

        self.verticalSpacer = QSpacerItem(20, 618, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sideBarVertLayout.addItem(self.verticalSpacer)

        self.quitButton = QPushButton(self.sideBarGroup)
        self.quitButton.setObjectName(u"quitButton")

        self.sideBarVertLayout.addWidget(self.quitButton)


        self.horizontalLayout.addLayout(self.sideBarVertLayout)

        self.log_box = QListView(self.centralwidget)
        self.log_box.setObjectName(u"log_box")
        self.log_box.setGeometry(QRect(150, 660, 1071, 131))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 640, 49, 16))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(150, 10, 941, 602))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.xLabel = QLabel(self.gridLayoutWidget)
        self.xLabel.setObjectName(u"xLabel")

        self.horizontalLayout_2.addWidget(self.xLabel)

        self.xValue = QLineEdit(self.gridLayoutWidget)
        self.xValue.setObjectName(u"xValue")
        self.xValue.setEnabled(True)
        self.xValue.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.xValue)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.yLabel = QLabel(self.gridLayoutWidget)
        self.yLabel.setObjectName(u"yLabel")

        self.horizontalLayout_3.addWidget(self.yLabel)

        self.yValue = QLineEdit(self.gridLayoutWidget)
        self.yValue.setObjectName(u"yValue")
        self.yValue.setEnabled(True)
        self.yValue.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.yValue)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.zLabel = QLabel(self.gridLayoutWidget)
        self.zLabel.setObjectName(u"zLabel")

        self.horizontalLayout_4.addWidget(self.zLabel)

        self.zValue = QLineEdit(self.gridLayoutWidget)
        self.zValue.setObjectName(u"zValue")
        self.zValue.setEnabled(True)
        self.zValue.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.zValue)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.pagesWidget = QStackedWidget(self.gridLayoutWidget)
        self.pagesWidget.setObjectName(u"pagesWidget")
        self.pagesWidget.setEnabled(True)
        self.pagesWidget.setMinimumSize(QSize(600, 600))
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.homeMap = QWidget(self.HomePage)
        self.homeMap.setObjectName(u"homeMap")
        self.homeMap.setGeometry(QRect(0, 0, 600, 600))
        self.pagesWidget.addWidget(self.HomePage)
        self.TrackingPage = QWidget()
        self.TrackingPage.setObjectName(u"TrackingPage")
        self.pagesWidget.addWidget(self.TrackingPage)
        self.DataPage = QWidget()
        self.DataPage.setObjectName(u"DataPage")
        self.pagesWidget.addWidget(self.DataPage)

        self.gridLayout.addWidget(self.pagesWidget, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pagesWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.calibrationButton.setText(QCoreApplication.translate("MainWindow", u"Calibartion", None))
        self.trackingButton.setText(QCoreApplication.translate("MainWindow", u"Tracking", None))
        self.dataButton.setText(QCoreApplication.translate("MainWindow", u"Recorded Data", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.xLabel.setText(QCoreApplication.translate("MainWindow", u"X: ", None))
        self.yLabel.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.zLabel.setText(QCoreApplication.translate("MainWindow", u"Z: ", None))
    # retranslateUi

