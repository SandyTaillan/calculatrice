#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

class Ui_TabWidget(object):

    def setupUi(self, tabwidget):  # création de la fonction pour tout ce qui est graphique

        tabwidget.setWindowTitle('La super calculatrice')  # doner un nom à l'application ici tabwidget
        w = h = 500
        tabwidget.move(1920 / 2 - w / 2, 1080 / 2 - h / 2)
        tabwidget.setObjectName("tabwidget")  # Nomme l'objet
        tabwidget.resize(300, 320)  # taille de ma fenetre en onglet
        tabwidget.setMinimumSize(QtCore.QSize(290, 320))  # taille minimum de ma fenetre en onglet

        self.calculatrice = QtGui.QWidget()
        self.convertisseur = QtGui.QWidget()

        self.calculatrice.setObjectName("calculatrice")  # Nomme l'objet calculatrice
        self.convertisseur.setObjectName("convertisseur")

        # layout = QtGui.QGridLayout(self)                         au lieu  de layout = QtGui.QGridLayout(QtGui.QWidget())
        tabwidget.addTab(self.calculatrice, "Calculatrice")  # création d'un onglet Calculatrice
        tabwidget.addTab(self.convertisseur, "Convertisseur")  # création d'un autre onglet Convertisseur

        # Onglet calculatrice

        self.gridLayout = QtGui.QGridLayout(self.calculatrice)  # rajoute un gridlayout sur l'onglet calculatrice
        self.calculatrice.setMinimumSize(QtCore.QSize(0, 0))

        self.btn_1 = QtGui.QPushButton('1', self.calculatrice)  # assigne btn_1 à calculatrice
        # self.btn_1.setObjectName("btn_1")                        # nomme btn_1 mais pas utile dans ce cas de figure
        self.gridLayout.addWidget(self.btn_1, 6, 0, 1, 1)  # indique l'endroit sur le gridLayout
        self.btn_1.setMinimumSize(QtCore.QSize(52, 52))  # indique la taille du bouton

        self.btn_2 = QtGui.QPushButton('2', self.calculatrice)
        # self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 6, 1, 1, 1)
        self.btn_2.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_3 = QtGui.QPushButton('3', self.calculatrice)
        # self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 6, 2, 1, 1)
        self.btn_3.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_4 = QtGui.QPushButton('4', self.calculatrice)
        # self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 5, 0, 1, 1)
        self.btn_4.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_5 = QtGui.QPushButton('5', self.calculatrice)
        # self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 5, 1, 1, 1)
        self.btn_5.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_6 = QtGui.QPushButton('6', self.calculatrice)
        # self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 5, 2, 1, 1)
        self.btn_6.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_7 = QtGui.QPushButton('7', self.calculatrice)
        # self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 4, 0, 1, 1)
        self.btn_7.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_8 = QtGui.QPushButton('8', self.calculatrice)
        # self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 4, 1, 1, 1)
        self.btn_8.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_9 = QtGui.QPushButton('9', self.calculatrice)
        # self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 4, 2, 1, 1)
        self.btn_9.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_0 = QtGui.QPushButton('0', self.calculatrice)
        # self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 7, 0, 1, 1)
        self.btn_0.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_00 = QtGui.QPushButton('00', self.calculatrice)
        # self.btn_00.setObjectName("btn_00")
        self.gridLayout.addWidget(self.btn_00, 7, 1, 1, 1)
        self.btn_00.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_point = QtGui.QPushButton('.', self.calculatrice)
        # self.btn_point.setObjectName("btn_point")
        self.gridLayout.addWidget(self.btn_point, 7, 2, 1, 1)
        self.btn_point.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_egal = QtGui.QPushButton('=', self.calculatrice)
        # self.btn_egal.setObjectName("btn_egal")
        self.gridLayout.addWidget(self.btn_egal, 7, 5, 1, 2)
        self.btn_egal.setMinimumSize(QtCore.QSize(106, 52))

        self.btn_plus = QtGui.QPushButton('+', self.calculatrice)
        # self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 6, 5, 1, 1)
        self.btn_plus.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_moins = QtGui.QPushButton('-', self.calculatrice)
        # self.btn_moins.setObjectName("btn_moins")
        self.gridLayout.addWidget(self.btn_moins, 6, 6, 1, 1)
        self.btn_moins.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_multi = QtGui.QPushButton('*', self.calculatrice)
        # self.btn_multi.setObjectName("btn_multi")
        self.gridLayout.addWidget(self.btn_multi, 5, 5, 1, 1)
        self.btn_multi.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_divi = QtGui.QPushButton('/', self.calculatrice)
        # self.btn_divi.setObjectName("btn_divi")
        self.gridLayout.addWidget(self.btn_divi, 5, 6, 1, 1)
        self.btn_divi.setMinimumSize(QtCore.QSize(52, 52))

        self.btn_c = QtGui.QPushButton('C', self.calculatrice)
        # self.btn_c.setObjectName("btn_c")
        self.gridLayout.addWidget(self.btn_c, 4, 5, 1, 2)
        self.btn_c.setMinimumSize(QtCore.QSize(106, 52))

        self.operation = QtGui.QLineEdit(self.calculatrice)
        # self.operation.setObjectName("operation")
        self.gridLayout.addWidget(self.operation, 0, 0, 1, 7)

        self.resultat = QtGui.QLineEdit('0', self.calculatrice)
        # self.resultat.setObjectName("resultat")
        self.gridLayout.addWidget(self.resultat, 1, 0, 2, 7)
        self.resultat.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)  # alignement texte
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.resultat.setFont(font)
        spacerItem1 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 7)

        spacerItem2 = QtGui.QSpacerItem(1, 223, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 4, 4, 1)

