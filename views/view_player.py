from datetime import datetime
from .view_base import BaseView

from colorama import Fore, Style, Back


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            print(
                Fore.WHITE
                + Back.MAGENTA
                + Style.BRIGHT
                + "================[MENU JOUEUR]================"
                + Style.RESET_ALL
            )
            print("1. Créer un joueur")
            print("2. Consulter Joueurs par ordre alphabétique")
            print("3. Revenir au MENU PRINCIPAL")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3"]:
                if choice == "3":
                    print("\n     Ok !\n")

                return choice

            else:
                print(Fore.RED + "Choix invalide !" + Style.RESET_ALL)

    def get_new_player(self) -> dict:
        """Displays field requested for player creation and returns the user's response"""

        print(
            Fore.MAGENTA
            + Style.BRIGHT
            + "============[CRÉATION DU JOUEUR]============="
            + Style.RESET_ALL
        )

        surname = self.get_alpha_string(label="Nom de famille du joueur")
        first_name = self.get_alpha_string(label="Prénom du joueur")
        date_of_birth = self.get_player_date_of_birth()
        national_chess_id = self.get_alphanum(
            "Identifiant national d échec de la fédération", min_len=7, max_len=7
        )
        score = self.get_player_score()

        return {
            "surname": surname,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "national_chess_id": national_chess_id,
            "score": score,
        }

    def get_player_date_of_birth(self):
        valid_birthday = False

        while valid_birthday == False:
            date_of_birth = input("Date de naissance au format JJ-MM-AAAA : ")

            try:
                formated_date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            except ValueError:
                print(
                    Fore.RED
                    + "Veuillez entrer une date valide au format JJ-MM-AAAA."
                    + Style.RESET_ALL
                )

                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
                return date_of_birth

            else:
                print(
                    Fore.RED
                    + "Vous devez avoir au moins 18 ans pour vous inscrire."
                    + Style.RESET_ALL
                )

    def error_requesting_name(surname):
        BaseView.display_message(
            f"Désolé, {surname} ne fait pas partie des joueurs enregistrés."
        )

    def error_requesting_name_already_registered(surname):
        BaseView.display_message(f"Désolé, {surname} est déjà inscrit(e) au tournoi.")
