#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenuBar
from PyQt5.QtGui import QIcon


class Pub(QMainWindow):

    def initAddBar(self):
        add = self.menuBar()
        add_menu = add.addMenu('&Добавить')

        dish = QAction(QIcon('resources/dish.png'), 'Блюдо', self)
        add_menu.addAction(dish)

        nonalcoholic = QAction(QIcon('resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        add_menu.addAction(nonalcoholic)

        alcoholic = QAction(QIcon('resources/alcoholic.png'), 'Алкогольный напиток', self)
        add_menu.addAction(alcoholic)

        waiter = QAction(QIcon('resources/waiter.png'), 'Оффициант', self)
        add_menu.addAction(waiter)

        client = QAction(QIcon('resources/client.png'), 'Клиент', self)
        add_menu.addAction(client)

        ingredient = QAction(QIcon('resources/carrot.png'), 'Ингредиент', self)
        add_menu.addAction(ingredient)

        provider = QAction(QIcon('resources/provider.png'), 'Поставщик', self)
        add_menu.addAction(provider)

        #self.toolbar = self.addToolBar('Hi')

    def initGetBar(self):
        get = self.menuBar()
        get_menu = get.addMenu('&Получить')

        get_dish = QAction(QIcon('resources/dish.png'), 'Блюдо', self)
        get_menu.addAction(get_dish)

        get_nonalcoholic = QAction(QIcon('resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        get_menu.addAction(get_nonalcoholic)

        get_alcoholic = QAction(QIcon('resources/alcoholic.png'), 'Алкогольный напиток', self)
        get_menu.addAction(get_alcoholic)

        get_waiter = QAction(QIcon('resources/waiter.png'), 'Оффициант', self)
        get_menu.addAction(get_waiter)

        get_client = QAction(QIcon('resources/client.png'), 'Клиент', self)
        get_menu.addAction(get_client)

        get_ingredient = QAction(QIcon('resources/carrot.png'), 'Ингредиент', self)
        get_menu.addAction(get_ingredient)

        get_provider = QAction(QIcon('resources/provider.png'), 'Поставщик', self)
        get_menu.addAction(get_provider)

    def __init__(self):
        super().__init__()

        self.toolbar = None
        self.initUI()

    def initUI(self):
        self.initAddBar()
        self.initGetBar()

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Паб')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pub()
    sys.exit(app.exec_())
