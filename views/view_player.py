from .view_base import BaseView
from .view_base import BaseView, console as c

from datetime import datetime
from colorama import Fore, Style


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            print("\n")
            self.player_menu_settings("MENU JOUEUR")

            self.display_section_subtitles("Tapez E pour revenir au menu précédent")

            print("1. Créer un joueur")
            print("2. Modifier un joueur")
            print("3. Supprimer un joueur")
            print("4. Consulter Joueurs par ordre alphabétique")
            print("Q. Quitter le programme")

            choice = self.get_user_answer(label=f"Entrez votre choix : ")

            if choice in ["1", "2", "3", "4", "e", "q"]:
                if choice.lower() == "e":
                    self.display_message(f"Ok !")

                elif choice.lower() == "q":
                    self.display_message(f"Au revoir !")

                return choice

            else:
                self.display_error_message(f"Choix invalide")

    def get_new_player(self) -> dict:
        """Displays field requested for player creation and returns the user's response"""

        self.player_sections_settings("CRÉATION DU JOUEUR")

        print("\n")

        surname = self.get_alpha_string(label=f"\n Nom de famille du joueur")
        first_name = self.get_alpha_string(label=f"\n Prénom du joueur")
        date_of_birth = self.get_player_date_of_birth()
        national_chess_id = self.get_alphanum(
            f"\n Identifiant national d échec de la fédération", min_len=7, max_len=7
        )

        return {
            "surname": surname,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "national_chess_id": national_chess_id,
        }

    def get_player_updated(self):
        """Returns a players id enter by the user to update it - from Tournament Controller"""

        self.player_sections_settings("MODIFICATION DU JOUEUR")
        self.display_section_subtitles("Tapez E pour revenir au menu précédent")

        player_id = input(
            Fore.MAGENTA
            + Style.BRIGHT
            + "\n Indiquez l'id_db du joueur à modifier dans la base : "
        )

        return player_id

    def get_fields_updated(self):
        """Displays fields requested for player update and returns the user's response"""

        while True:
            self.player_sections_messages_settings(
                f"Indiquez le champs à modifier : \n"
            )

            print("1. Nom de famille")
            print("2. Prénom")
            print("3. Date de naissance")
            print("4. Identifiant national d'échec de la fédération")

            choice = self.get_user_answer(label=f"Entrez votre choix : ")

            if choice in ["1", "2", "3", "4", "e"]:
                if choice == "1":
                    surname = self.get_alpha_string(
                        label=f"\n Nom de famille du joueur"
                    )
                    return {"surname": surname}

                elif choice == "2":
                    first_name = self.get_alpha_string(label=f"\n Prénom du joueur")
                    return {"first_name": first_name}

                elif choice == "3":
                    date_of_birth = self.get_player_date_of_birth()
                    return {"date_of_birth": date_of_birth}

                elif choice == "4":
                    national_chess_id = self.get_alphanum(
                        f"\n Identifiant national d échec de la fédération",
                        min_len=7,
                        max_len=7,
                    )
                    return {"national_chess_id": national_chess_id}

                elif choice.lower() == "e":
                    self.display_message(f"Ok !")
                    exit_requested = True

                return choice

            else:
                self.display_error_message(f"Choix invalide")

    def get_player_removed(self):
        """Returns a players id enter by the user to remove it - from Tournament Controller"""

        self.player_sections_settings(f"SUPPRESSION DU JOUEUR")
        self.display_section_subtitles("Tapez E pour revenir au menu précédent")

        players_id = input(
            Fore.MAGENTA
            + Style.BRIGHT
            + "\n Indiquez l'id_db du joueur à supprimer de la base : "
        )
        return players_id

    def get_tournament_players_id(
        self, player_number: int, valid_players_id: list
    ) -> list[str]:
        """Returns a list of players id enter by the user - from Tournament Controller"""

        while True:
            players_id_str: str = input(
                Fore.WHITE
                + Style.DIM
                + f"\n Indiquez l'id_db des {player_number} joueurs à ajouter au tournoi, séparés par un espace : "
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
