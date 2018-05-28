#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class interface(object):
    """Class pour regrouper toutes les fonctions utiles pour la création de l'interface graphique."""

    def intergenerale(self, ongletfenetre):
        """Appel des différentes fonctions de l'interface graphique et dimension générale"""

        ongletfenetre.setWindowTitle('Super-calculatrice')  # donner un nom à l'application
        w = 290
        h = 350
        ongletfenetre.move(1920 / 2 - w / 2, 1080 / 2 - h / 2)
        ongletfenetre.setMinimumSize(QtCore.QSize(w, h))  # taille minimum de ma fenetre en onglet
        ongletfenetre.resize(w, h)

        # appel des fonctions de chaque onglet
        self.creainterfaceCal(ongletfenetre)
        self.modificationSetupUi()
        self.creainterfaceTemp(ongletfenetre)
        self.creainterfacepied(ongletfenetre)

        self.retranslateUi(ongletfenetre)

    def creainterfaceCal(self, ongletfenetre):
        """Fonction dans laquelle on crée les widgets pour l'onglet calculatrice."""

        self.calculatrice = QtGui.QTabWidget()
        ongletfenetre.addTab(self.calculatrice, "Calculatrice")
        self.layout = QtGui.QGridLayout(self.calculatrice)


        # assignation des widgets à la calculatrice
        self.btntheme = QtGui.QPushButton('T', self.calculatrice)
        self.operation = QtGui.QLineEdit(self.calculatrice)
        self.resultat = QtGui.QLineEdit('0', self.calculatrice)
        self.spacerItem1 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.btn0 = QtGui.QPushButton('0', self.calculatrice)
        self.btn0.setObjectName("rouge")
        self.btn1 = QtGui.QPushButton('1', self.calculatrice)
        self.btn1.setObjectName("rouge")
        self.btn2 = QtGui.QPushButton('2', self.calculatrice)
        self.btn2.setObjectName("rouge")
        self.btn3 = QtGui.QPushButton('3', self.calculatrice)
        self.btn3.setObjectName("rouge")
        self.btn4 = QtGui.QPushButton('4', self.calculatrice)
        self.btn4.setObjectName("rouge")
        self.btn5 = QtGui.QPushButton('5', self.calculatrice)
        self.btn5.setObjectName("rouge")
        self.btn6 = QtGui.QPushButton('6', self.calculatrice)
        self.btn6.setObjectName("rouge")
        self.btn7 = QtGui.QPushButton('7', self.calculatrice)
        self.btn7.setObjectName("rouge")
        self.btn8 = QtGui.QPushButton('8', self.calculatrice)
        self.btn8.setObjectName("rouge")
        self.btn9 = QtGui.QPushButton('9', self.calculatrice)
        self.btn9.setObjectName("rouge")
        self.btn00 = QtGui.QPushButton('00', self.calculatrice)
        self.btn00.setObjectName("rouge")
        self.btnpoint = QtGui.QPushButton('.', self.calculatrice)
        self.btnpoint.setObjectName("rouge")
        self.btnegal = QtGui.QPushButton('=', self.calculatrice)
        self.btnegal.setObjectName("rouge")
        self.btnplus = QtGui.QPushButton('+', self.calculatrice)
        self.btnplus.setObjectName("rouge")
        self.btnmoins = QtGui.QPushButton('-', self.calculatrice)
        self.btnmoins.setObjectName("rouge")
        self.btnmulti = QtGui.QPushButton('*', self.calculatrice)
        self.btnmulti.setObjectName("rouge")
        self.btndivi = QtGui.QPushButton('/', self.calculatrice)
        self.btndivi.setObjectName("rouge")
        self.btn_c = QtGui.QPushButton('C', self.calculatrice)
        self.btn_c.setObjectName("rouge")

        # définition de la taille des widgets par rapport à la grille
        self.layout.addWidget(self.btntheme, 8, 6, 1, 1)
        self.layout.addWidget(self.operation, 0, 2, 1, 4)
        self.layout.addWidget(self.resultat, 1, 2, 2, 4)
        self.layout.addItem(self.spacerItem1, 3, 0, 2, 7)
        self.layout.addWidget(self.btn9, 4, 3, 1, 1)
        self.layout.addWidget(self.btn8, 4, 2, 1, 1)
        self.layout.addWidget(self.btn7, 4, 1, 1, 1)
        self.layout.addWidget(self.btn6, 5, 3, 1, 1)
        self.layout.addWidget(self.btn5, 5, 2, 1, 1)
        self.layout.addWidget(self.btn4, 5, 1, 1, 1)
        self.layout.addWidget(self.btn3, 6, 3, 1, 1)
        self.layout.addWidget(self.btn2, 6, 2, 1, 1)
        self.layout.addWidget(self.btn1, 6, 1, 1, 1)
        self.layout.addWidget(self.btn0, 7, 1, 1, 1)
        self.layout.addWidget(self.btn00, 7, 2, 1, 1)
        self.layout.addWidget(self.btnpoint, 7, 3, 1, 1)
        self.layout.addWidget(self.btnegal, 7, 5, 1, 2)
        self.layout.addWidget(self.btnplus, 6, 5, 1, 1)
        self.layout.addWidget(self.btnmoins, 6, 6, 1, 1)
        self.layout.addWidget(self.btnmulti, 5, 5, 1, 1)
        self.layout.addWidget(self.btndivi, 5, 6, 1, 1)
        self.layout.addWidget(self.btn_c, 4, 5, 1, 2)
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(6, -1, 6, -1)

        # attribution des tailles de widget
        # Attribution d'une taille minimum si le bouton à un ObjectName = rouge
        self.btnnombrerouge = []
        #self.btnnombrebleu = []

        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QtGui.QPushButton) and widget.objectName() == "rouge":
                self.btnnombrerouge.append(widget)
            #if isinstance(widget, QtGui.QPushButton) and widget.objectName() == "bleu":
                #self.btnnombrebleu.append(widget)
        for btn in self.btnnombrerouge:
            btn.setMinimumSize(50,50)

        #for btn in self.btnnombrebleu:
            #btn.setMinimumSize(50, 50)
        self.btntheme.setMaximumSize(20,20)
        self.resultat.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)  # alignement texte

        ongletfenetre.setCurrentIndex(0)  # indique l'onglet sur lequel ouvrira le programme


    def modificationSetupUi(self):
        """Fonction servant à mettre dans une liste tous les QPushButon avec un chiffre."""

        # le but ici est de déterminer si le bouton est de type nombre
        # pour pouvoir afficher le nombre en arguments de clicked
        # cela évite de connecter les boutons un à un
        # Pour cela, c'est la fonction isdigit qui va savoir si c'est un nombre
        # si le pushbutton est bien un nombre, alors cela l'ajoute à la liste btns_nombres
        # dont on s'en servira dans la fonction setupConnections


        self.btns_nombres = []

        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            # la ligne en suite se lit de cette façon : si le widget est de type QPushButton
            # et que le texte du widget et de type numéro alors on ajoute ce widget au bouton nombre
            if isinstance(widget, QtGui.QPushButton) and widget.text().isdigit():
                self.btns_nombres.append(widget)


    def creainterfaceTemp(self, ongletfenetre):
        """Fonction dans laquelle on crée les widgets pour l'onglet convertisseur."""

        self.temperature = QtGui.QTabWidget()
        ongletfenetre.addTab(self.temperature, "Température")
        self.layout = QtGui.QGridLayout(self.temperature)           # création du gridlayout


        # déclaration des variables-design
        self.la_entrerTemp = QtGui.QLabel(self.temperature)
        self.le_entrerTemp = QtGui.QLineEdit(self.temperature)
        self.radioButton_faren_cel = QtGui.QRadioButton(self.temperature)
        self.radioButton_cel_faren = QtGui.QRadioButton(self.temperature)
        self.line = QtGui.QFrame(self.temperature)
        self.la_result = QtGui.QLabel(self.temperature)
        self.tex_result = QtGui.QLabel(self.temperature)
        self.btntheme1 = QtGui.QPushButton('T', self.temperature)

        #Ajout de mes variables-design avec le layout
        self.layout.addWidget(self.la_entrerTemp, 0, 2, 1, 3)
        self.layout.addWidget(self.le_entrerTemp, 1, 2, 1, 1)
        self.layout.addWidget(self.radioButton_faren_cel, 2, 1, 1, 3)
        self.layout.addWidget(self.radioButton_cel_faren, 3, 1, 1, 3)
        self.layout.addWidget(self.line, 4, 1, 1, 3)
        self.layout.addWidget(self.la_result, 5, 2, 1, 2)
        self.layout.addWidget(self.tex_result, 6, 2, 1, 2)
        self.layout.addWidget(self.btntheme1, 8, 3, 1, 1)

        # déclaration des dimensions des éléments du design
        self.le_entrerTemp.setMinimumSize(QtCore.QSize(30, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.tex_result.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignHCenter)
        self.btntheme1.setMaximumSize(20, 20)

    def creainterfacepied(self, ongletfenetre):
        """Fonction dans laquelle on crée les widgets pour l'onglet convertir en pied"""

        self.mesurepied = QtGui.QTabWidget()
        ongletfenetre.addTab(self.mesurepied, "Mesure en pied")
        self.layout = QtGui.QGridLayout(self.mesurepied)  # rajoute un gridlayout sur l'onglet calculatrice

        # déclaration des variables-design
        self.la_entrerpied = QtGui.QLabel(self.mesurepied)
        self.le_entrercenti = QtGui.QLineEdit(self.mesurepied)
        self.radioButton_pied = QtGui.QRadioButton(self.mesurepied)  # création d'un bouton
        self.radioButton_metre = QtGui.QRadioButton(self.mesurepied)
        self.line1 = QtGui.QFrame(self.mesurepied)
        self.la_result1 = QtGui.QLabel(self.mesurepied)
        self.tex_result1 = QtGui.QLabel(self.mesurepied)
        self.btntheme2 = QtGui.QPushButton('T', self.mesurepied)

        # Ajout de mes variables-design avec le layout
        self.layout.addWidget(self.la_entrerpied, 0, 2, 1, 3)
        self.layout.addWidget(self.le_entrercenti, 1, 2, 1, 1)
        self.layout.addWidget(self.radioButton_pied, 2, 1, 1, 3)
        self.layout.addWidget(self.radioButton_metre, 3, 1, 1, 3)
        self.layout.addWidget(self.line1, 4, 1, 1, 3)
        self.layout.addWidget(self.la_result1, 5, 2, 1, 2)
        self.layout.addWidget(self.tex_result1, 6, 2, 1, 2)
        self.layout.addWidget(self.btntheme2, 8, 3, 1, 1)
        # déclaration des dimensions des éléments du design
        self.le_entrercenti.setMinimumSize(QtCore.QSize(30, 20))
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.tex_result1.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignHCenter)
        self.btntheme2.setMaximumSize(20, 20)

    # Problème de codage en UTF8 pour les accents
    def retranslateUi(self, ongletfenetre):
        """Fonction permettant d'écrire du texte en utf-8"""

        # Pour l'onglet température
        self.la_entrerTemp.setText(QtGui.QApplication.translate("ongletfenetre", "Entrez la température à convertir : ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_faren_cel.setText(QtGui.QApplication.translate("ongletfenetre", "Conversion Fahrenheit / Celcius ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_cel_faren.setText(QtGui.QApplication.translate("ongletfenetre", "Conversion Celcius / Fahrenheit ", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.la_result.setText(QtGui.QApplication.translate("ongletfenetre", "Le résultat de la conversion est :", None, QtGui.QApplication.UnicodeUTF8))
        ongletfenetre.setTabText(ongletfenetre.indexOf(self.temperature), QtGui.QApplication.translate("ongletfenetre", "Température", None, QtGui.QApplication.UnicodeUTF8))
        # pour l'onglet calculatrice
        # pour l'onglet mesurepied
        self.la_entrerpied.setText(QtGui.QApplication.translate("ongletfenetre", "Entrez la valeur à convertir : ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_pied.setText(QtGui.QApplication.translate("ongletfenetre", "Conversion en pied ", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_metre.setText(QtGui.QApplication.translate("ongletfenetre", "Conversion en centimètre ", None, QtGui.QApplication.UnicodeUTF8))
        self.la_result1.setText(QtGui.QApplication.translate("ongletfenetre", "Le résultat de la conversion est :", None, QtGui.QApplication.UnicodeUTF8))