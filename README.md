# ROYAUME DE SIAM - REGLES ET AIDES
Développé par Jules Berhault et François Rouvrais (BERVRAIS) - 2018
_________________________________________________________________________

Vous êtes au Royaume de Siam, jadis, un véritable paradis sur Terre,
de vastes plaines fertiles où éléphants et rhinocéros vivaient en paix
depuis des siècles.
Un jour la terre se mit à trembler et Siam fut alors réduite à deux
régions séparées par de gigantesques montagnes.
Depuis, éléphants et rhinocéros n'ont pas assez d'espace pour vivre;
ces deux espèces d'une force incroyable vont alors se livrer à une lutte
sans merci pour régner sans partage sur le territoire de Siam.
_________________________________________________________________________

### Télécharger le jeu
Les fichiers de jeu sont disponibles au format zip depuis ce lien de téléchargement

[__Télécharger Royaume de Siam__](https://drive.google.com/file/d/1Ewji9YnUkGATurLBP4GbyJgloxJKE9oz/view?usp=sharing)

_________________________________________________________________________

/!\ Pour lancer le jeu, ouvrir le fichier "Jeu de Siam.py".
Il est préférable de lancer le programme sous Windows.
Il est aussi conseillé d'ajuster le volume de vos enceintes à un niveau
raisonnable. (L'écoute prolongée à un volume élevé peut endommager vos
facultés auditives, la musique est entrainante certes mais faites
attention à vos oreilles)

_________________________________________________________________________

![Main_menu](https://github.com/julesberhault/Royaume-de-Siam/blob/main/Snapshots/Main_menu.JPG)

_________________________________________________________________________

### But du jeu

Le premier joueur à sortir une montagne à l'extérieur plateau.
A savoir que ce n'est pas forcément le joueur qui provoque la sortie de
la montagne mais le joueur dont la pièce est la plus proche et orientée
dans la direction du déplacement.

_________________________________________________________________________

![In_game_2](https://github.com/julesberhault/Royaume-de-Siam/blob/main/Snapshots/In_game_2.JPG)
_________________________________________________________________________

### Comment jouer

Les joueurs jouent à tour de rôle. Au début, les joueurs sont disposés à
l'extérieur du plateau. Les éléphants, animaux sacrés du Royaume de Siam
commencent à jouer.
A chaque tour, les joueurs ne peuvent exécuter une des actions suivantes:
* Entrer un animal sur une des cases extérieures du plateau (cases vertes)
* Sortir un de ses animaux disposés sur une case extérieure (cases vertes)
* Se déplacer sur une case libre ou en poussant d'autres pièces disposées
sur le plateau (si la force nécessaire au déplacement est suffisante).

_________________________________________________________________________

![Help](https://github.com/julesberhault/Royaume-de-Siam/blob/main/Snapshots/Help.JPG)
_________________________________________________________________________

### PLACER un animal

Vous pouvez faire entre un de vos animaux par l'une des cases extérieures.
Si la case est libre, le mouvement est possible
Si la case est occupée vous devez pousser l'élément qui l'occupe mais
vous devez avoir la force nécessaire pour le déplacer (voir "déplacer").

/!\ Pour cela, cliquer sur le bouton "Placer", sélectionner la case sur
laquelle vous souhaitez placer votre animal en cliquant dessus
puis cliquer sur une seconde case, adjacente à la première, pour orienter
votre animal.

_________________________________________________________________________

![In_game](https://github.com/julesberhault/Royaume-de-Siam/blob/main/Snapshots/In_game.JPG)
_________________________________________________________________________

### Changer l'ORIENTATION d'un animal

Vous pouvez changer l'orientation d'un animal sans changer de case. Ce
coup compte pour un tour de jeu.

/!\ Pour cela, cliquer sur le bouton "Orientation", sélectionner la case
sur lequel votre animal est situé en cliquant dessus puis cliquer sur une
seconde case, adjacente à la première, pour réorienter votre animal.

Cas particulier:
/!\ Si vous souhaitez orienter votre animal vers l'extérieur du plateau
alors que votre animal se situe sur une des cases qui bordent le plateau,
il vous suffit de cliquer une première fois sur la case qu'occupe votre
animal pour le sélectionner, puis de cliquer sur la seconde case voisine
dans la direction opposée à celle que vous désirez.
_________________________________________________________________________

### SORTIR un animal

Vous pouvez sortir une pièce située sur une des cases extérieures du
plateau (cases vertes). L'animal pourra ensuite être replacé sur le
plateau aux tours suivants. Ce coup compte pour un tour de jeu.

/!\ Pour cela, cliquer sur le bouton "Sortir" puis cliquer sur la case
sur lequel votre animal est situé.
_________________________________________________________________________
 
### DEPLACER un animal

Vous pouvez déplacer un de vos animaux sur une case adjacente mais pas en
diagonale.
Si la case est libre, le mouvement est possible
Si la case est occupée vous devez pousser l'élément:
* vous ne pouvez pousser que dans la direction de votre animal
* un animal a la force de pousser un rocher
* un animal a la force de pousser un autre animal sauf si il lui fait face
* un animal peut pousser autant d'animaux que possible si ceux-ci ne sont
pas orientés dans une direction opposée
Transmission de force
* la force des animaux peux être cumulée sur une chaine (tant que cette
force est transmise)

/!\ Pour cela, cliquer sur le bouton "Déplacer", selectionner la case sur
lequel votre animal est situé en cliquant dessus puis cliquer sur une
seconde case, adjacente à la première, pour déplacer votre animal.

Précision:
Dans une direction donnée:
* la force d'un animal orienté dans la même direction que le déplacement
vaut 10
* la force d'un animal orienté dans une direction opposée au déplacement
vaut -10
* la force d'un animal orienté dans une direction othogonale au
déplacement vaut 0
* la force d'un rocher vaut dans tout les cas -9
Voilà maintenant vous n'avez plus qu'à faire le calcul !

_________________________________________________________________________

![You_win](https://github.com/julesberhault/Royaume-de-Siam/blob/main/Snapshots/You_win.JPG)
_________________________________________________________________________

### MUSIQUE
Vous pouvez jouer avec une musique de fond pour rendre vos parties plus
attrayantes ou vous pouvez tout autrement jouer dans le calme si
l'adversaire est trop fort pour vous et vous souhaitez disposer de toute
votre concentration!

/!\ Pour cela, rien de plus simple, cliquer sur le bouton "Musique". Vous
remarquerez que les pièces émettent un bruit lorsqu'elles se déplacent.
_________________________________________________________________________
