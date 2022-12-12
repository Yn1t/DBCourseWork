#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenuBar
from PyQt5.QtGui import QIcon


class Pub(QMainWindow):

    def initToolBar(self):
        add = self.menuBar()
        addmenu = add.addMenu('&Добавить')

        dish = QAction(QIcon('resources/dish.png'), 'Блюдо', self)
        addmenu.addAction(dish)

        nonalcoholic = QAction(QIcon('resources/nonalcoholic.png'), 'Безалкогольный напиток', self)
        addmenu.addAction(nonalcoholic)

        alcoholic = QAction(QIcon('resources/alcoholic.png'), 'Алкогольный напиток', self)
        addmenu.addAction(alcoholic)

        waiter = QAction(QIcon('resources/waiter.png'), 'Оффициант', self)
        addmenu.addAction(waiter)

        client = QAction(QIcon('resources/client.png'), 'Клиент', self)
        addmenu.addAction(client)

        ingredient = QAction(QIcon('resources/carrot.png'), 'Ингредиент', self)
        addmenu.addAction(ingredient)

        provider = QAction(QIcon('resources/provider.png'), 'Поставщик', self)
        addmenu.addAction(provider)

        #self.toolbar = self.addToolBar('Hi')

    def __init__(self):
        super().__init__()

        self.toolbar = None
        self.initUI()

    def initUI(self):
        self.initToolBar()

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Паб')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pub()
    sys.exit(app.exec_())
