from .view_base import BaseView
from .view_base import BaseView, console as c

from datetime import datetime
from colorama import Fore, Style, Back


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            print("\n")
            self.player_menu_settings(f"MENU JOUEUR")

            self.display_section_subtitles(f"Tapez E pour revenir au menu précédent")

            print("1. Créer un joueur")
            print("2. Modifier un joueur")
            print("3. Supprimer un joueur")
            print("4. Consulter Joueurs par ordre alphabétique")
            print("Q. Quitter le programme")

            choice = self.get_user_answer(label=f"Entrez votre choix : ")

            if choice in ["1", "2", "3", "4", "Q", "q"]:
                if choice.lower() == "e":
                    self.display_message(f"Ok !")

                elif choice.lower() == "q":
                    self.display_message(f"Au revoir !")

                return choice

            else:
                self.display_error_message(f"Choix invalide")

    def get_new_player(self) -> dict:
        """Displays field requested for player creation and returns the user's response"""

        self.player_sections_settings(f"CRÉATION DU JOUEUR")

        print("\n")

        surname = self.get_alpha_string(label="Nom de famille du joueur")
        first_name = self.get_alpha_string(label="Prénom du joueur")
        date_of_birth = self.get_player_date_of_birth()
        national_chess_id = self.get_alphanum(
            "Identifiant national d échec de la fédération", min_len=7, max_len=7
        )

        return {
            "surname": surname,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "national_chess_id": national_chess_id,
        }

    def get_player_updated(self):
        pass

    def get_player_removed(self):
        pass

    def get_tournament_players_id(
        self, player_number: int, valid_players_id: list
    ) -> list[str]:
        """Returns a list of players id enter by the user - from Tournament Controller"""

        while True:
            players_id_str: str = input(
                Fore.WHITE
                + Style.DIM
                + f"\n Indiquez l'id_db des {player_number} joueurs à ajouter au tournoi, séparés par un espace : "
                + Style.RESET_ALL
            )

            if not players_id_str:
                return

            players_id: list = players_id_str.split()

            bad_id = []
            for db_id in players_id:
                if db_id not in valid_players_id:
                    bad_id.append(db_id)

            if len(bad_id) > 0:
                self.display_error_message(
                    f"\n Les identifiants suivants ne sont pas valides : {bad_id}"
                )
                continue

            if len(players_id) == player_number:
                return players_id

            else:
                self.display_error_message(
                    f"\n Saisie invalide. Vous devez indiquer {player_number} identifiants"
                )
