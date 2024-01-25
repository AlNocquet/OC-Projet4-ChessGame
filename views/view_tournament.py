from views.view_base import BaseView, CancelError, EXIT_CODE, QUIT_CODE
from models.model_round import Round
from models.model_match import Match

from colorama import Fore, Style


class ViewTournament(BaseView):
    def get_tournament_menu(self):
        """Display TOURNAMENT's MAIN MENU and returns the user's response"""

        while True:
            self.tournament_menu_settings(f"MENU TOURNOI")
            self.display_section_subtitles(
                "Tapez Exit pour revenir au menu précédent, Quit pour quitter le programme"
            )

            print("1. Créer un Tournoi")
            print("2. Charger un Tournoi")
            print("3. Afficher liste des Tournois (par date)")
            print("4. Consulter liste des ROUNDS d'un Tournoi")
            print("5. Consulter liste des MATCHS d'un Tournoi")

            choice = self.get_user_answer(label=f"Entrez votre choix : ")

            if choice in ["1", "2", "3", "4", "5", "exit", "quit"]:
                if choice.lower() == EXIT_CODE:
                    self.display_message(f"Ok !")

                if choice.lower() == QUIT_CODE:
                    self.display_message(f"Au revoir !")

                return choice

            else:
                self.display_error_message(f"Choix invalide")

    def display_fields_new_tournament(self) -> dict:
        """Displays fields for tournament's creation and returns the user's response"""

        self.tournament_sections_settings(f"CRÉATION DU TOURNOI ")
        self.display_section_subtitles(
            "Tapez Exit pour revenir au MENU TOURNOI, Quit pour quitter le programme"
        )

        name = self.get_alphanum(label="Nom du tournoi")
        place = self.get_alpha_string(label="Lieu du tournoi")
        start_date = self.get_date(label="Date du tournoi")
        number_of_rounds = self.get_int(label="Nombre de tours")
        number_of_players = self.get_player_number(label="Nombre de joueurs")
        description = self.get_alphanum(
            label="Remarques générales (réservé au directeur)", max_len=300
        )

        return {
            "name": name,
            "place": place,
            "start_date": start_date,
            "number_of_rounds": number_of_rounds,
            "number_of_players": number_of_players,
            "description": description,
        }

    def get_current_match(self, round: Round, match: Match):
        """Displays the current round and pair of players of each match"""

        self.tournament_sections_settings(f"Scores du {round.name}")

        self.match_players_settings(
            f"JOUEUR 1 :"
            + match.player_1.full_name
            + "\n"
            + "JOUEUR 2 :"
            + match.player_2.full_name
        )

        self.match_scores_settings(
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

    def get_tournament_id(self, valid_tournament_id: list[int]):
        """Displays field for the tournament's id and returns the user's response"""

        while True:
            tournament_id: int = input(
                Fore.BLUE
                + Style.BRIGHT
                + "\n"
                + "Indiquez l'id_db du tournoi à sélectionner : "
                + Style.RESET_ALL
            )

            if tournament_id in valid_tournament_id:
                return tournament_id

            # if tournament_id() == "exit":
            # raise CancelError

            # if tournament_id() == "quit":
            # self.display_message(f"Au revoir !")
            # exit()

            bad_id = []

            for id_db in tournament_id:
                if id_db not in valid_tournament_id:
                    bad_id.append(id_db)

                if len(id_db) > 0:
                    self.display_error_message(
                        f"L'identifiant {bad_id} n'est pas valide"
                    )

                else:
                    self.display_error_message("Saisie invalide")

            return tournament_id
