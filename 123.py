import sys
from random import choice
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QTextEdit
)

answers = [
    'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
    'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
    'Хорошие перспективы', 'Знаки говорят - да', 'Да',
    'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
    'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
    'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
    'Перспективы не очень хорошие', 'Весьма сомнительно'
]

class MagicBallApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Магический Шар')
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Как тебя зовут?')
        layout.addWidget(self.name_input)

        self.greet_label = QLabel('', self)
        layout.addWidget(self.greet_label)

        self.question_input = QTextEdit(self)
        self.question_input.setPlaceholderText('Задай свой вопрос...')
        layout.addWidget(self.question_input)

        self.answer_label = QLabel('', self)
        layout.addWidget(self.answer_label)

        self.ask_button = QPushButton('Спросить', self)
        self.ask_button.clicked.connect(self.get_answer)
        layout.addWidget(self.ask_button)

        self.setLayout(layout)

    def get_answer(self):
        name = self.name_input.text().strip()
        if name:
            self.greet_label.setText(f'Привет, {name}.')
        else:
            self.greet_label.setText('Привет, незнакомец.')

        question = self.question_input.toPlainText().strip()
        if question:
            self.answer_label.setText(choice(answers))
        else:
            self.answer_label.setText('Пожалуйста, задай вопрос.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MagicBallApp()
    window.show()
    sys.exit(app.exec_())

