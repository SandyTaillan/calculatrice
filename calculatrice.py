#!/usr/bin/env python
# -*- coding: utf-8 -*-

# voir les messages d'erreurs -> exception quand on tape des lettres et non des chiffres
# voir aussi pour n'avoir que 3 chiffres après la virgule


from PySide import QtGui, QtCore
from functools import partial
from designcalculatrice.interface import design


class MaSuperCalculatrice(QtGui.QTabWidget, design):
    def __init__(self):
        super(MaSuperCalculatrice, self).__init__()

        self.setupUiGene(fenetre)
        self.modificationSetupUi()
        self.setupConnections()

    def modificationSetupUi(self):

        # le but ici est de déterminer si le bouton est de type nombre
        # pour pouvoir afficher le nombre en arguments de clicked
        # cela évite de connecter les boutons un à un
        # Pour cela, c'est la fonction isdigit qui va savoir si c'est un nombre
        # si le pushbutton est bien un nombre, alors cela l'ajoute à la liste btns_nombres
        # dont on s'en servira dans la fonction setupConnections

        self.btns_nombres = []

        for i in range(self.gridLayout.count()):
            widget = self.gridLayout.itemAt(i).widget()
            # la ligne en suite se lit de cette façon : si le widget est de type QPushButton
            # et que le texte du widget et de type numéro alors on ajoute ce widget au bouton nombre
            if isinstance(widget, QtGui.QPushButton) and widget.text().isdigit():
                self.btns_nombres.append(widget)


    def setupConnections(self):
        '''connection de l'interface graphique avec le programme principal'''
        # partie calculatrice
        for btn in self.btns_nombres:
            btn.clicked.connect(partial(self.btnNombreClicked, str(btn.text())))

        self.btn_moins.clicked.connect(partial(self.btnOperationPressed, str(self.btn_moins.text())))
        self.btn_plus.clicked.connect(partial(self.btnOperationPressed, str(self.btn_plus.text())))
        self.btn_multi.clicked.connect(partial(self.btnOperationPressed, str(self.btn_multi.text())))
        self.btn_divi.clicked.connect(partial(self.btnOperationPressed, str(self.btn_divi.text())))

        self.btn_egal.clicked.connect(self.calculOperation)
        self.btn_c.clicked.connect(self.supprimerResultat)

        # partie temperature
        self.radioButton_faren_cel.clicked.connect(self.actionFarCel)
        self.radioButton_cel_faren.clicked.connect(self.actionCelFar)

        QtCore.QMetaObject.connectSlotsByName(self.temperature)

    def setupRaccourcisClaviers(self):
        # On fait une boucle de 0 a 9 pour passer a travers les boutons de nombres
        for btn in range(10):
            # On cree un shortcut pour chaque bouton
            QtGui.QShortcut(QtGui.QKeySequence(str(btn)), self, partial(self.btnNombreClicked, str(btn)))

        # On cree plusieurs shortcuts pour les boutons d'operation
        QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_plus.text())), self,
                        partial(self.btnOperationPressed, str(self.btn_plus.text())))
        QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_moins.text())), self,
                        partial(self.btnOperationPressed, str(self.btn_moins.text())))
        QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_multi.text())), self,
                        partial(self.btnOperationPressed, str(self.btn_multi.text())))
        QtGui.QShortcut(QtGui.QKeySequence(str(self.btn_divi.text())), self,
                        partial(self.btnOperationPressed, str(self.btn_divi.text())))

        # On cree d'autres shortcuts pour l'application en general
        QtGui.QShortcut(QtGui.QKeySequence('Enter'), self, self.calculOperation)
        QtGui.QShortcut(QtGui.QKeySequence('Del'), self, self.supprimerResultat)
        QtGui.QShortcut(QtGui.QKeySequence('Esc'), self, self.close)

    def btnNombreClicked(self, bouton):
        """Fonction activee quand l'utilisateur appuie sur un numero (0-9)"""

        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.resultat.text())

        if resultat == '0':
            # Si le resultat est egal a 0 on met le nombre du bouton
            # que l'utilisateur a presse dans le LineEdit resultat
            self.resultat.setText(bouton)
        else:
            # Si le resultat contient autre chose que zero,
            # On ajoute le texte du bouton a celui dans le LineEdit resultat
            self.resultat.setText(resultat + bouton)

    def btnOperationPressed(self, operation):
        """
        Fonction activee quand l'utilisateur appuie sur
        une touche d'operation (+, -, /, *)
        """

        # On recupere le texte dans le LineEdit operation
        operationText = str(self.operation.text())
        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.resultat.text())

        # On additionne l'operation en cours avec le texte dans le resultat
        # et on ajoute a la fin le signe de l'operation qu'on a choisie
        self.operation.setText(operationText + resultat + operation)
        # On reset le texte du LineEdit resultat
        self.resultat.setText('0')

    def supprimerResultat(self):
        """On reset le texte des deux LineEdit"""

        self.resultat.setText('0')
        self.operation.setText('')

    def calculOperation(self):
        """On calcule le resultat de l'operation en cours (quand l'utilisateur appuie sur egal)"""

        # On recupere le texte dans le LineEdit resultat
        resultat = str(self.resultat.text())

        # On ajoute le nombre actuel dans le LineEdit resultat
        # au LineEdit operation
        self.operation.setText(self.operation.text() + resultat)

        # On evalue le resultat de l'operation
        resultatOperation = eval(str(self.operation.text()))

        # On met le resultat final dans le LineEdit resultat
        self.resultat.setText(str(resultatOperation))


    # calcul pour le convertisseur température
    def actionFarCel(self):
        resul_inter = (self.le_entrerTemp.text())
        resul = (float(resul_inter) -32) / 1.8
        self.tex_result.setText(str(resul))

    def actionCelFar(self):
        resul_inter = (self.le_entrerTemp.text())
        resul = (float(resul_inter) * 1.8) + 32
        self.tex_result.setText(str(resul))


app = QtGui.QApplication([])

fenetre = QtGui.QTabWidget()
MaSuperCalculatrice()
fenetre.show()
app.exec_()                           # le programme ne se terminera qu'en cliquant sur la croix de la fenêtre