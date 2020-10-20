#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import math
import numpy as np
from tableau_de_jeu import*
from piece import*
from joueur import*
from jeu import*
'''
La classe table_de_jeu, à besoin d'un joueur pour pouvoir déplacer des pièces, ici on vérifie les caractérisitques de la table mais la table est ici vide, (simplement avec des rochers).
'''
table_jeu1 = Table_jeu(5,5,3)
jeu = Partie()

class TestTableau_de_jeu(unittest.TestCase):
    def test_init(self):
        self.assertEqual(table_jeu1.xmax, 5)
        self.assertEqual(table_jeu1.ymax, 5)
        self.assertEqual(table_jeu1.nb_roc, 3)
        self.assertIsInstance(table_jeu1.initialiserPlateau().table_jeu, np.ndarray)
        
    def test_initialiserPlateau(self):
        for k in range(1,4):
            self.assertEqual(table_jeu1.initialiserPlateau().table_jeu[2,k].car(), 'R') #test: initialiserPlateau place bien les rochers au centre de la table
            self.assertEqual(jeu.orientation(0,1,'O'), None) # la case est vide
        
        
if __name__ == '__main__':
    unittest.main()
