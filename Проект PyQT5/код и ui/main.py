import sys

from PyQt5 import uic
from random import shuffle
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *

poss1, poss2, poss3, poss4, poss5, poss6 = [], [], [], [], [], []  # списки со всеми квадратами
poss_for_check1, poss_for_check2, poss_for_check3 = [], [], []  # список со всеми квадратами
poss_for_check4, poss_for_check5, poss_for_check6 = [], [], []  # для проверки
a1, a2, a3, a4, a5, a6 = 5, 7, 9, 5, 7, 9  # количество задействованых квадратов
b1, b2, b3, b4, b5, b6 = 0, 0, 0, 0, 0, 0  # для времени на уровне
conde, condn, condh, conse, consn, consh = 0, 0, 0, 0, 0, 0  # для проверки нажатий начать
exp1, exp2, exp3, exp4, exp5, exp6 = 0, 0, 0, 0, 0, 0  # для подсчета уровня


class Menu(QWidget):  # окно меню
    def __init__(self):
        super().__init__()
        uic.loadUi('Menu.ui', self)
        self.textEdit.setReadOnly(True)
        [i.clicked.connect(self.run) for i in self.buttonGroup.buttons()]

    def run(self):  # основная функция
        if self.sender().text() == 'Цифры':  # возвращает в окно с выбором сложности
            self.close()
            self.digits = Digits()
            self.digits.show()
        if self.sender().text() == 'Квадраты':  # начинает игру
            self.close()
            self.squares = Squares()
            self.squares.show()
        if self.sender().text() == 'Правила':  # возвращает в окно с выбором сложности
            self.close()
            self.rules = Rules()
            self.rules.show()


class Rules(QWidget):  # окно с правилами
    def __init__(self):
        super().__init__()
        uic.loadUi('Rules.ui', self)
        self.textEdit.setReadOnly(True)
        [i.clicked.connect(self.run) for i in self.buttonGroup.buttons()]

    def run(self):  # основная функция
        if self.sender().text() == 'Назад':  # возвращает в окно с выбором сложности
            self.close()
            self.menu = Menu()
            self.menu.show()


class Digits(QWidget):  # окно режима выбора сложности для режима цифры
    def __init__(self):
        super().__init__()
        uic.loadUi('Digits.ui', self)
        self.textBrowser.setReadOnly(True)
        [i.clicked.connect(self.run) for i in self.buttonGroup.buttons()]

    def run(self):  # основная функция
        if self.sender().text() == 'Назад':  # возвращает в меню
            self.close()
            self.menu = Menu()
            self.menu.show()
        if self.sender().text() == 'Легко':  # переход в окно со сложностью легко
            self.close()
            self.digits_easy = Digits_Easy()
            self.digits_easy.show()
        if self.sender().text() == 'Нормально':  # переход в окно со сложностью нормально
            self.close()
            self.digits_norm = Digits_Norm()
            self.digits_norm.show()
        if self.sender().text() == 'Сложно':  # переход в окно со сложностью сложно
            self.close()
            self.digits_hard = Digits_Hard()
            self.digits_hard.show()


class Squares(QWidget):  # окно режима выбора сложности для режима квадраты
    def __init__(self):
        super().__init__()
        uic.loadUi('Squares.ui', self)
        self.textBrowser.setReadOnly(True)
        [i.clicked.connect(self.run) for i in self.buttonGroup.buttons()]

    def run(self):  # основная функция
        if self.sender().text() == 'Назад':  # возвращает в меню
            self.close()
            self.menu = Menu()
            self.menu.show()
        if self.sender().text() == 'Легко':  # переход в окно со сложностью легко
            self.close()
            self.squares_easy = Squares_Easy()
            self.squares_easy.show()
        if self.sender().text() == 'Нормально':  # переход в окно со сложностью нормально
            self.close()
            self.squares_norm = Squares_Norm()
            self.squares_norm.show()
        if self.sender().text() == 'Сложно':  # переход в окно со сложностью сложно
            self.close()
            self.squares_hard = Squares_Hard()
            self.squares_hard.show()


class Digits_Easy(QWidget):  # окно режима цифры со сложностью легко
    def __init__(self):
        super().__init__()
        uic.loadUi('Digits_Easy.ui', self)
        self.textEdit.setReadOnly(True)
        self.pushButton_back.clicked.connect(self.run)
        self.pushButton_run.clicked.connect(self.run)

    def run(self):  # основная функция
        global conde, poss_for_check1, b1, poss1
        poss1 = self.buttonGroup.buttons()
        for i in range(9):
            poss1[i].setText('')
        if self.sender().text() == 'Назад':  # возвращает в окно с выбором сложности
            conde = 0
            self.close()
            self.digits = Digits()
            self.digits.show()
        if self.sender().text() == 'Начать':  # начинает игру
            if conde < 1:
                shuffle(poss1)
                poss_for_check1 = []
                conde += 1
                self.random_in()
                self.num = 0
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.showTime)
                self.timer.start(1)
            else:
                self.showDialog()  # при повторном нажатии на кнопку начать открывает диалоговое окно

    def showTime(self):  # подсчитывает время и расставляет/убирает цифры
        global b1, exp1, a1, poss_for_check1, poss1
        self.label.setNum(self.num)
        self.num += 0.001
        if self.num == 1:
            for i in range(9):
                poss1[i].setText('')
        if self.num > 1 + b1 * 0.25:
            for i in range(exp1 + a1):
                poss_for_check1[i].setText((i + 1) * '1')
            self.check_in()

    def random_in(self):  # генерирует положение цифр
        global exp1, a1, poss_for_check1, poss1
        for i in range(exp1 + a1):
            poss1[i].setText(str(i + 1))
            poss_for_check1.append(poss1[i])

    def check_in(self):  # проверяет нажатые квадраты
        if exp1 <= 2:
            if b1 < exp1 + a1:
                if self.sender().text() == str((a1 + exp1) * '1'):
                    b1 += 1
                else:
                    self.showDialog_check()
            else:
                self.showDialog_win()
        else:
            self.showDialog_winwin()

    def showDialog_check(self):  # диалоговое окно с сообщением о поражении
        button = QMessageBox.question(self, "Поражение", "Начать заново？",
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.run()
        else:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog(self):  # диалоговое окно
        button = QMessageBox.question(self, "Начать заново？", "Уверенны?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.digits_easy = Digits_Easy()
            self.digits_easy.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog_win(self):  # диалоговое окно с сообщением о победе на уровне
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            exp1 += 1
            self.close()
            self.digits_easy = Digits_Easy()
            self.digits_easy.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog_winwin(self):  # диалоговое окно с сообщением о прохождение всех уровней
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.digits_easy = Digits_Easy()
            self.digits_easy.show()
        else:
            self.close()
            self.digits = Digits()
            self.digits.show()


class Digits_Norm(QWidget):  # окно режима цифры со сложностью нормально
    def __init__(self):
        super().__init__()
        uic.loadUi('Digits_Norm.ui', self)
        self.textEdit.setReadOnly(True)
        self.pushButton_back.clicked.connect(self.run)
        self.pushButton_run.clicked.connect(self.run)

    def run(self):  # основная функция
        global condn, poss_for_check2, b2, poss2
        poss2 = self.buttonGroup.buttons()
        for i in range(16):
            poss2[i].setText('')
        if self.sender().text() == 'Назад':  # возвращает в окно с выбором сложности
            condn = 0
            self.close()
            self.digits = Digits()
            self.digits.show()
        if self.sender().text() == 'Начать':  # начинает игру
            if condn < 1:
                shuffle(poss2)
                poss_for_check2 = []
                condn += 1
                self.random_in()
                self.num = 0
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.showTime)
                self.timer.start(1)
            else:
                self.showDialog()  # при повторном нажатии на кнопку начать открывает диалоговое окно

    def showTime(self):  # подсчитывает время и расставляет/убирает цифры
        global b2, exp2, a2, poss_for_check2, poss2
        self.label.setNum(self.num)
        self.num += 0.001
        if self.num == 1:
            for i in range(16):
                poss2[i].setText('')
        if self.num >= 1 + b2 * 0.25:
            for i in range(exp2 + a2):
                poss_for_check2[i].setText((i + 1) * '1')
            self.check_in()

    def random_in(self):  # генерирует положение цифр
        global exp2, a2, poss_for_check2, poss2
        for i in range(exp2 + a2):
            poss2[i].setText(str(i + 1))
            poss_for_check2.append(poss2[i])

    def check_in(self):  # проверяет нажатые квадраты

        if exp2 <= 3:
            if b2 < exp2 + a2:
                if self.sender().text() == str((a2 + exp2) * '1'):
                    b2 += 1
                else:
                    self.showDialog_check()
            else:
                self.showDialog_win()
        else:
            self.showDialog_winwin()

    def showDialog_check(self):

        button = QMessageBox.question(self, "Поражение", "Начать заново？",
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)

        if button == QMessageBox.Ok:
            self.run()
        else:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog(self):  # диалоговое окно

        button = QMessageBox.question(self, "Начать заново？", "Уверенны?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)

        if button == QMessageBox.Ok:
            self.close()
            self.digits_norm = Digits_Norm()
            self.digits_norm.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog_win(self):  # диалоговое окно

        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)

        if button == QMessageBox.Ok:
            exp2 += 2
            self.close()
            self.digits_norm = Digits_Norm()
            self.digits_norm.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog_winwin(self):  # диалоговое окно

        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)

        if button == QMessageBox.Ok:
            self.close()
            self.digits_norm = Digits_Norm()
            self.digits_norm.show()
        else:
            self.close()
            self.digits = Digits()
            self.digits.show()


class Digits_Hard(QWidget):  # окно режима цифры со сложностью сложно
    def __init__(self):
        super().__init__()
        uic.loadUi('Digits_Hard.ui', self)
        self.textEdit.setReadOnly(True)
        self.pushButton_back.clicked.connect(self.run)
        self.pushButton_run.clicked.connect(self.run)

    def run(self):  # основная функция
        global condh, poss_for_check3, b3, poss3
        poss3 = self.buttonGroup.buttons()
        for i in range(25):
            poss3[i].setText('')
        if self.sender().text() == 'Назад':  # возвращает в окно с выбором сложности
            condh = 0
            self.close()
            self.digits = Digits()
            self.digits.show()
        if self.sender().text() == 'Начать':  # начинает игру
            if condh < 1:
                shuffle(poss3)
                poss_for_check3 = []
                conde += 1
                self.random_in()
                self.num = 0
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.showTime)
                self.timer.start(1)
            else:
                self.showDialog()  # при повторном нажатии на кнопку начать открывает диалоговое окно

    def showTime(self):  # подсчитывает время и расставляет/убирает цифры
        global b3, exp3, a3, poss_for_check3, poss3
        self.label.setNum(self.num)
        self.num += 0.001
        if self.num == 1:
            for i in range(25):
                poss3[i].setText('')
        if self.num > 1 + b3 * 0.25:
            for i in range(exp3 + a3):
                poss_for_check3[i].setText((i + 1) * '1')
            self.check_in()

    def random_in(self):  # генерирует положение цифр
        global exp3, a3, poss_for_check1, poss1
        for i in range(exp3 + a3):
            poss3[i].setText(str(i + 1))
            poss_for_check3.append(poss3[i])

    def check_in(self):  # проверяет нажатые квадраты
        global exp3, b3, a3
        if exp3 <= 2:
            if b3 < exp3 + a3:
                if self.sender().text() == str((a3 + exp3) * '1'):
                    b3 += 1
                else:
                    self.showDialog_check()
            else:
                self.showDialog_win()
        else:
            self.showDialog_winwin()

    def showDialog_check(self):  # диалоговое окно с сообщением о поражении
        button = QMessageBox.question(self, "Поражение", "Начать заново？",
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.run()
        else:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog(self):  # диалоговое окно
        button = QMessageBox.question(self, "Начать заново？", "Уверенны?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.digits_hard = Digits_Hard()
            self.digits_hard.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog_win(self):  # диалоговое окно с сообщением о победе на уровне
        global exp3
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            exp3 += 1
            self.close()
            self.digits_hard = Digits_Hard()
            self.digits_hard.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.digits = Digits()
            self.digits.show()

    def showDialog_winwin(self):  # диалоговое окно с сообщением о прохождение всех уровней
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.digits_hard = Digits_Hard()
            self.digits_hard.show()
        else:
            self.close()
            self.digits = Digits()
            self.digits.show()


class Squares_Easy(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Squares_Easy.ui', self)
        self.textEdit.setReadOnly(True)
        self.pushButton_back.clicked.connect(self.run)
        self.pushButton_run.clicked.connect(self.run)

    def run(self):  # основная функция
        global conse, poss_for_check4, b4, poss4
        poss4 = self.buttonGroup.buttons()
        for i in range(9):
            poss4[i].setText('')
        if self.sender().text() == 'Назад':  # возвращает в окно с выбором сложности
            conse = 0
            self.close()
            self.digits = Digits()
            self.digits.show()
        if self.sender().text() == 'Начать':  # начинает игру
            if conse < 1:
                shuffle(poss4)
                poss_for_check4 = []
                conse += 1
                self.random_in()
                self.num = 0
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.showTime)
                self.timer.start(1)
            else:
                self.showDialog()  # при повторном нажатии на кнопку начать открывает диалоговое окно

    def showTime(self):  # подсчитывает время и расставляет/убирает цифры
        global b4, exp4, a4, poss_for_check4, poss4
        self.label.setNum(self.num)
        self.num += 0.001
        if self.num == 1:
            for i in range(9):
                poss4[i].setText('')
        if self.num > 1 + b4 * 0.25:
            for i in range(exp4 + a4):
                poss_for_check4[i].setText((i + 1) * '1')
            self.check_in()

    def random_in(self):  # генерирует положение цифр
        global exp4, a4, poss_for_check4, poss4
        for i in range(exp4 + a4):
            poss3[i].setText(str(i + 1))
            poss_for_check4.append(poss4[i])

    def check_in(self):  # проверяет нажатые квадраты
        global exp4, b4, a4
        if exp4 <= 2:
            if b4 < exp4 + a4:
                if self.sender().text() == str((a4 + exp4) * '1'):
                    b4 += 1
                else:
                    self.showDialog_check()
            else:
                self.showDialog_win()
        else:
            self.showDialog_winwin()

    def showDialog_check(self):  # диалоговое окно с сообщением о поражении
        button = QMessageBox.question(self, "Поражение", "Начать заново？",
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.run()
        else:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog(self):  # диалоговое окно
        button = QMessageBox.question(self, "Начать заново？", "Уверенны?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.squares_easy = Squares_Easy()
            self.squares_easy.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog_win(self):  # диалоговое окно с сообщением о победе на уровне
        global exp4
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            exp4 += 1
            self.close()
            self.squares_easy = Squares_Easy()
            self.squares_easy.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog_winwin(self):  # диалоговое окно с сообщением о прохождение всех уровней
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.squares_easy = Squares_Easy()
            self.squares_easy.show()
        else:
            self.close()
            self.squares = Squares()
            self.squares.show()


class Squares_Norm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Squares_Norm.ui', self)
        self.textEdit.setReadOnly(True)
        self.pushButton_back.clicked.connect(self.run)
        self.pushButton_run.clicked.connect(self.run)

    def run(self):  # основная функция
        global consn, poss_for_check5, b5, poss5
        poss5 = self.buttonGroup.buttons()
        for i in range(16):
            poss5[i].setText('')
        if self.sender().text() == 'Назад':  # возвращает в окно с выбором сложности
            consn = 0
            self.close()
            self.digits = Digits()
            self.digits.show()
        if self.sender().text() == 'Начать':  # начинает игру
            if consn < 1:
                shuffle(poss5)
                poss_for_check5 = []
                consn += 1
                self.random_in()
                self.num = 0
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.showTime)
                self.timer.start(1)
            else:
                self.showDialog()  # при повторном нажатии на кнопку начать открывает диалоговое окно

    def showTime(self):  # подсчитывает время и расставляет/убирает цифры
        global b5, exp5, a5, poss_for_check5, poss5
        self.label.setNum(self.num)
        self.num += 0.001
        if self.num == 1:
            for i in range(16):
                poss5[i].setText('')
        if self.num > 1 + b5 * 0.25:
            for i in range(exp5 + a5):
                poss_for_check5[i].setText((i + 1) * '1')
            self.check_in()

    def random_in(self):  # генерирует положение цифр
        global exp5, a5, poss_for_check5, poss5
        for i in range(exp5 + a5):
            poss5[i].setText(str(i + 1))
            poss_for_check5.append(poss5[i])

    def check_in(self):  # проверяет нажатые квадраты
        global exp5, b5, a5
        if exp5 <= 2:
            if b5 < exp5 + a5:
                if self.sender().text() == str((a5 + exp5) * '1'):
                    b5 += 1
                else:
                    self.showDialog_check()
            else:
                self.showDialog_win()
        else:
            self.showDialog_winwin()

    def showDialog_check(self):  # диалоговое окно с сообщением о поражении
        button = QMessageBox.question(self, "Поражение", "Начать заново？",
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.run()
        else:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog(self):  # диалоговое окно
        button = QMessageBox.question(self, "Начать заново？", "Уверенны?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.squares_norm = Squares_Norm()
            self.squares_norm.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog_win(self):  # диалоговое окно с сообщением о победе на уровне
        global exp5
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            exp5 += 1
            self.close()
            self.squares_norm = Squares_Norm()
            self.squares_norm.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog_winwin(self):  # диалоговое окно с сообщением о прохождение всех уровней
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.squares_norm = Squares_Norm()
            self.squares_norm.show()
        else:
            self.close()
            self.squares = Squares()
            self.squares.show()


class Squares_Hard(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Squares_Hard.ui', self)
        self.textEdit.setReadOnly(True)
        self.pushButton_back.clicked.connect(self.run)
        self.pushButton_run.clicked.connect(self.run)

    def run(self):  # основная функция
        global consh, poss_for_check6, b6, poss6
        poss6 = self.buttonGroup.buttons()
        for i in range(25):
            poss6[i].setText('')
        if self.sender().text() == 'Назад':  # возвращает в окно с выбором сложности
            consh = 0
            self.close()
            self.digits = Digits()
            self.digits.show()
        if self.sender().text() == 'Начать':  # начинает игру
            if consh < 1:
                shuffle(poss6)
                poss_for_check6 = []
                consh += 1
                self.random_in()
                self.num = 0
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.showTime)
                self.timer.start(1)
            else:
                self.showDialog()  # при повторном нажатии на кнопку начать открывает диалоговое окно

    def showTime(self):  # подсчитывает время и расставляет/убирает цифры
        global b6, exp6, a6, poss_for_check6, poss6
        self.label.setNum(self.num)
        self.num += 0.001
        if self.num == 1:
            for i in range(25):
                poss6[i].setText('')
        if self.num > 1 + b6 * 0.25:
            for i in range(exp6 + a6):
                [i].setText((i + 1) * '1')
            self.check_in()

    def random_in(self):  # генерирует положение цифр
        global exp6, a6, poss_for_check6, poss6
        for i in range(exp6 + a6):
            poss6[i].setText(str(i + 1))
            poss_for_check6.append(poss6[i])

    def check_in(self):  # проверяет нажатые квадраты
        global exp6, b6, a6
        if exp6 <= 2:
            if b5 < exp6 + a6:
                if self.sender().text() == str((a6 + exp6) * '1'):
                    b6 += 1
                else:
                    self.showDialog_check()
            else:
                self.showDialog_win()
        else:
            self.showDialog_winwin()

    def showDialog_check(self):  # диалоговое окно с сообщением о поражении
        button = QMessageBox.question(self, "Поражение", "Начать заново？",
                                      QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.run()
        else:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog(self):  # диалоговое окно
        button = QMessageBox.question(self, "Начать заново？", "Уверенны?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.squares_hard = Squares_Hard()
            self.squares_hard.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog_win(self):  # диалоговое окно с сообщением о победе на уровне
        global exp6
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            exp6 += 1
            self.close()
            self.squares_hard = Squares_Hard()
            self.squares_hard.show()
        if button == QMessageBox.Cancel:
            self.close()
            self.squares = Squares()
            self.squares.show()

    def showDialog_winwin(self):  # диалоговое окно с сообщением о прохождение всех уровней
        button = QMessageBox.question(self, "Молодец", "Дальше?", QMessageBox.Ok | QMessageBox.Cancel,
                                      QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.close()
            self.squares_hard = Squares_Hard()
            self.squares_hard.show()
        else:
            self.close()
            self.squares = Squares()
            self.squares.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
