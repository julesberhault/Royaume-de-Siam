import sys
from jeu import *
from PyQt5 import  QtGui, QtCore, QtWidgets, uic
import winsound
import time

"""
Classe permettant l'affichage graphique et l'interaction avec le jeu. Elle fonctionne donc avec la classe jeu.
"""

class Interface_Siam_UI(QtWidgets.QMainWindow):
    """
    Cette classe sert à faire le lien entre l'interface graphique créée
    dans QtDesigner et les mécanismes de jeu de l'écosystème.
    """

    def __init__(self, nb_piece, nb_roc, *args, **kwargs):
        self.nb_piece = nb_piece
        self.nb_roc = nb_roc
        self.jeu = Partie(5, 5, self.nb_piece, self.nb_roc, music=True)
        self.depl_case=[[False,'E','O'],['S'],['N']]
        self.pos_depl=[[0,0],[0,0]]
        self.pos = [0, 0]
        self.selection = True
        self.fenetre_aide = False
        self.choix = 0
        self.time=time.time()
        self.image_rhinoceros={'N':'rhinocerosN.png','E':'rhinocerosE.png','S':'rhinocerosS.png','O':'rhinocerosO.png'}
        self.image_elephant={'N':'elephantN.png','E':'elephantE.png','S':'elephantS.png','O':'elephantO.png'}

        QtWidgets.QMainWindow.__init__(self, *args)
        # self.ui = Ui_principale_ihm()
        # self.ui.setupUi(self)
        self.ui = uic.loadUi('interface.ui', self)

        # Connection des fonctions aux boutons de l'interface
        self.ui.bouton_rec.clicked.connect(self.recommencer)
        self.ui.bouton_pla.clicked.connect(self.placer)
        self.ui.bouton_dep.clicked.connect(self.deplacer)
        self.ui.bouton_ori.clicked.connect(self.orientation)
        self.ui.bouton_sor.clicked.connect(self.sortir)
        self.ui.bouton_mus.clicked.connect(self.musique)
        self.ui.bouton_aid.clicked.connect(self.aide)

        self.painter = QtGui.QPainter()

        self.ui.conteneur.paintEvent = self.draw_Royaume
        pal = QtGui.QPalette()
        pixmap = QtGui.QPixmap("grid.png")
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap)) #setGeometrie
        self.ui.conteneur.lower()
        self.ui.conteneur.stackUnder(self)
        self.ui.conteneur.setAutoFillBackground(True)
        self.ui.conteneur.setPalette(pal)

    def recommencer(self):
        m=self.jeu.music
        self.jeu = Partie(5, 5, self.nb_piece, self.nb_roc, music=m)
        self.choix = 0
        self.time=time.time()
        self.fenetre_aide = False
        self.ui.conteneur.update()
        self.ui.conteneur.repaint()

    def placer(self): #ne serait il pas plus intuitif pour l'utilisateur de préciser l'orientation qu'il souhaite pour la fonction placer ?? On fait ca en créant 4 boutons, Nord, Sud, Est, Ouest ??
        self.selection = True
        self.choix = 4

    def deplacer(self):
        self.selection_depl = True #l'utilisateur a appuyé sur le bouton déplacer
        self.choix = 1

    def orientation(self):
        self.selection_orientation = True  # l'utilisateur a appuyé sur le bouton orientation
        self.choix = 2
        self.update()

    def sortir(self):
        self.selection = True
        self.choix = 3

    def musique(self):
        if self.jeu.music==False:
            self.jeu.music = True
            winsound.PlaySound("donkey_kong_theme.wav", winsound.SND_ASYNC)
        else:
            self.jeu.music = False
            winsound.PlaySound("place.wav", winsound.SND_ASYNC)

    def aide(self):
        self.fenetre_aide = not(self.fenetre_aide)
        self.ui.conteneur.update()

    def draw_Royaume(self, *args): #*args à la place de e

        # on informe le peintre qu'on veut dessiner dans le widget conteneur
        self.painter.begin(self.ui.conteneur)
        # variable intermédiraire pour alléger le code
        p = self.painter

        # Dessin de la grille
        largeur_case=self.ui.conteneur.width()//5
        hauteur_case=self.ui.conteneur.height()//5

        #Dessin des pions
        #On parcourt la représentation du jeu et on affiche

        for i in range(5) :
            for j in range(5) :
                if self.jeu.table_jeu[i][j]!=0 : #faut il mettre jeu.table_jeu ??
                    if self.jeu.table_jeu[i][j].car()== 'M':
                        img = QtGui.QImage(self.image_elephant[self.jeu.table_jeu[i][j].orientation])
                        p.drawImage(j*largeur_case,i*largeur_case,img) # on affiche l'image aux bonnes coordonées
                    if self.jeu.table_jeu[i][j].car()== 'H':
                        img = QtGui.QImage(self.image_rhinoceros[self.jeu.table_jeu[i][j].orientation])
                        p.drawImage(j * largeur_case, i * largeur_case, img)# on affiche l'image aux bonnes coordonées
                    if self.jeu.table_jeu[i][j].car() == 'R':
                        img = QtGui.QImage("mountain.png")
                        p.drawImage(j * largeur_case, i * largeur_case-10, img) # on affiche l'image aux bonnes coordonées
        if time.time()-self.time < 2:
            img = QtGui.QImage("logo.png")
            p.drawImage(50, 10, img)
            img = QtGui.QImage("start.png")
            p.drawImage(50, 455, img)
        if self.fenetre_aide==True:
            self.selection=True
            img = QtGui.QImage("aide.png")
            p.drawImage(25, 25, img)
        if self.jeu.end==True:
            img = QtGui.QImage("you_win.png")
            p.drawImage(70, 330, img)
            if self.jeu.elephants.winner==True:
                img = QtGui.QImage("elephant.png")
                p.drawImage(160, 90, img)
            if self.jeu.rhinoceros.winner==True:
                img = QtGui.QImage("rhinoceros.png")
                p.drawImage(160, 90, img)
        if self.selection==False:
            img = QtGui.QImage("select.png")
            p.drawImage(self.pos_depl[0][1] * largeur_case, self.pos_depl[0][0] * largeur_case, img)
        # on informe le peintre qu'on a fini
        self.painter.end()

    def mousePressEvent(self,e) : # à definir dans qt designer, à chaque clique on rentre dans cette fonction
        largeur_case=self.ui.conteneur.width()//5
        hauteur_case=self.ui.conteneur.height()//5
        # Les coordonnées du point cliqué sont e.x() et e.y()

        # Transformation des coordonnées écran en coordonnées dans
        # le plateau de jeu
        j=min(e.x()//largeur_case,4)
        i=min(round(((e.y()-26)//hauteur_case)*(561/self.ui.conteneur.height())),4)

        self.fenetre_aide = False

        if self.choix == 1:
        #application d'un déplacement
            if self.selection == True:
                self.pos_depl[0] = [i,j]
                if self.jeu.table_jeu[i,j]!=0:
                    if self.jeu.table_jeu[i,j].car() == self.jeu.joueurTour.typeAnimal:
                        self.selection = False
                        print('Choisissez une orientation en selectionnant une case adjacente')
                    else:
                        (print("Vous n'avez pas le droit de contrôler cette pièce"))
                else:
                    print('Vous ne pouvez pas contrôler un rocher')
            elif min(abs(self.pos_depl[0][0] - i),1) ^ min(abs(self.pos_depl[0][1] - j),1):
                self.pos_depl[1] = [i,j]
                self.selection = True
                ori=self.depl_case[self.pos_depl[1][0] - self.pos_depl[0][0]][self.pos_depl[1][1] - self.pos_depl[0][1]]
                if ori!=False:
                    self.jeu.deplacer(self.pos_depl[0][0], self.pos_depl[0][1], ori)
                else:
                    print('Vous devez indiquer une orientation en selectionnant une case adjacente')
                self.choix=0

        if self.choix == 2:
        #application d'une orientation
            if self.selection == True:
                self.pos_depl[0] = [i,j]
                if self.jeu.table_jeu[i,j]!=0:
                    if self.jeu.table_jeu[i,j].car() == self.jeu.joueurTour.typeAnimal:
                        self.selection = False
                        print('Choisissez une orientation en selectionnant une case adjacente')
                    else:
                        (print("Vous n'avez pas le droit de changer l'orientation de cette pièce"))
                else:
                    print("Vous ne pouvez pas changer l'orientation d'un rocher")
            elif min(abs(self.pos_depl[0][0] - i),1) ^ min(abs(self.pos_depl[0][1] - j),1):
                self.pos_depl[1] = [i,j]
                self.selection = True
                ori=self.depl_case[self.pos_depl[1][0] - self.pos_depl[0][0]][self.pos_depl[1][1] - self.pos_depl[0][1]]
                if ori!=False:
                    self.jeu.orientation(self.pos_depl[0][0], self.pos_depl[0][1],ori)
                else:
                    print('Vous devez indiquer une orientation en selectionnant une case adjacente')
                self.choix = 0

        if self.choix ==3 :
        #application d'une sortie
            self.pos[0] = i
            self.pos[1] = j
            if self.jeu.table_jeu[i, j] != 0:
                if self.jeu.table_jeu[i, j].car() == self.jeu.joueurTour.typeAnimal:
                    self.jeu.sortir(self.pos[0], self.pos[1])
                    self.choix = 0
                else:
                    (print("Vous n'avez pas le droit de sortir cette pièce"))
            else:
                print('Vous ne pouvez pas contrôler un rocher')

        if self.choix == 4:
        #application d'un placement
            if self.selection == True:
                self.pos_depl[0] = [i,j]
                if i in (0,4) or j in (0,4):
                    self.selection = False
                print('Choisissez une orientation en selectionnant une case adjacente')
            elif min(abs(self.pos_depl[0][0] - i),1) ^ min(abs(self.pos_depl[0][1] - j),1):
                self.pos_depl[1] = [i,j]
                self.selection = True
                ori=self.depl_case[self.pos_depl[1][0] - self.pos_depl[0][0]][self.pos_depl[1][1] - self.pos_depl[0][1]]
                if ori!=False:
                    self.jeu.placer(self.pos_depl[0][0], self.pos_depl[0][1],ori)
                else:
                    print('Vous devez indiquer une orientation en selectionnant une case adjacente')
                self.choix = 0
        self.ui.conteneur.update()


if __name__ == "__main__":

    # on créé une nouvelle application Qt
    app = QtWidgets.QApplication(sys.argv)
    
    # ici nous passons au constructeur de notre interface de jeu les
    # paramètres nb_ins, nb_tour, nb_nour mais on pourrait aussi
    # faire en sorte de les faire renseigner par l'utilisateur
    # au lancement de l'interface graphique.
    window = Interface_Siam_UI(5, 3, )
    
    # la fenêtre a été initialisée, tous les callbacks ont éte mis
    # en place (ou plutôt le seront, c'est votre travail), on affiche
    # la fenêtre
    window.show()
    
    # et on lance l'application
    sys.exit(app.exec_())