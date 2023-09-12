from colorama import Fore, Style, Back


class ViewApp:
    def display_main_menu(self):
        """Affiche le menu principal et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print(
                Fore.WHITE
                + Back.RED
                + Style.BRIGHT
                + "===============[MENU PRINCIPAL]==============="
                + Style.RESET_ALL
            )
            print("1. Gestion des Tournois")
            print("2. Gestion des Joueurs")
            print("3. Quitter")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3"]:
                if choice == "3":
                    print("\n                  Au revoir !")
                return choice
            else:
                print("Choix invalide !")
