from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSizePolicy
from PySide6.QtCore import Qt

class FAQItem(QWidget):
    def __init__(self, question, answer, toggle_callback):
        super().__init__()
        self.answer_visible = False
        self.toggle_callback = toggle_callback  # Ссылка на метод FAQWindow для управления

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # Кнопка вопроса
        self.btn_question = QPushButton("▶ " + question)
        self.btn_question.setCheckable(True)
        self.btn_question.setStyleSheet("text-align: left;")
        self.btn_question.clicked.connect(self.toggle_answer)

        self.label_answer = QLabel(answer)
        self.label_answer.setWordWrap(True)
        self.label_answer.setVisible(False)
        self.label_answer.setStyleSheet("padding-left: 20px; color: #c0c0c0;")

        self.layout.addWidget(self.btn_question)
        self.layout.addWidget(self.label_answer)

    def toggle_answer(self):
        self.toggle_callback(self)  # Сообщить FAQWindow, что по этой кнопке кликнули

    def expand(self):
        self.answer_visible = True
        self.label_answer.setVisible(True)
        self.btn_question.setText("▼ " + self.btn_question.text()[2:])

    def collapse(self):
        self.answer_visible = False
        self.label_answer.setVisible(False)
        self.btn_question.setText("▶ " + self.btn_question.text()[2:])


class FAQWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FAQ — Часто задаваемые вопросы")
        self.setFixedSize(500, 400)  # Фиксированное окно

        self.items = []

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        faqs = [
            ("Передаются ли введённые пароли куда-то по интернету?",
                "Нет, программа проверяет пароли локально и не отправляет их на серверы или третьим лицам."),
            ("Сохраняются ли мои пароли в программе?",
                "Программа не сохраняет введённые пароли ни на диске, ни в облаке — все данные обрабатываются только во время работы."),
            ("Как обеспечивается безопасность программы?",
                "Все операции с паролями происходят локально, без подключения к сети. Исходный код открыт и не содержит шпионских функций."),
            ("Можно ли использовать эту программу для своих проектов?",
                "Да, вы можете использовать программу и её код в своих проектах. Если хотите, можете внести улучшения и поделиться ими с сообществом.")
        ]

        for q, a in faqs:
            item = FAQItem(q, a, self.toggle_item)
            self.items.append(item)
            layout.addWidget(item)

        layout.addStretch()

    def toggle_item(self, clicked_item):
        for item in self.items:
            if item is clicked_item:
                if item.answer_visible:
                    item.collapse()
                else:
                    item.expand()
            else:
                item.collapse()
