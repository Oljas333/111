import sys
from random import choice, randint
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QTextEdit, QMessageBox
)

class GuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Игра "Угадай число"')
        self.setGeometry(100, 100, 500, 400)
        self.initUI()

        self.num_to_guess = None
        self.count = 0

    def initUI(self):
        layout = QVBoxLayout()

        self.rules = QLabel('Добро пожаловать в игру "Угадай число"!\nВведи границы диапазона и попробуй угадать число.')
        layout.addWidget(self.rules)

        hlayout_range = QHBoxLayout()
        self.input_x = QLineEdit()
        self.input_x.setPlaceholderText('Первая граница')
        self.input_y = QLineEdit()
        self.input_y.setPlaceholderText('Вторая граница')
        self.set_range_button = QPushButton('Задать диапазон')
        self.set_range_button.clicked.connect(self.set_range)
        hlayout_range.addWidget(self.input_x)
        hlayout_range.addWidget(self.input_y)
        hlayout_range.addWidget(self.set_range_button)
        layout.addLayout(hlayout_range)

        self.guess_input = QLineEdit()
        self.guess_input.setPlaceholderText('Твоя попытка')
        layout.addWidget(self.guess_input)

        self.guess_button = QPushButton('Проверить')
        self.guess_button.clicked.connect(self.check_guess)
        layout.addWidget(self.guess_button)

        self.feedback = QLabel('')
        layout.addWidget(self.feedback)

        self.restart_button = QPushButton('Сыграть заново')
        self.restart_button.clicked.connect(self.restart_game)
        layout.addWidget(self.restart_button)

        self.setLayout(layout)

    def set_range(self):
        try:
            x = int(self.input_x.text())
            y = int(self.input_y.text())
            if x == y:
                self.feedback.setText('Границы не должны совпадать.')
                return
            if x > y:
                x, y = y, x
            self.num_to_guess = randint(x, y)
            self.count = 0
            self.feedback.setText(f'Я загадал число от {x} до {y}. Попробуй угадать!')
        except ValueError:
            self.feedback.setText('Введите корректные числа.')

    def check_guess(self):
        if self.num_to_guess is None:
            self.feedback.setText('Сначала задай диапазон.')
            return

        try:
            guess = int(self.guess_input.text())
        except ValueError:
            self.feedback.setText('Это не число.')
            return

        self.count += 1
        diff = abs(guess - self.num_to_guess)

        too_much = ['Многовато!', 'Бери ниже', 'Нужно меньшее число!']
        too_little = ['Маловато!', 'Бери выше', 'Нужно большее число!']
        almost = ['Ты близок!', 'Горячо!', 'Уже рядом!']
        guessed = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)']
        too_soon = ['Ого, так быстро!', 'Да ты волшебник!', 'Ты угадал слишком быстро!']

        if guess == self.num_to_guess:
            if self.count == 1:
                message = 'Скажи честно, ты подглядывал?'
            elif self.count <= 5:
                message = choice(too_soon)
            else:
                message = choice(guessed)
            self.feedback.setText(f'{message}\nПопыток: {self.count}')
        elif guess > self.num_to_guess:
            msg = choice(too_much)
            self.feedback.setText(f'{msg}\n{choice(almost) if diff < 5 else ""}')
        elif guess < self.num_to_guess:
            msg = choice(too_little)
            self.feedback.setText(f'{msg}\n{choice(almost) if diff < 5 else ""}')

    def restart_game(self):
        self.input_x.clear()
        self.input_y.clear()
        self.guess_input.clear()
        self.feedback.setText('')
        self.num_to_guess = None
        self.count = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GuessingGame()
    game.show()
    sys.exit(app.exec_())
