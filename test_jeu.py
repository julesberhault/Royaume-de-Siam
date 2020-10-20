#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import math
from tableau_de_jeu import*
from piece import *
from joueur import*
from jeu import*

'''
Le jeu oppose les deux joueurs, il faut donc tester le constructeur de Jeu mais aussi, comment les joueurs vont jouer, passer d'un tour à l'autre, quel est l'impact sur le plateau de l'appel d'une fonction comme déplacer (est ce que les animaux se sont déplacer correctement sur le plateau ??)
'''


class TestPartie(unittest.TestCase):
    def test_init(self):
        jeu = Partie()
        Table=Table_jeu(5,5,3).initialiserPlateau().table_jeu
        J1= jeu.elephants
        J2= jeu.rhinoceros

        self.assertIsInstance(jeu.elephants, Joueur)
        self.assertIsInstance(jeu.rhinoceros, Joueur)
        self.assertEqual(jeu.joueurTour, jeu.elephants)
        self.assertEqual(jeu.nb_tour_done, 0)
    
    def test_tourSuivant(self):
        jeu = Partie()
        Table=Table_jeu(5,5,3).initialiserPlateau().table_jeu
        J1= jeu.elephants
        J2= jeu.rhinoceros
        for k in range(2):
            jeu.tourSuivant()
            self.assertEqual(jeu.nb_tour_done, k+1) #on vérifie que le nb de tour est bien décompté
            
        self.assertEqual(jeu.joueurTour, J1) #on vérifie qu'après 2 tour, c'est bien aux éléphants de jouer
        
    def test_placer(self):
        jeu = Partie()
        J1= jeu.elephants
        J2= jeu.rhinoceros
        for k in range (1,4):
            for i in range(1,4):
                self.assertEqual(jeu.placer(k,i,'N'),None) # on ne peut pas placer de pièce au centre du plateau
        jeu.placer(0,1,'S') #tour des éléphants
        self.assertEqual(jeu.table_jeu[0,1].typeAnimal,'M') #on vérifie que l'animal placer est bien celui désiré
        self.assertEqual(jeu.table_jeu[0,1].orientation,'S')
        self.assertEqual(jeu.table_jeu[0,1].joueur,J1)
        self.assertEqual(jeu.placer(0,1,'S'), None) #tour des rhinos: on ne peut pas placer deux animaux dans la même case
        self.assertEqual(jeu.placer(0,0, 'N'),None) #on ne peut pas insérer une pièce par le 'haut' du tableau orienté vers le nord
        
    def test_orientation(self):
        jeu = Partie()
        self.assertEqual(jeu.orientation(2,1,'S'), None) #on ne peut pas changer l'orientation d'un rocher
        self.assertEqual(jeu.orientation(0,0,'S'), None)
        jeu.placer(0,1,'S') #tour Elephant
        jeu.placer(0,2,'S') #tour Rhino
        jeu.orientation(0,1,'E')
        self.assertEqual(jeu.orientation(0,2,'S'), None) # la pièce est déjà orientée vers le sud donc changer_orientation de Pièce renvoie False
        self.assertEqual(jeu.table_jeu[0,1].orientation, 'E') #tour Elephant, le changement d'orientation peut il exceder 90 deg en 1 application de la fonction changer orientation
        self.assertEqual(jeu.orientation(0,1,'S'), None) # c'est au tour des Rhinos mais les Rhinos veulent modifier l'orientation d'un Elephant = INTERDIT
        
    def test_deplacer(self):
        jeu = Partie()
        jeu.placer(0,1,'S') #tour Elephant
        jeu.placer(0,2,'S') #tour Rhino
        jeu.deplacer(0,1,'S')
        self.assertEqual(jeu.table_jeu[1,1].typeAnimal, 'M')# on regarde si l'animal s'est bien déplacer
        self.assertEqual(jeu.deplacer(2,2,'S'), None)
        
        ''' 
        on va tester une opposition entre deux éléphants et un rhinocéros pour voir si la fonction déplacer est opérationelle"
        '''
        jeu = Partie() # on réinitialise le plateau
        jeu.placer(0,1,'S') #tour Elephant
        jeu.placer(0,3,'S') #tour Rhino
        jeu.placer(0,2,'S') #tour Elephant
        jeu.orientation(0,3,'O')
        jeu.orientation(0,2,'E')
        jeu.placer(2,0,'E')
        jeu.orientation(0,1,'E')
        jeu.placer(3,0,'E')
        jeu.deplacer(0,1,'E') # le déplacement est possible si tout marche bien
        
        jeu = Partie()
        jeu.placer(0,1,'S')
        self.assertEqual(jeu.deplacer(0,1,'S'), None) #le joueur Rhino essaie de deplacer une piece du joueur Elephant
        jeu.placer(0,2,'S')
        self.assertEqual(jeu.deplacer(0,1,'E'), None)
        
    def test_sortir(self):
        jeu = Partie()
        jeu.placer(0,1,'S') #tour Elephant
        jeu.placer(0,3,'S')
        jeu.deplacer(0,1,'S')
        jeu.sortir(0,3)
        self.assertEqual(len(jeu.rhinoceros.listeAnimaux), 5) # on vérifie que le joueur a bien récupéré sa pièce dans sa réserve
        self.assertEqual(jeu.table_jeu[0,3], 0) # on vérifie que le rhinoceros a bien été sorti du plateau
        self.assertEqual(jeu.sortir(1,1), None) # la pièce n'étant pas sur les bords du plateau, elle ne peut pas sortir, donc la fonction sortir de la classe Pièce renvoie False.
        
if __name__ == '__main__':
    unittest.main()

        
        