from .view_base import BaseView

from colorama import Fore, Style, Back


class ViewApp(BaseView):
    def display_main_menu(self):
        """Affiche le menu principal et renvoie le résultat du choix de l'utilisateur"""

        while True:
            self.main_menu_settings(f"MENU PRINCIPAL")

            self.display_section_subtitles(f"BIENVENU !")

            print("1. Gestion des Tournois")
            print("2. Gestion des Joueurs")
            print("Q. Quitter le programme")

            choice = self.get_user_answer(label="Entrez votre choix : ")

            valid_choice = ["1", "2", "q"]

            if choice in valid_choice:
                return choice

            else:
                self.display_error_message(f"Choix invalide !")
