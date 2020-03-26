__authors__ = "Cyrine G"
__date__ = "31/12/2019"

"""Ce fichier permet de definir la partie du jeux et il est aussi celui qui contient la fct main.
 Pour executer le jeu tic-tac-toe il suffit de executer ce fichier."""

from plateau import Plateau
from joueur import Joueur

class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()    # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []       # La liste des deux joueurs (initialement une liste vide).
                                # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
                                    # Pendant le jeu et à chaque tour d'un joueur,
                                    # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def saisir_nombre(self, nb_min, nb_max):
        """Args:
                  nb_min (int): Un entier représentant le minimum du nombre à entrer.
                  nb_max (int): Un entier représentant le maximum du nombre à entrer.

              Returns:
                  int: Le nombre saisi par l'utilisateur après validation.
              """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."
        nbre = input("Entrez s.v.p. un nombre entre "+ str(nb_min) + " et "+ str(nb_max) + ":? ")
        while (not nbre.isnumeric() or int(nbre) not in range(nb_min,nb_max+1)):
            print("***Valeur incorrecte!***")
            nbre = input("Entrez s.v.p. un nombre entre "+ str(nb_min) + " et "+ str(nb_max) + ":? ")
        return int(nbre)

    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """
        pionStr = input("Selectionnez s.v.p. la forme de votre pion (X,O):?")
        while (pionStr not in ["O","X"]):
            print("***Valeur incorrecte!***")
            pionStr = input("Selectionnez s.v.p. la forme de votre pion (X,O):?")
        return pionStr

    def demander_postion(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        print(self.joueur_courant.nom, " : Entrez s.v.p. les coordonnees de la case a utiliser:\n")
        print("Numéro de la ligne:")
        ligne = self.saisir_nombre(0,2)
        print("Numéro de la colonne:")
        col =  self.saisir_nombre(0,2)
        while(not self.plateau.position_valide(ligne, col)) :
            print("***position n'est pas valide***\n")
            print(self.joueur_courant.nom, " : Entrez s.v.p. les coordonnees de la case a utiliser:\n")
            print("Numéro de la ligne:")
            ligne = self.saisir_nombre(0, 2)
            print("Numéro de la colonne:")
            col = self.saisir_nombre(0, 2)
        return ligne, col



    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."

        print(self.plateau.__str__())
        if self.joueur_courant.type =="Ordinateur":
                ligne, col = self.plateau.choisir_prochaine_case(self.joueur_courant.pion)
        else :
            ligne, col = self.demander_postion()

        self.plateau.selectionner_case(ligne, col, self.joueur_courant.pion)

    def jouer(self):
        print("Bienvenue au jeu Tic Tac Toe. \n")
        print("---------------Menu---------------\n")
        print("1- Jouer avec l'ordinateur.\n")
        print("2- Jouer avec une autre personne.\n")
        print("0- Quitter.\n")
        print("----------------------------------\n")

        # choix du mode de jeux

        mode = self.saisir_nombre(0,2)
        # initialisation des joueurs
        if mode == 0:
            print("***Merci et au revoir !***")
            return 0
        else :
            nom = input("Entrez s.v.p. votre nom:? ")
            pion = self.demander_forme_pion()
            player1 = Joueur(nom, "Personne", pion)

            # deduction du pion du joueur 2
            if player1.pion == "X":
                pion = "O"
            else:
                pion = "X"

            #creation du joueur 2 selon le mode choisit
            if mode == 1:
                player2 = Joueur("Colosse","Ordinateur",pion)
            if (mode == 2):
                nom = input("Entrez s.v.p. votre nom:? ")
                player2 = Joueur(nom, "Personne", pion)
            self.joueurs = [player1,player2]

            #si partie n'est pas finie, les joueur 1 et 2 joue a tour de role
            replay = "O"
            while replay == "O":
                partie.plateau.initialiser()
                while (self.plateau.non_plein()==True and self.plateau.est_gagnant(player1.pion)==False and self.plateau.est_gagnant(player2.pion)==False) :
                    self.joueur_courant = player1
                    print("c'est le tour maintenant de " + str(self.joueur_courant.type) + " " + self.joueur_courant.nom + "! \n")
                    self.tour(mode)
                    if self.plateau.est_gagnant(player1.pion) or self.plateau.non_plein()==False :
                        break
                    self.joueur_courant = player2
                    print("c'est le tour maintenant de " + str(self.joueur_courant.type) + " " + self.joueur_courant.nom + "! \n")
                    self.tour(mode)
                    if self.plateau.est_gagnant(player2.pion) or self.plateau.non_plein()==False :
                        break
                if (self.plateau.non_plein()==False) :
                    self.nb_parties_nulles+=1
                    print("Partie terminée! La partie est nulle \n ")
                    print("Partie gangner par "+ player1.nom + ": " + str(player1.nb_parties_gagnees))
                    print("Partie gangner par " + player2.nom + ": " + str(player2.nb_parties_gagnees))
                    print("Partie nulle : " + str(self.nb_parties_nulles) + " \n")

                if self.plateau.est_gagnant(player1.pion) == True:
                    player1.nb_parties_gagnees+=1
                    print("Partie terminée! Le joueur gagnant est : "+ player1.nom+ " \n ")
                    print("Partie gangner par " + player1.nom + ": " + str(player1.nb_parties_gagnees)+" \n")
                    print("Partie gangner par " + player2.nom + ": " + str(player2.nb_parties_gagnees)+" \n")
                    print("Partie nulle : "+ str(self.nb_parties_nulles)+ " \n")

                if (self.plateau.est_gagnant(player2.pion) == True):
                    player2.nb_parties_gagnees += 1
                    print("Partie terminée! Le joueur gagnant est : " + player2.nom+" \n")
                    print("Partie gangner par " + player1.nom + ": " + str(player1.nb_parties_gagnees)+" \n")
                    print("Partie gangner par " + player2.nom + ": " + str(player2.nb_parties_gagnees)+" \n")
                    print("Partie nulle : " + str(self.nb_parties_nulles) + " \n")
                replay = input("Voulez-vous recommencer (O,N)?")
                if replay == "N":
                    print("***Merci et au revoir !***")



            """Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """
if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()


