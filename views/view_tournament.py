from .view_base import BaseView
from models.model_round import Round
from models.model_match import Match

from colorama import Fore, Style


class ViewTournament(BaseView):
    def get_tournament_menu(self):
        """Display TOURNAMENT's MAIN MENU and returns the user's response"""

        while True:
            self.tournament_menu_settings(f"MENU TOURNOI")

            self.display_section_subtitles(f"Tapez E pour revenir au menu précédent")

            print("1. Créer un Tournoi")
            print("2. Charger un Tournoi")
            print("3. Afficher liste des Tournois (par date)")
            print("4. Consulter liste des ROUNDS d'un Tournoi")
            print("5. Consulter liste des MATCHS d'un Tournoi")
            print("Q. Quitter le programme")

            choice = self.get_user_answer(label=f"Entrez votre choix : ")

            valid_choice = ["1", "2", "3", "4", "5", "6", "e", "q"]

            if choice in valid_choice:
                return choice

            else:
                self.display_error_message(f"Choix invalide")

    def get_create_tournament(self) -> dict:
        """Displays field for tournament creation and returns the user's response"""

        self.tournament_sections_settings(f"CRÉATION DU TOURNOI ")

        print("\n")

        name = self.get_alphanum(label="Nom du tournoi")
        place = self.get_alpha_string(label="Lieu du tournoi")
        date = self.get_date(label="Date du tournoi")
        number_of_rounds = self.get_int(label="Nombre de tours")
        number_of_players = self.get_player_number(label="Nombre de joueurs")
        description = self.get_alphanum(
            label="Remarques générales (réservé au directeur)", max_len=300
        )

        return {
            "name": name,
            "place": place,
            "date": date,
            "number_of_rounds": number_of_rounds,
            "number_of_players": number_of_players,
            "description": description,
        }

    def get_current_match(self, round: Round, match: Match):
        """Displays round's name and 2 players of each match"""

        self.tournament_sections_settings(f"Scores du {round.name}")

        self.scores_section_settings_1(
            f"JOUEUR 1 :"
            + match.player_1.full_name
            + "\n"
            + "JOUEUR 2 :"
            + match.player_2.full_name
        )

        self.scores_section_settings_2(
            f"VICTOIRE JOUEUR 1 : Tapez 1"
            + "\n"
            + f"VICTOIRE JOUEUR 2 : Tapez 2"
            + "\n"
            + f"MATCH NUL : Tapez 3"
        )

    def get_choices_match_result(self, round: Round):
        """Displays choices of match results and returns the user's response"""

        choice = self.get_user_answer(label=f"Entrez votre choix : ")

        if choice in ["1", "2", "3"]:
            return choice

        else:
            self.display_error_message(f"Choix invalide")

    def get_tournament_id(self, valid_tournament_id):
        """Returns a list of tournaments' id enter by the user"""

        while True:
            tournament_id = input(
                Fore.WHITE
                + Style.DIM
                + "Indiquez l'id_db du tournoi à sélectionner : "
                + Style.RESET_ALL
            )
            print()

            if not tournament_id:
                return

            bad_id = []
            for db_id in tournament_id:
                if db_id not in valid_tournament_id:
                    bad_id.append(db_id)

            if len(bad_id) > 0:
                self.display_error_message(
                    f"Les identifiants suivants ne sont pas valides : {bad_id}"
                )

            else:
                self.display_error_message("Saisie invalide")
