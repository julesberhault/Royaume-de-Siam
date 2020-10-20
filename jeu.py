from tableau_de_jeu import Table_jeu
from joueur import Joueur
import winsound
import sys

"""
Classe permettant d'initialiser une partie et d'executer l'ensemble des actions basiques du jeu de Siam et d'agir
avec les pièces sur le plateau de jeu.
Elle est aussi munie d'un affiche rudimentaire du plateau, en temps réel, sur la console.
"""

class Partie():

    def __init__(self, xmax=5, ymax=5, nb_piece=5, nb_roc=3, music=False):
        self.table_jeu = Table_jeu(xmax,ymax,nb_roc).initialiserPlateau().table_jeu
        self.elephants = Joueur('M', nb_piece, self.table_jeu)
        self.rhinoceros = Joueur('H',nb_piece,self.table_jeu)
        self.joueurTour = self.elephants
        self.nb_tour_done = 0
        self.end=False
        self.music=music
        if self.music == True:  # lance la musique de fond, True signifie 'ON', False signifie 'OFF'
            winsound.PlaySound("donkey_kong_theme.wav", winsound.SND_ASYNC)

    def car(self):
        return "C'est au tour des "+self.joueurTour.car()

    def __str__(self):
        fleche={'N': '▲ ', 'E': '▶ ', 'S': '▼ ', 'O': '◀ '}
        Display=""
        for i in range(self.table_jeu.shape[0]):
            for j in range(self.table_jeu.shape[1]):
                if self.table_jeu[i,j]==0:
                    Display+='[   ]'
                elif self.table_jeu[i,j].car()=='R':
                    Display+='( '
                    Display+=self.table_jeu[i,j].car()
                    Display+=' )'
                else:
                    Display += '{'
                    Display += self.table_jeu[i, j].car()
                    Display += fleche[self.table_jeu[i, j].orientation]
                    Display += '}'
            Display += '\n'
        return Display

    def recommencer(self):
        self = Partie()
        print('La partie commence')
        print('')
        print(jeu)
        print(jeu.car())

    def tourSuivant(self):
        if self.music==False:
            winsound.PlaySound("place.wav", winsound.SND_ASYNC)
        if self.elephants.winner == True:
            print('')
            print(self)
            print('Les', self.elephants.car(), 'ont gagnés en', self.nb_tour_done, 'tours !')
            #lance le jingle de fin
            winsound.PlaySound("you_win.wav",winsound.SND_ASYNC)
            self.end = True
            #sys.exit(0)
        elif self.rhinoceros.winner == True:
            print('')
            print(self)
            print('Les', self.elephants.car(), 'ont gagnés en', self.nb_tour_done, 'tours !')
            #lance le jingle de fin
            winsound.PlaySound("you_win.wav",winsound.SND_ASYNC)
            self.end = True
            #sys.exit(0)
        else:
            self.nb_tour_done += 1
            if self.joueurTour.car() == 'éléphants':
                self.joueurTour = self.rhinoceros
            else:
                self.joueurTour = self.elephants
            # affichage du plateau de jeu à chaque tour
            print('')
            print(self)
            print(self.car())

    def placer(self, i, j, ori):
        if self.joueurTour.placer(i,j,ori)!=False:
            self.tourSuivant()

    def deplacer(self, i, j, ori):
        depl_case = {"O": [0, -1], "E": [0, 1], "N": [-1, 0],
                     "S": [1, 0]}
        inext = i + depl_case[ori][0]
        jnext = j + depl_case[ori][1]
        if self.table_jeu[i,j] == 0:
            print('La case est vide')
        elif self.table_jeu[i,j].car() == 'R':
            print('Vous ne pouvez pas déplacer un rocher')
        else:
            if self.table_jeu[i,j].car() == self.joueurTour.typeAnimal:
                if self.table_jeu[inext,jnext]==0:
                    self.table_jeu[i,j].deplacer(i,j,ori)
                    self.tourSuivant()
                else:
                    if ori == self.table_jeu[i,j].orientation:
                        if self.table_jeu[i,j].deplacer(i,j,ori)!=False:
                            self.tourSuivant()
                    else:
                        print("Pour pousser l'autre pièce votre animal doit être orienté dans la bonne direction")
            else:
                print("Vous n'avez pas le droit de déplacer cette pièce")

    def orientation(self, i, j, ori):
        if self.table_jeu[i,j] == 0:
            print('La case est vide')
        elif self.table_jeu[i,j].car() == 'R':
            print("Vous ne pouvez pas changer l'orientation d'un rocher")
        else:
            if self.table_jeu[i,j].car() == self.joueurTour.typeAnimal:
                if self.table_jeu[i,j].changer_orientation(i,j,ori)!=False:
                    self.tourSuivant()
            else:
                print("Vous n'avez pas le droit de déplacer cette pièce")

    def sortir(self, i, j):
        if self.table_jeu[i,j] == 0:
            print('La case est vide')
        elif self.table_jeu[i,j].car() == 'R':
            print('Vous ne pouvez pas controler un rocher')
        else:
            if self.table_jeu[i,j].car() == self.joueurTour.typeAnimal:
                if self.table_jeu[i,j].sortir(i,j)!=False:
                    self.tourSuivant()
            else:
                print("Vous n'avez pas le droit de sortir cette pièce")

if __name__ == "__main__":
    jeu = Partie()
    print('La partie commence')
    print('')
    print(jeu)
    print(jeu.car())