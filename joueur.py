import numpy as np
from piece import Piece,Animal

"""
Classe permettant la création d'un joueur. Chaque joueur possède ainsi 5 animauw qui lui sont instanciés dans une liste.
C'est la classe joueur qui place les pièces animal sur le plateau.
"""

class Joueur():

    def __init__(self, typeAnimal, nb_piece, table_jeu):
        self.__typeAnimal = typeAnimal
        self.nb_piece = nb_piece
        self.table_jeu = table_jeu
        listeAnimaux=np.zeros(nb_piece,dtype=Piece)
        for i in range(nb_piece):
            listeAnimaux[i]=Animal(table_jeu, 'N', typeAnimal, self)
        self.listeAnimaux=listeAnimaux
        self.winner=False

    def car(self):
        if self.typeAnimal == 'H':
            return 'rhinocéros'
        if self.typeAnimal == 'M':
            return 'éléphants'

    def __str__(self):
        return "%c : %i sur %i dans la reserve" %(self.car(), len(self.listeAnimaux), self.nb_piece)

    @property
    def typeAnimal(self):
        return self.__typeAnimal

    def placer(self, i, j, ori):
        if len(self.listeAnimaux) > 0:
            return self.listeAnimaux[0].placer(i, j, ori)
        else:
            print("Il n'y a plus de pièces",self.car(),"disponibles en stock")
            return False