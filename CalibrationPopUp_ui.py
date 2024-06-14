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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
    QWidget)

class Ui_CalibrationWindow(object):
    def setupUi(self, CalibrationWindow):
        if not CalibrationWindow.objectName():
            CalibrationWindow.setObjectName(u"CalibrationWindow")
        CalibrationWindow.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalibrationWindow.sizePolicy().hasHeightForWidth())
        CalibrationWindow.setSizePolicy(sizePolicy)
        CalibrationWindow.setMinimumSize(QSize(600, 400))
        CalibrationWindow.setMaximumSize(QSize(600, 400))
        self.centralwidget = QWidget(CalibrationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        CalibrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CalibrationWindow)

        QMetaObject.connectSlotsByName(CalibrationWindow)
    # setupUi

    def retranslateUi(self, CalibrationWindow):
        CalibrationWindow.setWindowTitle(QCoreApplication.translate("CalibrationWindow", u"MainWindow", None))
    # retranslateUi

