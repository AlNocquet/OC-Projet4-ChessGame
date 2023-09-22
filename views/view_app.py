from colorama import Fore, Style, Back


class ViewApp:
    def display_main_menu(self):
        """Affiche le menu principal et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print(
                "\n"
                + Fore.WHITE
                + Back.RED
                + Style.BRIGHT
                + "===============[MENU PRINCIPAL]===============\n"
                + Style.RESET_ALL
            )
            print("1. Gestion des Tournois")
            print("2. Gestion des Joueurs")
            print("Q. Quitter le programme")

            choice = input("\n Entrez votre choix :")

            if choice in ["1", "2", "Q", "q"]:
                if choice == "Q" or choice == "q":
                    print("\n                  Au revoir !\n")
                return choice
            else:
                print(Fore.RED + "\n Choix invalide !\n" + Style.RESET_ALL)
