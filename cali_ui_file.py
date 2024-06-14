# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalibrationPopUp.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_CalibrationWindow(object):
    def setupUi(self, CalibrationWindow):
        if not CalibrationWindow.objectName():
            CalibrationWindow.setObjectName(u"CalibrationWindow")
        CalibrationWindow.resize(800, 600)
        self.centralwidget = QWidget(CalibrationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 280, 201, 20))
        CalibrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CalibrationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        CalibrationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CalibrationWindow)
        self.statusbar.setObjectName(u"statusbar")
        CalibrationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CalibrationWindow)

        QMetaObject.connectSlotsByName(CalibrationWindow)
    # setupUi

    def retranslateUi(self, CalibrationWindow):
        CalibrationWindow.setWindowTitle(QCoreApplication.translate("CalibrationWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("CalibrationWindow", u"Calibration window", None))
    # retranslateUi

