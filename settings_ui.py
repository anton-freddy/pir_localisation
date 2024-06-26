# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(800, 500)
        Settings.setMinimumSize(QSize(800, 500))
        Settings.setMaximumSize(QSize(800, 500))
        self.centralwidget = QWidget(Settings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.Calibration_Tab = QWidget()
        self.Calibration_Tab.setObjectName(u"Calibration_Tab")
        self.gridLayout_3 = QGridLayout(self.Calibration_Tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cali_points = QTableWidget(self.Calibration_Tab)
        if (self.cali_points.columnCount() < 3):
            self.cali_points.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.cali_points.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cali_points.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cali_points.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.cali_points.rowCount() < 9):
            self.cali_points.setRowCount(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cali_points.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cali_points.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cali_points.setItem(0, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cali_points.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.cali_points.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.cali_points.setItem(1, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.cali_points.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.cali_points.setItem(2, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.cali_points.setItem(2, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.cali_points.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.cali_points.setItem(3, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.cali_points.setItem(3, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.cali_points.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.cali_points.setItem(4, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.cali_points.setItem(4, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.cali_points.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.cali_points.setItem(5, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.cali_points.setItem(5, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.cali_points.setItem(6, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.cali_points.setItem(6, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.cali_points.setItem(6, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.cali_points.setItem(7, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.cali_points.setItem(7, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.cali_points.setItem(7, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.cali_points.setItem(8, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.cali_points.setItem(8, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.cali_points.setItem(8, 2, __qtablewidgetitem29)
        self.cali_points.setObjectName(u"cali_points")
        self.cali_points.setInputMethodHints(Qt.ImhNone)
        self.cali_points.setAlternatingRowColors(True)
        self.cali_points.setShowGrid(True)
        self.cali_points.setSortingEnabled(True)
        self.cali_points.setRowCount(9)
        self.cali_points.setColumnCount(3)
        self.cali_points.horizontalHeader().setVisible(True)
        self.cali_points.verticalHeader().setVisible(False)
        self.cali_points.verticalHeader().setHighlightSections(True)

        self.gridLayout_3.addWidget(self.cali_points, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.Calibration_Tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.y_min = QLineEdit(self.frame_2)
        self.y_min.setObjectName(u"y_min")

        self.gridLayout_4.addWidget(self.y_min, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.y_max = QLineEdit(self.frame_2)
        self.y_max.setObjectName(u"y_max")

        self.gridLayout_4.addWidget(self.y_max, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.x_min = QLineEdit(self.frame_4)
        self.x_min.setObjectName(u"x_min")
        self.x_min.setInputMethodHints(Qt.ImhNone)
        self.x_min.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.x_min, 0, 1, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.x_max = QLineEdit(self.frame_4)
        self.x_max.setObjectName(u"x_max")

        self.gridLayout_6.addWidget(self.x_max, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_3, 0, 2, 1, 1)

        self.tabWidget.addTab(self.Calibration_Tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.exit_button = QPushButton(self.frame)
        self.exit_button.setObjectName(u"exit_button")

        self.gridLayout_2.addWidget(self.exit_button, 0, 0, 1, 1)

        self.save_and_exit_button = QPushButton(self.frame)
        self.save_and_exit_button.setObjectName(u"save_and_exit_button")

        self.gridLayout_2.addWidget(self.save_and_exit_button, 0, 1, 1, 1)

        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")

        self.gridLayout_2.addWidget(self.save_button, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Settings", u"General", None))
        ___qtablewidgetitem = self.cali_points.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Settings", u"X Pos", None));
        ___qtablewidgetitem1 = self.cali_points.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Settings", u"Y Pos", None));
        ___qtablewidgetitem2 = self.cali_points.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Settings", u"Z Pos", None));

        __sortingEnabled = self.cali_points.isSortingEnabled()
        self.cali_points.setSortingEnabled(False)
        self.cali_points.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("Settings", u"Y min", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"Y max", None))
        self.label.setText(QCoreApplication.translate("Settings", u"X min", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"X max", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Calibration_Tab), QCoreApplication.translate("Settings", u"Calibration", None))
        self.exit_button.setText(QCoreApplication.translate("Settings", u"Exit", None))
        self.save_and_exit_button.setText(QCoreApplication.translate("Settings", u"Save and Exit", None))
        self.save_button.setText(QCoreApplication.translate("Settings", u"Save Changes", None))
    # retranslateUi

