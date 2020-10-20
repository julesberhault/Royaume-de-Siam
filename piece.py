from abc import ABCMeta
import numpy as np

"""
Classe permettant la création des classes des éléments du jeu, à savoir, un éléphant, un rhinocéros ou un rocher.
Cette classe ne peut être instanciée.
"""

class Piece(metaclass=ABCMeta):
    def __init__(self, table_jeu):
        self.table_jeu=table_jeu

    def car(self):
        return 'P'

    def __str__(self):
        return self.car()
    
    def bouger(self,i,j,dir_depl): # i et j sont les coordonnées de la pièce qui souhaite se déplacer
        depl_case={"O":[0,-1],"E":[0,1],"N":[-1,0],"S":[1,0]}
        inext=i+depl_case[dir_depl][0]
        jnext=j+depl_case[dir_depl][1]
        imax = self.table_jeu.shape[0]-1
        jmax = self.table_jeu.shape[1]-1
        if (inext > imax or jnext > jmax or 0 > inext or 0 > jnext):
            self.table_jeu[i,j].sortir(i,j)
        else:
            self.table_jeu[inext,jnext]=self
        if 4>=i>=0 and 4>=j>=0:
            self.table_jeu[i,j]=0


    def deplacer(self, i, j, dir_depl, sum_force=1): # i et j sont les coordonnées de la pièce qui souhaite se déplacer
        NESO = ['N', 'E', 'S', 'O']
        depl_case={"O":[0,-1],"E":[0,1],"N":[-1,0],"S":[1,0]} #vecteurs unitaires correspondant aux orientations
        inext=i+depl_case[dir_depl][0] #coordonnée que la pièce qui se deplace va atteindre
        jnext=j+depl_case[dir_depl][1]
        imax=self.table_jeu.shape[0]-1
        jmax = self.table_jeu.shape[1]-1
        if (inext>imax or jnext>jmax or 0>inext or 0>jnext): # si piece située sur le bord du plateau, on rentre dans le if
            if sum_force>0: # verifie la somme des forces obtenues par récursivité
                self.sortir(i,j)
                if self.car() == 'R': # si un rocher sort, le jeu s'arrete au tour suivant
                    self.winner(i,j,dir_depl)
            else:
                print("Mouvement impossible : force insuffisante pour le déplacement")
                return False
        else:
            next = self.table_jeu[inext, jnext]
            if next == 0: # case non occupée
                if sum_force>0:
                    self.bouger(i, j, dir_depl)
                else:
                    print("Mouvement impossible : force insuffisante pour le déplacement")
                    return False
            else : # transmission de force possible
                if next.car() in ['H', 'M']:
                    if next.orientation == dir_depl:
                        sum_force += 1
                    if abs(NESO.index(next.orientation)-NESO.index(dir_depl)) == 2:
                        sum_force -= 1
                if next.car() == 'R':
                    sum_force -=  0.9
                if next.deplacer(inext, jnext, dir_depl, sum_force) != False: #si la piece en aval a pu quitter sa case
                    self.bouger(i, j, dir_depl)
                else:
                    return False

    def winner(self,i,j,dir_depl): # determine qui a gagné en remontant la chaine
        depl_case = {"O": [0, -1], "E": [0, 1], "N": [-1, 0], "S": [1, 0]}
        iprev = i-depl_case[dir_depl][0]
        jprev = j-depl_case[dir_depl][1]
        if self.table_jeu[iprev,jprev].car() == 'R':
            self.winner(iprev,jprev,dir_depl)
        elif self.table_jeu[iprev,jprev].orientation != dir_depl:
            self.winner(iprev, jprev, dir_depl)
        else:
            self.table_jeu[iprev,jprev].joueur.winner = True

"""
Classe permettant la création d'un animal tel qu'un éléphant ou un rhinocéros. Elle contient des informations comme
son orientation, son type (espèce) ou le joueur à qui il appartient mais pas sa position sur le plateau.
La classe Animal hérite de la classe Pièce
"""

class Animal(Piece):

    def __init__(self, table_jeu, orientation, typeAnimal, joueur):
        super().__init__(table_jeu)
        self.__orientation=orientation
        self.__typeAnimal=typeAnimal
        self.joueur = joueur

    def car(self):
        if self.typeAnimal == 'M':
            return 'M'
        if self.typeAnimal == 'H':
            return 'H'

    def placer(self, i, j, ori): # i et j sont les coordonnées à atteindre
        nom_animal = {"H": 'rhinocéros', "M": 'éléphant'}
        imax=self.table_jeu.shape[0]-1
        jmax=self.table_jeu.shape[1]-1
        depl_case = {"O": [0, -1], "E": [0, 1], "N": [-1, 0], "S": [1, 0]}
        ctrl_ori={'N': [imax, None],'E': [None, 0], 'S': [0, None], 'O': [None, jmax]}
        if i in [0, imax] or j in [0, jmax]:
            iprev = i - depl_case[ori][0]
            jprev = j - depl_case[ori][1]
            if self.table_jeu[i,j] == 0:
                self.__orientation = ori
                self.table_jeu[i, j] = self
                self.joueur.listeAnimaux = np.delete(self.joueur.listeAnimaux, 0)
                print('Un', nom_animal[self.table_jeu[i, j].car()], 'a été placé sur le plateau')
            else:
                if i == ctrl_ori[ori][0] or j == ctrl_ori[ori][1]:
                    if self.table_jeu[i,j].deplacer(iprev, jprev, ori,sum_force=1) != False:
                        self.__orientation = ori
                        self.table_jeu[i,j] = self
                        self.joueur.listeAnimaux = np.delete(self.joueur.listeAnimaux, 0)
                        print('Un',nom_animal[self.table_jeu[i,j].car()],'a été placé sur le plateau')
                    else:
                        return False
                else:
                    print("Vous ne pouvez pousser d'autres pièces sur le plateau avec cette direction")
                    return False
        else:
            print('La pièce peut uniquement être placée sur les cases extérieures')
            return False
            
    def changer_orientation(self, i, j, ori):
        nom_dir = {"O": 'ouest', "E": 'est', "N": 'nord', "S": 'sud'}
        if self.table_jeu[i, j].__orientation == ori:
            print('La pièce', self.table_jeu[i, j], 'est déjà orientée dans la direction', nom_dir[ori])
            return False
        self.table_jeu[i, j].__orientation = ori
        print('La pièce', self.table_jeu[i, j], 'a été orientée dans la direction ', nom_dir[ori])

    def sortir(self,i,j):
        nom_animal = {"H": 'rhinocéros', "M": 'éléphant'}
        imax=self.table_jeu.shape[0]-1
        jmax=self.table_jeu.shape[1]-1
        if not(i in [0,imax] or j in [0,jmax]):
            print('Pour sortir, votre ', nom_animal[self.table_jeu[i, j].car()],
                  ' doit être positionné sur une case extérieure')
            return False
        self.joueur.listeAnimaux = np.append(self.joueur.listeAnimaux,self)
        self.table_jeu[i,j]=0
        print('Un',nom_animal[self.car()],'a été sorti du plateau')
        
    @property
    def orientation(self):
        return self.__orientation
    
    @orientation.setter
    def orientation(self, new_ori):
        NESO = ['N', 'E', 'S', 'O']
        if new_ori in NESO:
            self.orientation = new_ori

    @property
    def typeAnimal(self):
        return self.__typeAnimal

"""
Classe permettant la création d'un rocher. Elle hérite de la classe Pièce.
"""

class Rock(Piece):  # il faut definir deplacer dans rocher et animal
                    # et pas dans pièce car pas la meme facon de se deplacer

    def car(self):# ou définit on les forces
        return 'R'

    def sortir(self,i,j):
        self.table_jeu[i,j] = 0
        print('Un des rochers a été éjecté du plateau')
        # IMPORTANT !
        # un rocher est sorti du plateau : le joueur le plus proche gagne !

Plateau=np.array([[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],dtype=Piece)