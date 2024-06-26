# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalibrationWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_Calibration(object):
    def setupUi(self, Calibration):
        if not Calibration.objectName():
            Calibration.setObjectName(u"Calibration")
        Calibration.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calibration.sizePolicy().hasHeightForWidth())
        Calibration.setSizePolicy(sizePolicy)
        Calibration.setMinimumSize(QSize(600, 400))
        Calibration.setMaximumSize(QSize(600, 400))
        self.centralwidget = QWidget(Calibration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphFrame = QFrame(self.centralwidget)
        self.graphFrame.setObjectName(u"graphFrame")
        self.graphFrame.setMinimumSize(QSize(382, 382))
        self.graphFrame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.graphFrame.setFrameShape(QFrame.StyledPanel)
        self.graphFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.graphFrame, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.yFrame = QFrame(self.centralwidget)
        self.yFrame.setObjectName(u"yFrame")
        self.yFrame.setFrameShape(QFrame.StyledPanel)
        self.yFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.yFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.yLabel = QLabel(self.yFrame)
        self.yLabel.setObjectName(u"yLabel")

        self.gridLayout_5.addWidget(self.yLabel, 0, 0, 1, 1)

        self.yValue = QLineEdit(self.yFrame)
        self.yValue.setObjectName(u"yValue")
        self.yValue.setAcceptDrops(False)
        self.yValue.setFrame(True)
        self.yValue.setReadOnly(True)

        self.gridLayout_5.addWidget(self.yValue, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.yFrame, 4, 0, 1, 1)

        self.nextPointButton = QPushButton(self.centralwidget)
        self.nextPointButton.setObjectName(u"nextPointButton")

        self.gridLayout_2.addWidget(self.nextPointButton, 1, 0, 1, 1)

        self.recordPointButton = QPushButton(self.centralwidget)
        self.recordPointButton.setObjectName(u"recordPointButton")

        self.gridLayout_2.addWidget(self.recordPointButton, 0, 0, 1, 1)

        self.saveAbortFrame = QFrame(self.centralwidget)
        self.saveAbortFrame.setObjectName(u"saveAbortFrame")
        self.saveAbortFrame.setFrameShape(QFrame.StyledPanel)
        self.saveAbortFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.saveAbortFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.saveAndExitButton = QPushButton(self.saveAbortFrame)
        self.saveAndExitButton.setObjectName(u"saveAndExitButton")

        self.gridLayout_7.addWidget(self.saveAndExitButton, 0, 1, 1, 1)

        self.abortButton = QPushButton(self.saveAbortFrame)
        self.abortButton.setObjectName(u"abortButton")

        self.gridLayout_7.addWidget(self.abortButton, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.saveAbortFrame, 6, 0, 1, 1)

        self.currentPointFrame = QFrame(self.centralwidget)
        self.currentPointFrame.setObjectName(u"currentPointFrame")
        self.currentPointFrame.setFrameShape(QFrame.StyledPanel)
        self.currentPointFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.currentPointFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.currentPointValue = QLineEdit(self.currentPointFrame)
        self.currentPointValue.setObjectName(u"currentPointValue")
        self.currentPointValue.setAcceptDrops(False)
        self.currentPointValue.setFrame(True)
        self.currentPointValue.setReadOnly(True)

        self.gridLayout_3.addWidget(self.currentPointValue, 0, 1, 1, 1)

        self.currentPointLabel = QLabel(self.currentPointFrame)
        self.currentPointLabel.setObjectName(u"currentPointLabel")

        self.gridLayout_3.addWidget(self.currentPointLabel, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.currentPointFrame, 2, 0, 1, 1)

        self.zFrame = QFrame(self.centralwidget)
        self.zFrame.setObjectName(u"zFrame")
        self.zFrame.setFrameShape(QFrame.StyledPanel)
        self.zFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.zFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.zValue = QLineEdit(self.zFrame)
        self.zValue.setObjectName(u"zValue")
        self.zValue.setAcceptDrops(False)
        self.zValue.setFrame(True)
        self.zValue.setReadOnly(True)

        self.gridLayout_6.addWidget(self.zValue, 0, 1, 1, 1)

        self.zLabel = QLabel(self.zFrame)
        self.zLabel.setObjectName(u"zLabel")

        self.gridLayout_6.addWidget(self.zLabel, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.zFrame, 5, 0, 1, 1)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")

        self.gridLayout_2.addWidget(self.settingsButton, 7, 0, 1, 1)

        self.xFrame = QFrame(self.centralwidget)
        self.xFrame.setObjectName(u"xFrame")
        self.xFrame.setFrameShape(QFrame.StyledPanel)
        self.xFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.xFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.xLabel = QLabel(self.xFrame)
        self.xLabel.setObjectName(u"xLabel")

        self.gridLayout_4.addWidget(self.xLabel, 0, 0, 1, 1)

        self.xValue = QLineEdit(self.xFrame)
        self.xValue.setObjectName(u"xValue")
        self.xValue.setAcceptDrops(False)
        self.xValue.setFrame(True)
        self.xValue.setReadOnly(True)

        self.gridLayout_4.addWidget(self.xValue, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.xFrame, 3, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 3, 1, 1)

        Calibration.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calibration)

        QMetaObject.connectSlotsByName(Calibration)
    # setupUi

    def retranslateUi(self, Calibration):
        Calibration.setWindowTitle(QCoreApplication.translate("Calibration", u"MainWindow", None))
        self.yLabel.setText(QCoreApplication.translate("Calibration", u"Recorded Y", None))
        self.nextPointButton.setText(QCoreApplication.translate("Calibration", u"Select Next point", None))
        self.recordPointButton.setText(QCoreApplication.translate("Calibration", u"Record Point", None))
        self.saveAndExitButton.setText(QCoreApplication.translate("Calibration", u"Save and Exit", None))
        self.abortButton.setText(QCoreApplication.translate("Calibration", u"Abort", None))
        self.currentPointLabel.setText(QCoreApplication.translate("Calibration", u"Current Point", None))
        self.zLabel.setText(QCoreApplication.translate("Calibration", u"Recorded Z", None))
        self.settingsButton.setText(QCoreApplication.translate("Calibration", u"Settings", None))
        self.xLabel.setText(QCoreApplication.translate("Calibration", u"Recorded X", None))
    # retranslateUi

