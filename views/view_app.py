from .view_base import BaseView


class ViewApp(BaseView):
    def display_main_menu(self):
        """Displays the MAIN MENU and returns the user's choice"""

        while True:
            self.main_menu_settings("MENU PRINCIPAL")
            self.display_section_subtitles("BIENVENU !")

            print("1. Gestion des Tournois")
            print("2. Gestion des Joueurs")
            print("Q. Quitter le programme")

            choice = self.get_user_answer(label="Entrez votre choix : ")

            valid_choice = ["1", "2"]

            if choice in valid_choice:
                return choice

            else:
                self.display_error_message("Choix invalide !")
