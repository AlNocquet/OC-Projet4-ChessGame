from .view_base import BaseView

from colorama import Fore, Style, Back


class ViewApp(BaseView):
    def display_main_menu(self):
        """Affiche le menu principal et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print("\n")
            self.main_menu_settings(
                f"=============================[MENU PRINCIPAL]==========================="
            )

            self.display_message_section(
                f"\n       BIENVENU, BIENVENU ! Et ! Que le sort vous soit favorable ! \n"
            )

            print("1. Gestion des Tournois")
            print("2. Gestion des Joueurs")
            print("Q. Quitter le programme")

            choice = input(
                Fore.BLACK
                + Style.BRIGHT
                + f"\n Entrez votre choix : "
                + Style.RESET_ALL
            )

            if choice in ["1", "2", "Q", "q"]:
                if choice.lower() == "q":
                    self.display_message(f"\n Au revoir !\n")
                return choice
            else:
                self.display_error_message(f"\n Choix invalide !\n")
