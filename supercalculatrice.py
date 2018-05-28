#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 2.7 et PySide

from PySide import QtGui, QtCore
from design.intergraphique import interface
from functools import partial

class Masupercalculatrice(QtGui.QTabWidget, interface):
    """Ma super class qui va appeler les fonctions principales"""

    def __init__(self):
        super(Masupercalculatrice, self).__init__()

        # déclaration de variables
        self.choixtheme = 0

        #lancement des fonctions
        self.intergenerale(ongletfenetre)
        self.relationinter()
        self.modiftheme()

    def relationinter(self):
        """Fonction dont le but est de connecter l'interface au code de calcul"""

        # partie calculatrice
        for btn in self.btns_nombres:
            btn.clicked.connect(partial(self.boutonclick, str(btn.text())))
        self.btnpoint.clicked.connect(partial(self.boutonclick, str(self.btnpoint.text())))
        self.btnmoins.clicked.connect(partial(self.btnOperationPressed, str(self.btnmoins.text())))
        self.btnplus.clicked.connect(partial(self.btnOperationPressed, str(self.btnplus.text())))
        self.btnmulti.clicked.connect(partial(self.btnOperationPressed, str(self.btnmulti.text())))
        self.btndivi.clicked.connect(partial(self.btnOperationPressed, str(self.btndivi.text())))
        self.btnegal.clicked.connect(self.calculOperation)
        self.btn_c.clicked.connect(self.supprimerResultat)
        self.btntheme.clicked.connect(self.modiftheme)
        # partie temperature
        self.radioButton_faren_cel.clicked.connect(self.actionFarCel)
        self.radioButton_cel_faren.clicked.connect(self.actionCelFar)
        self.btntheme1.clicked.connect(self.modiftheme)
        # partie metre-pied
        self.radioButton_pied.clicked.connect(self.actionpiedcenti)
        self.radioButton_metre.clicked.connect(self.actioncentipied)
        self.btntheme2.clicked.connect(self.modiftheme)

        # feuille de style
        f = QtCore.QFile("./design/designsombre.css")
        f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        ts = QtCore.QTextStream(f)
        stylesheet = ts.readAll()
        ongletfenetre.setStyleSheet(stylesheet)

    def modiftheme(self):
        """Sélection de la feuille de style avec le bouton"""

        if self.choixtheme == 0:
            f = QtCore.QFile("./design/designclair.css")
            f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
            ts = QtCore.QTextStream(f)
            stylesheet = ts.readAll()
            ongletfenetre.setStyleSheet(stylesheet)
            self.choixtheme = 1
        else:
            f = QtCore.QFile("./design/designsombre.css")
            f.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
            ts = QtCore.QTextStream(f)
            stylesheet = ts.readAll()
            ongletfenetre.setStyleSheet(stylesheet)
            self.choixtheme = 0

    def boutonclick(self, bouton):
        """Fonction activée quand l'utilisateur appuie sur un numéro (0-9)"""

        # On récupére le texte dans le LineEdit résultat
        resultat = str(self.resultat.text())

        if resultat == '0':
            # Si le résultat est égal a 0 on met le nombre du bouton
            # que l'utilisateur a pressé dans le LineEdit résultat
            self.resultat.setText(bouton)
        else:
            # Si le résultat contient autre chose que zero,
            # On ajoute le texte du bouton à celui dans le LineEdit résultat
            self.resultat.setText(resultat + bouton)

    def btnOperationPressed(self, operation):
        """Fonction activée quand l'utilisateur appuie sur une touche d'operation (+, -, /, *)"""

        # On récupére le texte dans le LineEdit opération
        operationText = str(self.operation.text())
        # On récupére le texte dans le LineEdit résultat
        resultat = str(self.resultat.text())

        # On additionne l'operation en cours avec le texte dans le résultat
        # et on ajoute a la fin le signe de l'opération qu'on a choisie
        self.operation.setText(operationText + resultat + operation)
        # On reset le texte du LineEdit résultat
        self.resultat.setText('0')

    def supprimerResultat(self):
        """On reset le texte des deux LineEdit"""

        self.resultat.setText('0')
        self.operation.setText('')

    def calculOperation(self):
        """On calcule le résultat de l'opération en cours (quand l'utilisateur appuie sur égal)"""

        # On récupére le texte dans le LineEdit résultat
        try:
            resultat = str(self.resultat.text())
            # On ajoute le nombre actuel dans le LineEdit résultat
            # au LineEdit operation
            self.operation.setText(self.operation.text() + resultat)
            # On évalue le résultat de l'opération
            resultatOperation = eval(str(self.operation.text()))
            # On met le résultat final dans le LineEdit résultat
            self.resultat.setText(str(resultatOperation))
        except NameError:
            # je suis obligée d'attendre un peu (3 secondes) pour que Erreur ait le temps de s'afficher
            self.resultat.setText('Erreur')
            self.timer = QtCore.QTimer()
            self.timer.singleShot(3000, self.supprimerResultat)


    # calcul pour le convertisseur température

    # todo : je répète deux fois le même code. Voir si je peux améliorer cela.

    def actionFarCel(self):
        """Calcul pour convertir du Fahrenheit en Celcius"""
        try:
            resul_inter = (self.le_entrerTemp.text())
            resul = (float(resul_inter) -32) / 1.8
            self.tex_result.setText(str(resul))
        except ValueError:
            self.le_entrerTemp.setText('Veuillez entrer un nombre, merci.')
            self.timer = QtCore.QTimer()
            self.timer.singleShot(3000, self.le_entrerTemp.clear)

    def actionCelFar(self):
        """Calcul pour convertir du Celcius en Fahrenheit"""
        try:
            resul_inter = (self.le_entrerTemp.text())
            resul = (float(resul_inter) * 1.8) + 32
            self.tex_result.setText(str(resul))
        except ValueError:
            self.le_entrerTemp.setText('Veuillez entrer un nombre, merci.')
            self.timer = QtCore.QTimer()
            self.timer.singleShot(3000, self.le_entrerTemp.clear)

    # calcul pour le convertisseur centimètre -pied

    def actionpiedcenti(self):
        try:
            resul_inter = (self.le_entrercenti.text())
            resul = (float(resul_inter) /30.48)
            self.tex_result1.setText(str(resul))
        except ValueError:
            self.le_entrercenti.setText('Veuillez entrer un nombre, merci.')
            self.timer = QtCore.QTimer()
            self.timer.singleShot(3000, self.le_entrercenti.clear)

    def actioncentipied(self):
        try:
            resul_inter = (self.le_entrercenti.text())
            print('resul_inter')
            resul = (float(resul_inter) * 30.48)
            print(resul)
            self.tex_result1.setText(str(resul))
        except ValueError:
            self.le_entrercenti.setText('Veuillez entrer un nombre, merci.')
            self.timer = QtCore.QTimer()
            self.timer.singleShot(3000, self.le_entrercenti.clear)


app = QtGui.QApplication([])
ongletfenetre = QtGui.QTabWidget()

Masupercalculatrice()
ongletfenetre.show()
app.exec_()