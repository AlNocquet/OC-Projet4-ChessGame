class ViewTournament:
    def display_tournament_menu(self):
        """Affiche le menu Tournoi et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print("===============[MENU JOUEUR]===============")
            print("1. Créer un Tournoi")
            print("2. Consulter données d un Tournoi")
            print("3. Consulter liste des Tournois")
            print("4. Consulter liste Joueurs d un Tournoi par ordre alphabétique")
            print("5. Consulter liste des Tours d un Tournoi")
            print("6. Consulter liste des Matchs d un Tournoi")
            print("7. Revenir au MENU PRINCIPAL")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                if choice == "7":
                    print("Ok !")

                return choice

            else:
                print("Choix invalide !")
