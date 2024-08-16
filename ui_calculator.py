# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(387, 657)
        Calculator.setBaseSize(QSize(300, 450))
        Calculator.setStyleSheet(u"background-color:black;")
        self.main_label2 = QLabel(Calculator)
        self.main_label2.setObjectName(u"main_label2")
        self.main_label2.setGeometry(QRect(10, 20, 371, 61))
        font = QFont()
        font.setPointSize(16)
        self.main_label2.setFont(font)
        self.main_label2.setStyleSheet(u"color:white;")
        self.main_label2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.main_label = QLabel(Calculator)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setGeometry(QRect(10, 100, 371, 81))
        font1 = QFont()
        font1.setPointSize(35)
        self.main_label.setFont(font1)
        self.main_label.setStyleSheet(u"color:white;")
        self.main_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(Calculator)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 190, 371, 461))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")
        font2 = QFont()
        font2.setPointSize(30)
        self.btn_2.setFont(font2)
        self.btn_2.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_2, 4, 2, 1, 1)

        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFont(font2)
        self.btn_1.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_1, 4, 3, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFont(font2)
        self.btn_4.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_4, 3, 3, 1, 1)

        self.btn_0 = QPushButton(self.gridLayoutWidget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFont(font2)
        self.btn_0.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_0, 5, 1, 1, 2)

        self.btn_min = QPushButton(self.gridLayoutWidget)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setFont(font2)
        self.btn_min.setStyleSheet(u"color:white;\n"
"background-color:#EEA10C;\n"
"border-radius:50px;\n"
"")

        self.gridLayout.addWidget(self.btn_min, 3, 4, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFont(font2)
        self.btn_3.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_3, 4, 1, 1, 1)

        self.btn_plus = QPushButton(self.gridLayoutWidget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setFont(font2)
        self.btn_plus.setStyleSheet(u"color:white;\n"
"background-color:#EEA10C;\n"
"border-radius:50px;\n"
"")

        self.gridLayout.addWidget(self.btn_plus, 4, 4, 1, 1)

        self.btn_mul = QPushButton(self.gridLayoutWidget)
        self.btn_mul.setObjectName(u"btn_mul")
        self.btn_mul.setFont(font2)
        self.btn_mul.setStyleSheet(u"color:white;\n"
"background-color:#EEA10C;\n"
"border-radius:50px;\n"
"")

        self.gridLayout.addWidget(self.btn_mul, 2, 4, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setFont(font2)
        self.btn_8.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_8, 2, 2, 1, 1)

        self.btn_dot = QPushButton(self.gridLayoutWidget)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setFont(font2)
        self.btn_dot.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_dot, 5, 3, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setFont(font2)
        self.btn_7.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_7, 2, 3, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFont(font2)
        self.btn_9.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_9, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFont(font2)
        self.btn_6.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_6, 3, 1, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFont(font2)
        self.btn_5.setStyleSheet(u"color:white;\n"
"background-color:#2A322E;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_5, 3, 2, 1, 1)

        self.btn_div = QPushButton(self.gridLayoutWidget)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setFont(font2)
        self.btn_div.setStyleSheet(u"color:white;\n"
"background-color:#EEA10C;\n"
"border-radius:50px;\n"
"")

        self.gridLayout.addWidget(self.btn_div, 5, 4, 1, 1)

        self.btn_equals = QPushButton(self.gridLayoutWidget)
        self.btn_equals.setObjectName(u"btn_equals")
        self.btn_equals.setFont(font2)
        self.btn_equals.setStyleSheet(u"color:black;\n"
"background-color:white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_equals, 6, 3, 1, 2)

        self.btn_c = QPushButton(self.gridLayoutWidget)
        self.btn_c.setObjectName(u"btn_c")
        self.btn_c.setFont(font2)
        self.btn_c.setStyleSheet(u"color:black;\n"
"background-color:white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_c, 6, 1, 1, 2)


        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Form", None))
        self.main_label2.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.main_label.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.btn_2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.btn_1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.btn_4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.btn_0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.btn_min.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.btn_3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.btn_plus.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.btn_mul.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.btn_8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.btn_dot.setText(QCoreApplication.translate("Calculator", u".", None))
        self.btn_7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.btn_9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.btn_6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.btn_5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.btn_div.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.btn_equals.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.btn_c.setText(QCoreApplication.translate("Calculator", u"C", None))
    # retranslateUi

