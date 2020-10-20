#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import math
from tableau_de_jeu import*
from piece import *
from joueur import*
from jeu import*

''' 
Une pièce ne se déplace pas sans plateau ni joueur qui lui applique des directives, ici il faut donc simplement tester les caractéristique d'une pièce sans plateau de jeu
'''

table_jeu = Table_jeu(5,5,3).initialiserPlateau().table_jeu
Joueur1 = Joueur('M', 5, table_jeu)

class TestPiece(unittest.TestCase):
    def test_init(self):
        A1 = Animal(table_jeu, 'N', 'M', Joueur1)
        self.assertEqual(A1.orientation, 'N')
        self.assertEqual(A1.typeAnimal, 'M')
        self.assertEqual(A1.joueur, Joueur1)
        self.assertIsInstance(A1, Animal)


if __name__ == '__main__':
    unittest.main()
