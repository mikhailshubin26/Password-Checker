import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtGui import QIcon, QAction, QFont, QPixmap
from PySide6.QtCore import Qt, QTimer
from ui_window import Ui_MainWindow
from check import checker

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):  # PyInstaller запаковывает всё в _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(resource_path("icon.ico")))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("""
    QMainWindow {
        background-color: #121B26;
    }
    QLabel {
        color: #E0E7FF;
        font-size: 14pt;
        font-weight: bold;
    }
    QPushButton {
        background-color: #2563EB;
        color: white;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #3B82F6;
    }
    QPushButton:pressed {
        background-color: #1D4ED8;
    }
    QLineEdit {
        background-color: #3B82F6;
        border: 2px solid #2563EB;
        border-radius: 6px;
        color: #E0E7FF;
        padding: 4px;
    }
""")


        self.password_visible=False

        self.toggle_action=QAction(self)
        self.toggle_action.setIcon(QIcon(resource_path("img/hide_password.png")))
        self.toggle_action.triggered.connect(self.toggle_password)

        self.font_default = self.ui.lineEditPassword.font()
        self.mono_font=QFont("Courier New")

        self.mono_font.setBold(True)

        self.mono_font.setStyleHint(QFont.StyleHint.Monospace)
        self.mono_font.setPointSize(18)

        self.ui.lineEditPassword.setPlaceholderText("Пароль")

        self.ui.lineEditPassword.addAction(
    		self.toggle_action, QLineEdit.ActionPosition.TrailingPosition
    	)

        self.ui.pushButtonCheck.clicked.connect(self.check_password)

        self.default_color = "white"

        self.ui.labelLogo.setScaledContents(True)
        self.pixmap = QPixmap(resource_path("img/logo.png"))
        self.ui.labelLogo.setPixmap(self.pixmap)

    def toggle_password(self):
    	self.password_visible=not self.password_visible

    	if self.password_visible:
    		if self.ui.lineEditPassword.text():
	    		self.ui.lineEditPassword.setFont(self.mono_font)
	    	self.ui.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Normal)
    		self.toggle_action.setIcon(QIcon(resource_path("img/show_password.png")))
    	else:
    		self.ui.lineEditPassword.setFont(self.font_default)
    		self.ui.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)
    		self.toggle_action.setIcon(QIcon(resource_path("img/hide_password.png")))

    def check_password(self):
        self.ui.labelResults.setStyleSheet(f"color: {self.default_color};")
        password=self.ui.lineEditPassword.text()
        if password:
            self.ui.labelResults.setText('Проверка...')
            QTimer.singleShot(300, lambda: self.finish_check(password))
        else:
        	self.ui.labelResults.setText('Введите пароль')

    def finish_check(self, password):
        result = checker(password)
        self.ui.labelResults.setStyleSheet(f"color: {result[1]};")
        self.ui.labelResults.setText(result[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Password Checker")  # заголовок окна
    window.show()
    sys.exit(app.exec())