#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import psycopg2
from PyQt5 import uic
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMessageBox, QGridLayout, QTableWidget, \
    QTableWidgetItem, QWidget, QAbstractItemView, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QIcon


def about():
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText("Автор: студент группы М8О-310Б-20 Петров Никита")
    msg_box.setWindowTitle("Об авторе")
    msg_box.exec()


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Waiter(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)

        self.lbl = QLabel(self)
        qle = QLineEdit()

        button = Button("Button", self)

        self.layout().addWidget(qle)
        self.layout().addWidget(button)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        #qle.textChanged[str].connect(self.onChanged)
        self.setGeometry(300, 300, 280, 170)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


class Pub(QMainWindow):

    def clean_layout(self):
        if self.layout():
            for i in reversed(range(self.layout.count())):
                self.layout.itemAt(i).widget().deleteLater()

    def print_get_result(self, strings):
        self.clean_layout()
        if len(strings):
            table = QTableWidget()
            table.setRowCount(len(strings[0]))
            table.setColumnCount(len(strings))
            table.setHorizontalHeaderLabels([desc[0] for desc in self.cur.description])
            table.resizeColumnsToContents()
            table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            for i in range(len(strings)):
                for j in range(len(strings[i])):
                    table.setItem(i, j, QTableWidgetItem(str(strings[i][j])))
            self.setCentralWidget(table)

    def init_add_bar(self):
        add = self.menuBar()
        add_menu = add.addMenu('&Добавить')

        dish = QAction(QIcon('resources/dish.png'), 'Блюдо', self)
        dish.triggered.connect(self.add_new_dish)
        add_menu.addAction(dish)

        nonalcoholic = QAction(QIcon('resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        nonalcoholic.triggered.connect(self.add_new_alcohol_free)
        add_menu.addAction(nonalcoholic)

        alcoholic = QAction(QIcon('resources/alcoholic.png'), 'Алкогольный напиток', self)
        alcoholic.triggered.connect(self.add_new_alcohol)
        add_menu.addAction(alcoholic)

        dish_menu = QAction(QIcon('resources/menu.png'), 'Меню', self)
        dish_menu.triggered.connect(self.add_new_menu)
        add_menu.addAction(dish_menu)

        waiter = QAction(QIcon('resources/waiter.png'), 'Оффициант', self)
        waiter.triggered.connect(self.add_new_waiter)
        add_menu.addAction(waiter)

        client = QAction(QIcon('resources/client.png'), 'Клиент', self)
        client.triggered.connect(self.add_new_client)
        add_menu.addAction(client)

        ingredient = QAction(QIcon('resources/carrot.png'), 'Ингредиент', self)
        ingredient.triggered.connect(self.add_new_ingredient)
        add_menu.addAction(ingredient)

        provider = QAction(QIcon('resources/provider.png'), 'Поставщик', self)
        provider.triggered.connect(self.add_new_provider)
        add_menu.addAction(provider)

        bill = QAction(QIcon('resources/check.png'), 'Чек', self)
        add_menu.addAction(bill)
        # self.toolbar = self.addToolBar('Hi')

    def init_get_bar(self):
        get = self.menuBar()
        get_menu = get.addMenu('&Вывести')

        get_dish = QAction(QIcon('resources/dish.png'), 'Блюдо', self)
        get_dish.triggered.connect(self.get_all_dishes)
        get_menu.addAction(get_dish)

        get_nonalcoholic = QAction(QIcon('resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        get_nonalcoholic.triggered.connect(self.get_all_non_alcohol)
        get_menu.addAction(get_nonalcoholic)

        get_alcoholic = QAction(QIcon('resources/alcoholic.png'), 'Алкогольный напиток', self)
        get_alcoholic.triggered.connect(self.get_all_alcohol)
        get_menu.addAction(get_alcoholic)

        get_dish_menu = QAction(QIcon('resources/menu.png'), 'Меню', self)
        get_dish_menu.triggered.connect(self.get_all_menu)
        get_menu.addAction(get_dish_menu)

        get_waiter = QAction(QIcon('resources/waiter.png'), 'Оффициант', self)
        get_waiter.triggered.connect(self.get_all_waiters)
        get_menu.addAction(get_waiter)

        get_client = QAction(QIcon('resources/client.png'), 'Клиент', self)
        get_client.triggered.connect(self.get_all_clients)
        get_menu.addAction(get_client)

        get_ingredient = QAction(QIcon('resources/carrot.png'), 'Ингредиент', self)
        get_ingredient.triggered.connect(self.get_all_ingredients)
        get_menu.addAction(get_ingredient)

        get_provider = QAction(QIcon('resources/provider.png'), 'Поставщик', self)
        get_provider.triggered.connect(self.get_all_providers)
        get_menu.addAction(get_provider)

        get_bill = QAction(QIcon('resources/check.png'), 'Счёт', self)
        get_bill.triggered.connect(self.get_all_checks)
        get_menu.addAction(get_bill)

    def init_change_bar(self):
        change = self.menuBar()
        change_menu = change.addMenu('&Изменить')

        change_dish = QAction(QIcon('resources/dish.png'), 'Блюдо', self)
        change_menu.addAction(change_dish)

        change_nonalcoholic = QAction(QIcon('resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        change_menu.addAction(change_nonalcoholic)

        change_alcoholic = QAction(QIcon('resources/alcoholic.png'), 'Алкогольный напиток', self)
        change_menu.addAction(change_alcoholic)

        change_dish_menu = QAction(QIcon('resources/menu.png'), 'Меню', self)
        change_menu.addAction(change_dish_menu)

        change_waiter = QAction(QIcon('resources/waiter.png'), 'Оффициант', self)
        change_menu.addAction(change_waiter)

        change_client = QAction(QIcon('resources/client.png'), 'Клиент', self)
        change_menu.addAction(change_client)

        change_ingredient = QAction(QIcon('resources/carrot.png'), 'Ингредиент', self)
        change_menu.addAction(change_ingredient)

        change_provider = QAction(QIcon('resources/provider.png'), 'Поставщик', self)
        change_menu.addAction(change_provider)

        change_bill = QAction(QIcon('resources/check.png'), 'Счёт', self)
        change_menu.addAction(change_bill)

    def change_alcohol(self):
        print("a")

    def change_alcohol_free(self):
        print("a")

    def change_check(self):
        print("a")

    def change_waiter(self):
        print("a")

    def change_menu(self):
        print("a")

    def change_client(self):
        print("a")

    def change_provider(self):
        print("a")

    def change_dish(self):
        print("a")

    def change_ingredient(self):
        print("a")

    def add_new_alcohol(self):
        print("a")

    def add_new_alcohol_free(self):
        print("a")

    def add_new_check(self):
        print("a")

    def add_new_waiter(self):
        waiter_widget = Waiter()
        self.setCentralWidget(waiter_widget)

    def add_new_menu(self):
        print("a")

    def add_new_client(self):
        print("a")

    def add_new_provider(self):
        print("a")

    def add_new_dish(self):
        print("a")

    def add_new_ingredient(self):
        print("a")

    def get_all_ingredients(self):
        self.cur.execute("SELECT * FROM ingredient")
        ingredient = self.cur.fetchall()
        self.print_get_result(ingredient)

    def get_all_checks(self):
        self.cur.execute("SELECT * FROM checks")
        checks = self.cur.fetchall()
        self.print_get_result(checks)

    def get_all_clients(self):
        self.cur.execute("SELECT * FROM clients")
        clients = self.cur.fetchall()
        self.print_get_result(clients)

    def get_all_non_alcohol(self):
        self.cur.execute("SELECT * FROM alcohol_free")
        alcohol_free = self.cur.fetchall()
        self.print_get_result(alcohol_free)

    def get_all_alcohol(self):
        self.cur.execute("SELECT * FROM alcohol")
        alcohol = self.cur.fetchall()
        self.print_get_result(alcohol)

    def get_all_waiters(self):
        self.cur.execute("SELECT * FROM waiters")
        waiters = self.cur.fetchall()
        self.print_get_result(waiters)

    def get_all_dishes(self):
        self.cur.execute("SELECT * FROM dish")
        dishes = self.cur.fetchall()
        self.print_get_result(dishes)

    def get_all_menu(self):
        self.cur.execute("SELECT * FROM menu")
        menu = self.cur.fetchall()
        print(menu)

    def get_all_providers(self):
        self.cur.execute("SELECT * FROM providers")
        providers = self.cur.fetchall()
        self.print_get_result(providers)

    def __init__(self):
        super().__init__()

        self.conn = psycopg2.connect(user="postgres",
                                     password="1964",
                                     host="localhost",
                                     port="5432",
                                     database="postgres")
        self.cur = self.conn.cursor()

        uic.loadUi('forms/mainwindow.ui', self)
        self.initUI()

    def initUI(self):

        # init bars
        self.init_add_bar()
        self.init_get_bar()
        self.init_change_bar()

        about_action = QAction('Об авторе', self)
        about_action.triggered.connect(about)
        self.menuBar().addAction(about_action)

        self.setGeometry(300, 300, 800, 600)
        self.layout().setGeometry(QRect(20, 20, 500, 500))
        self.setWindowIcon(QIcon('resources/pub.png'))
        self.setWindowTitle('Паб')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pub()
    sys.exit(app.exec_())
