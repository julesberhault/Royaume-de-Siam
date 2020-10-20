import numpy as np
from piece import Piece,Rock

"""
Classe permettant la création d'un plateau de jeu, soit une matrice contenant les pièces du jeu.
"""

class Table_jeu():
    """
    Classe gérant le déroulement du jeu.
    """
    def __init__(self,xmax, ymax, nb_roc):
        self.xmax = max((xmax//2)*2+1,5)  # la longueur du plateau est impaire et d'au moins 5
        self.ymax = max((ymax//2)*2+1,5)  # la largeur du plateau est impaire et d'au moins 5
        self.nb_roc = max(1, min(self.ymax, nb_roc)) # le nombre de rocher n'excede pas la largeur du plateau
        self.table_jeu = np.zeros([self.xmax, self.ymax], dtype=Piece)

    def __str__(self):
        return ("il y a %i éléphants, %i rhinocéros sur le plateau"
                % ((self.elephants.nb_piece-len(self.elephants.listeAnimaux)),
                   (self.rhinoceros.nb_piece-len(self.rhinoceros.listeAnimaux))))

    def car(self):
        return self.table_jeu

    def initialiserPlateau(self):
        self.table_jeu = np.zeros([self.xmax, self.ymax], dtype=Piece)  # comment melanger deux type dans un tableau ??
        midx, midy=self.xmax//2, self.ymax//2  # indices de la case correspondant au centre du plateau
        for k in range(self.nb_roc):  # place les rochers un à un, en rangée, au milieu du plateau
            self.table_jeu[midx, midy+k-self.nb_roc//2]=Rock(self.table_jeu)
        return self

    def deplacer(self, piece, i, j, dir_depl):  # on recupère animal en cliquant sur le plateau
        piece.deplacer(i, j, dir_depl)

    def changerOrientation(self, animal, i, j, ori):
        animal.orientation(i, j, ori)

    def sortir(self, animal, i, j):
        animal.sortir(i, j)


