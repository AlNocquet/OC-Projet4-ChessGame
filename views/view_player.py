from .view_base import BaseView
from .view_base import BaseView, console as c

from datetime import datetime


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            self.player_menu_settings(
                f"================[ MENU JOUEUR ]================"
            )
            self.display_message(f"\n--- Tapez E pour revenir au menu précédent ---\n")

            print("1. Créer un joueur")
            print("2. Modifier un joueur")
            print("3. Supprimer un joueur")
            print("4. Consulter Joueurs par ordre alphabétique")
            print("5. Trouver un joueur par ID")
            print("6. Trouver un joueur par son Nom")
            print("Q. Quitter le programme")

            choice = input(f"\n Entrez votre choix :")

            if choice in ["1", "2", "3", "4", "5", "6", "E", "e", "Q", "q"]:
                if choice == "E" or choice == "e":
                    self.display_message(f"\n Ok !\n")

                elif choice == "Q" or choice == "q":
                    self.display_message(f"\n Au revoir !\n")

                return choice

            else:
                self.display_error_message(f"\n Choix invalide !\n")

    def get_new_player(self) -> dict:
        """Displays field requested for player creation and returns the user's response"""

        self.player_sections_settings(
            f"\n============[ CRÉATION DU JOUEUR ]============"
        )
        self.display_message(f"\n-- Tapez Exit pour revenir au menu précédent --\n")

        surname = self.get_alpha_string(label="Nom de famille du joueur")
        first_name = self.get_alpha_string(label="Prénom du joueur")
        date_of_birth = self.get_player_date_of_birth()
        national_chess_id = self.get_alphanum(
            "Identifiant national d échec de la fédération", min_len=7, max_len=7
        )
        score = self.get_player_number(label="Score")

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
                self.display_error_message(
                    f"\n Veuillez entrer une date valide au format JJ-MM-AAAA.\n"
                )
                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
                return date_of_birth

            else:
                self.display_error_message(
                    f"\n Vous devez avoir au moins 18 ans pour vous inscrire."
                )

    def get_player_updated(self):
        self.player_sections_settings(
            f"\n==========[ MODIFICATION DU JOUEUR ]=========="
        )
        self.display_message(f"\n-- Tapez Exit pour revenir au menu précédent --\n")
        self.request_player_by_id()

    def get_player_removed(self):
        self.player_sections_settings(
            f"\n==========[ SUPPRESSION DU JOUEUR ]=========="
        )
        self.display_message(f"\n-- Tapez Exit pour revenir au menu précédent --\n")
        self.request_player_by_id()

    def get_player_by_id(self):
        self.player_sections_settings(
            f"\n========[ RECHERCHE DU JOUEUR PAR ID ]========"
        )
        self.display_message(f"\n-- Tapez Exit pour revenir au menu précédent --\n")
        self.request_player_by_id()

    def request_player_by_id(self):
        return self.get_alphanum(label="Quel est l'ID du joueur recherché")

    def get_player_by_fullname(self):
        self.player_sections_settings(
            f"\n===[ RECHERCHE DU JOUEUR PAR NOM et PRENOM ]==="
        )
        self.display_message(f"\n-- Tapez Exit pour revenir au menu précédent --\n")
        self.request_player_by_fullname()

    def request_player_by_fullname(self):
        surname = self.get_alpha_string(
            label="Quel est le Nom de famille du joueur recherché"
        )
        first_name = self.get_alpha_string(
            label="Quel est le Prénom du joueur recherché"
        )

        return {"surname": surname, "first_name": first_name}

    def get_tournament_players_id(
        self, player_number: int, valid_players_id: list
    ) -> list[str]:
        """Return a list of players id enter by the user"""

        while True:
            players_id_str: str = self.get_alphanum(
                label=f"Veuillez indiquer les chess_id des {player_number} joueurs à ajouter séparés avec un espace [Enter pour annuler]:\n"
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

            c.print(f"len players_id = {len(players_id)}")
            if len(players_id) == player_number:
                return players_id

            c.print("\n dans viewPlayer. get_tournament_players_id")
            c.print(locals())
            print(
                f"\nSaisie invalide. Vous devez indiquer {player_number} identifiants"
            )
