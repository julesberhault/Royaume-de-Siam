#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import math
from tableau_de_jeu import*
from piece import *
from joueur import*

'''
Le joueur va pouvoir agir sur la table en déplaçant des pièces, il faut donc ici tester les caractéristique de Joueur mais aussi l'influence de l'application des fonctions du jeu sur les caractéristiques d'un Joueur (ex: l'appel de placer fait baisser le nb de pièce à la disposition du joueur)
'''


table_jeu1 = Table_jeu(5,5,3).initialiserPlateau().table_jeu
Joueur1 = Joueur('M', 5, table_jeu1)

class TestJoueur(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Joueur1.typeAnimal,'M')
        self.assertEqual(Joueur1.nb_piece,5)
        self.assertIsInstance(Joueur1,Joueur)
        
    def test_Placer(self):
        for k in range(5):
            Joueur1.placer(0,k,'S')
            self.assertEqual(len(Joueur1.listeAnimaux),5-k-1) # on vérifie que lorqu'un joueur place un animal sur le plateau, il en a un en moins dans sa reserve de 5 animaux
            
        L=len(Joueur1.listeAnimaux)
        L=0
        self.assertEqual(Joueur1.placer(1,0,'E'),False) #si le joueur n'a plus d'animaux en réserve il ne peut plus en placer sur le plateau.
        
if __name__ == '__main__':
    unittest.main()