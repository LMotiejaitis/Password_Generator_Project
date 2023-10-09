# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordGenerator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QTextEdit, QWidget)

class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        if not PasswordGenerator.objectName():
            PasswordGenerator.setObjectName(u"PasswordGenerator")
        PasswordGenerator.resize(387, 555)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PasswordGenerator.sizePolicy().hasHeightForWidth())
        PasswordGenerator.setSizePolicy(sizePolicy)
        PasswordGenerator.setMinimumSize(QSize(387, 555))
        PasswordGenerator.setMaximumSize(QSize(500, 1000))
        PasswordGenerator.setAnimated(True)
        self.centralwidget = QWidget(PasswordGenerator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.amount_input_slider = QSlider(self.centralwidget)
        self.amount_input_slider.setObjectName(u"amount_input_slider")
        self.amount_input_slider.setGeometry(QRect(90, 40, 160, 22))
        self.amount_input_slider.setMinimum(1)
        self.amount_input_slider.setMaximum(25)
        self.amount_input_slider.setOrientation(Qt.Horizontal)
        self.length_input_slider = QSlider(self.centralwidget)
        self.length_input_slider.setObjectName(u"length_input_slider")
        self.length_input_slider.setGeometry(QRect(90, 110, 160, 22))
        self.length_input_slider.setMinimum(6)
        self.length_input_slider.setMaximum(25)
        self.length_input_slider.setOrientation(Qt.Horizontal)
        self.amount_label = QLabel(self.centralwidget)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(10, 20, 61, 41))
        self.length_label = QLabel(self.centralwidget)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setGeometry(QRect(10, 90, 61, 41))
        self.amount_input = QLineEdit(self.centralwidget)
        self.amount_input.setObjectName(u"amount_input")
        self.amount_input.setGeometry(QRect(140, 10, 41, 21))
        self.length_input = QLineEdit(self.centralwidget)
        self.length_input.setObjectName(u"length_input")
        self.length_input.setGeometry(QRect(140, 80, 41, 21))
        self.h_line_1 = QFrame(self.centralwidget)
        self.h_line_1.setObjectName(u"h_line_1")
        self.h_line_1.setGeometry(QRect(0, 60, 291, 21))
        self.h_line_1.setFrameShape(QFrame.HLine)
        self.h_line_1.setFrameShadow(QFrame.Sunken)
        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setGeometry(QRect(90, 160, 111, 41))
        self.h_line_2 = QFrame(self.centralwidget)
        self.h_line_2.setObjectName(u"h_line_2")
        self.h_line_2.setGeometry(QRect(0, 140, 291, 21))
        self.h_line_2.setFrameShape(QFrame.HLine)
        self.h_line_2.setFrameShadow(QFrame.Sunken)
        self.passwords_output = QTextEdit(self.centralwidget)
        self.passwords_output.setObjectName(u"passwords_output")
        self.passwords_output.setGeometry(QRect(0, 210, 291, 301))
        font = QFont()
        font.setPointSize(10)
        self.passwords_output.setFont(font)
        self.passwords_output.setReadOnly(True)
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(210, 520, 81, 31))
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(130, 520, 81, 31))
        self.v_line_1 = QFrame(self.centralwidget)
        self.v_line_1.setObjectName(u"v_line_1")
        self.v_line_1.setGeometry(QRect(280, 0, 20, 551))
        self.v_line_1.setFrameShape(QFrame.VLine)
        self.v_line_1.setFrameShadow(QFrame.Sunken)
        self.addons_label = QLabel(self.centralwidget)
        self.addons_label.setObjectName(u"addons_label")
        self.addons_label.setGeometry(QRect(320, 10, 51, 41))
        PasswordGenerator.setCentralWidget(self.centralwidget)

        self.retranslateUi(PasswordGenerator)

        QMetaObject.connectSlotsByName(PasswordGenerator)
    # setupUi

    def retranslateUi(self, PasswordGenerator):
        PasswordGenerator.setWindowTitle(QCoreApplication.translate("PasswordGenerator", u"MainWindow", None))
        self.amount_label.setText(QCoreApplication.translate("PasswordGenerator", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Amount</span></p></body></html>", None))
        self.length_label.setText(QCoreApplication.translate("PasswordGenerator", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Length</span></p></body></html>", None))
        self.generate_button.setText(QCoreApplication.translate("PasswordGenerator", u"Generate", None))
        self.exit_button.setText(QCoreApplication.translate("PasswordGenerator", u"Exit", None))
        self.clear_button.setText(QCoreApplication.translate("PasswordGenerator", u"Clear", None))
        self.addons_label.setText(QCoreApplication.translate("PasswordGenerator", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Addons</span></p></body></html>", None))
    # retranslateUi

