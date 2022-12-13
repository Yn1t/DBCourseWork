#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import psycopg2
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui


class Pub(QMainWindow):
    def con(self):
        self.conn = psycopg2.connect(user="postgres",
                                     password="1234",
                                     host="localhost",
                                     port="5432",
                                     database="postgres")
        #self.cur = self.conn.cursor()

    def initAddBar(self):
        add = self.menuBar()
        add_menu = add.addMenu('&Добавить')

        dish = QAction(QIcon('venv/resources/dish.png'), 'Блюдо', self)
        add_menu.addAction(dish)

        nonalcoholic = QAction(QIcon('venv/resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        add_menu.addAction(nonalcoholic)

        alcoholic = QAction(QIcon('venv/resources/alcoholic.png'), 'Алкогольный напиток', self)
        add_menu.addAction(alcoholic)

        bar_menu = QAction(QIcon('venv/resources/bar_menu.png'), 'Барное меню', self)
        add_menu.addAction(bar_menu)

        dish_menu = QAction(QIcon('venv/resources/menu.png'), 'Меню', self)
        add_menu.addAction(dish_menu)

        waiter = QAction(QIcon('venv/resources/waiter.png'), 'Оффициант', self)
        add_menu.addAction(waiter)

        client = QAction(QIcon('venv/resources/client.png'), 'Клиент', self)
        add_menu.addAction(client)

        ingredient = QAction(QIcon('venv/resources/carrot.png'), 'Ингредиент', self)
        add_menu.addAction(ingredient)

        provider = QAction(QIcon('venv/resources/provider.png'), 'Поставщик', self)
        add_menu.addAction(provider)

        bill = QAction(QIcon('venv/resources/check.png'), 'Чек', self)
        add_menu.addAction(bill)
        # self.toolbar = self.addToolBar('Hi')

    def initGetBar(self):
        get = self.menuBar()
        get_menu = get.addMenu('&Вывести')

        get_dish = QAction(QIcon('venv/resources/dish.png'), 'Блюдо', self)
        get_menu.addAction(get_dish)

        get_nonalcoholic = QAction(QIcon('venv/resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        get_menu.addAction(get_nonalcoholic)

        get_alcoholic = QAction(QIcon('venv/resources/alcoholic.png'), 'Алкогольный напиток', self)
        get_menu.addAction(get_alcoholic)

        get_bar_menu = QAction(QIcon('venv/resources/bar_menu.png'), 'Барное меню', self)
        get_menu.addAction(get_bar_menu)

        get_dish_menu = QAction(QIcon('venv/resources/menu.png'), 'Меню', self)
        get_menu.addAction(get_dish_menu)

        get_waiter = QAction(QIcon('venv/resources/waiter.png'), 'Оффициант', self)
        get_menu.addAction(get_waiter)

        get_client = QAction(QIcon('venv/resources/client.png'), 'Клиент', self)
        get_menu.addAction(get_client)

        get_ingredient = QAction(QIcon('venv/resources/carrot.png'), 'Ингредиент', self)
        get_menu.addAction(get_ingredient)

        get_provider = QAction(QIcon('venv/resources/provider.png'), 'Поставщик', self)
        get_menu.addAction(get_provider)

        get_bill = QAction(QIcon('venv/resources/check.png'), 'Счёт', self)
        get_menu.addAction(get_bill)

    def initChangeBar(self):
        change = self.menuBar()
        change_menu = change.addMenu('&Изменить')

        change_dish = QAction(QIcon('venv/resources/dish.png'), 'Блюдо', self)
        change_menu.addAction(change_dish)

        change_nonalcoholic = QAction(QIcon('venv/resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        change_menu.addAction(change_nonalcoholic)

        change_alcoholic = QAction(QIcon('venv/resources/alcoholic.png'), 'Алкогольный напиток', self)
        change_menu.addAction(change_alcoholic)

        change_bar_menu = QAction(QIcon('venv/resources/bar_menu.png'), 'Барное меню', self)
        change_menu.addAction(change_bar_menu)

        change_dish_menu = QAction(QIcon('venv/resources/menu.png'), 'Меню', self)
        change_menu.addAction(change_dish_menu)

        change_waiter = QAction(QIcon('venv/resources/waiter.png'), 'Оффициант', self)
        change_menu.addAction(change_waiter)

        change_client = QAction(QIcon('venv/resources/client.png'), 'Клиент', self)
        change_menu.addAction(change_client)

        change_ingredient = QAction(QIcon('venv/resources/carrot.png'), 'Ингредиент', self)
        change_menu.addAction(change_ingredient)

        change_provider = QAction(QIcon('venv/resources/provider.png'), 'Поставщик', self)
        change_menu.addAction(change_provider)

        change_bill = QAction(QIcon('venv/resources/check.png'), 'Счёт', self)
        change_menu.addAction(change_bill)

    def __init__(self):
        super().__init__()

        self.cur = None
        self.conn = None
        self.initUI()

    def initUI(self):
        # create connection
        self.con()

        # init bars
        self.initAddBar()
        self.initGetBar()
        self.initChangeBar()

        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QIcon('venv/resources/pub.png'))
        self.setWindowTitle('Паб')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pub()
    sys.exit(app.exec_())
