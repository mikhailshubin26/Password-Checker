from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class SupportItem(QWidget):
    def __init__(self, name, address, qr_image_path, toggle_callback):
        super().__init__()
        self.name = name
        self.expanded = False
        self.toggle_callback = toggle_callback  # метод родителя

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.btn = QPushButton(name)
        self.btn.setCheckable(True)
        self.btn.clicked.connect(self.on_clicked)

        self.content = QWidget()
        content_layout = QHBoxLayout(self.content)

        self.qr_label = QLabel()
        self.qr_label.setPixmap(QPixmap(qr_image_path).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.qr_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.addr_label = QLabel(address)
        self.addr_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.addr_label.setStyleSheet("padding-left: 15px; font-weight: bold; color: #E0E7FF;")

        content_layout.addWidget(self.qr_label)
        content_layout.addWidget(self.addr_label)
        self.content.setVisible(False)

        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.content)

    def on_clicked(self):
        self.toggle_callback(self)

    def expand(self):
        self.expanded = True
        self.content.setVisible(True)
        self.btn.setChecked(True)

    def collapse(self):
        self.expanded = False
        self.content.setVisible(False)
        self.btn.setChecked(False)


class SupportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поддержать проект")
        self.setFixedSize(600, 400)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.items = []

        cryptos = [
            ("BTC", "bc1qllfd0zxmk45j3x53d5dnu9y0ls7vdx60yyk3u4", "img/btc_qr.png"),
            ("ETH", "0x480468BbB77ef4a4abed20e81656e4CFBcc1C055", "img/eth_qr.png"),
            ("USDT", "TVrv9eQp4cvQ71NhE2uypCksjR9qQZBHcZ", "img/usdt_qr.png"),
        ]

        for name, addr, qr_path in cryptos:
            item = SupportItem(name, addr, qr_path, self.toggle_item)
            layout.addWidget(item)
            self.items.append(item)

        layout.addStretch()

    def toggle_item(self, clicked_item):
        for item in self.items:
            if item is clicked_item:
                if item.expanded:
                    item.collapse()
                else:
                    item.expand()
            else:
                item.collapse()
