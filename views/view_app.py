class ViewApp:
    def display_main_menu(self):
        """Affiche le menu principal et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print("===============[MENU PRINCIPAL]===============")
            print("1. Gestion des Tournois")
            print("2. Gestion des Joueurs")
            print("3. Quitter")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3"]:
                if choice == "3":
                    print("================[ Au revoir !]=================")
                return choice
            else:
                print("Choix invalide !")
