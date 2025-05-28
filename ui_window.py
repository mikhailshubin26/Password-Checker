# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QSize(640, 480))
        MainWindow.setMaximumSize(QSize(640, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEditPassword = QLineEdit(self.centralwidget)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setGeometry(QRect(50, 170, 540, 51))
        self.lineEditPassword.setMinimumSize(QSize(540, 0))
        self.lineEditPassword.setMaximumSize(QSize(540, 16777215))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(18)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setFrame(True)
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.lineEditPassword.setCursorPosition(0)
        self.lineEditPassword.setDragEnabled(False)
        self.lineEditPassword.setReadOnly(False)
        self.lineEditPassword.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 450, 81, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.pushButtonCheck = QPushButton(self.centralwidget)
        self.pushButtonCheck.setObjectName(u"pushButtonCheck")
        self.pushButtonCheck.setGeometry(QRect(220, 240, 191, 51))
        font2 = QFont()
        font2.setPointSize(18)
        self.pushButtonCheck.setFont(font2)
        self.labelResults = QLabel(self.centralwidget)
        self.labelResults.setObjectName(u"labelResults")
        self.labelResults.setGeometry(QRect(60, 300, 531, 51))
        self.labelResults.setFont(font2)
        self.labelResults.setLayoutDirection(Qt.LeftToRight)
        self.labelResults.setAlignment(Qt.AlignCenter)
        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(180, 40, 271, 101))
        self.labelLogo.setPixmap(QPixmap(u"img/logo.png"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1.0.0", None))
        self.pushButtonCheck.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.labelResults.setText("")
        self.labelLogo.setText("")
    # retranslateUi

