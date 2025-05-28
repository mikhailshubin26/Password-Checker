import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget
from PySide6.QtGui import QIcon, QAction, QFont, QPixmap
from PySide6.QtCore import Qt, QTimer
from ui_window import Ui_MainWindow
from ui_faq_window import Ui_Form
from faq_window import FAQWindow
from support_window import SupportWindow
from check import checker

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # Запуск из PyInstaller
        base_path = sys._MEIPASS
    else:
        # Запуск из исходников
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(resource_path("icon.ico")))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        self.ui.pushButtonFAQ.clicked.connect(self.show_faq)
        self.faq_window = None

        self.ui.pushButtonSupport.clicked.connect(self.show_support)
        self.support_window = None

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

    def show_faq(self):
        if self.faq_window is None:
            self.faq_window = FAQWindow()
        self.faq_window.show()
        self.faq_window.raise_()
        self.faq_window.activateWindow()

    def show_support(self):
        if self.support_window is None:
            self.support_window=SupportWindow()
        self.support_window.show()
        self.support_window.raise_()
        self.support_window.activateWindow()

class FaqWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    def load_stylesheet(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    app = QApplication(sys.argv)
    app.setStyleSheet(load_stylesheet(resource_path("style.qss")))
    window = MainWindow()
    window.setWindowTitle("Password Checker")  # заголовок окна
    window.show()
    sys.exit(app.exec())