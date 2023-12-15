from .view_base import BaseView
from models.model_round import Round

from colorama import Fore, Style


class ViewTournament(BaseView):
    def get_tournament_menu(self):
        """Display TOURNAMENT's MAIN MENU and returns the user's response"""

        while True:
            self.tournament_menu_settings(f"MENU TOURNOI")

            self.display_section_subtitles(f"Tapez E pour revenir au menu précédent")

            print("1. Créer un Tournoi")
            print("2. Charger un Tournoi")
            print("3. Afficher liste des Tournois")
            print("4. Consulter liste des ROUNDS d'un Tournoi")
            print("5. Consulter liste des MATCHS d'un Tournoi")
            print("Q. Quitter le programme")

            choice = self.get_user_answer(label="\n Entrez votre choix : ")

            if choice in ["1", "2", "3", "4", "5", "6", "E", "e", "Q", "q"]:
                if choice.lower() == "E":
                    self.display_message(f"\n Ok !\n")

                elif choice.lower() == "Q":
                    self.display_message(f"\n Au revoir !\n")

                return choice

            else:
                self.display_error_message(f"\n Choix invalide !\n")

    def get_create_tournament(self) -> dict:
        """Displays field for tournament creation and returns the user's response"""

        self.tournament_sections_settings(f"CRÉATION DU TOURNOI")
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

    def get_create_round(self, round: Round):
        """Displays field for user's choice for round creation and returns the user's response"""

        choice = self.get_user_answer(f"Lancer le round ? (Y/N) : ")

        if choice in ["Y", "N", "y", "n"]:
            if choice.lower() == "N":
                self.display_message(f"\n Ok !\n")

                return choice

            else:
                self.display_error_message(f"\n Choix invalide !\n")

    def get_current_match(self, round: Round):
        """Displays round's name and 2 players of each match"""

        for match in round.matches:
            self.tournament_sections_settings(f"Enregistrement scores du {round.name}")

            self.tournament_sections_settings(
                f"JOUEUR 1 :"
                + match.player_1.full_name
                + "\n"
                + "JOUEUR 2 :"
                + match.player_2.full_name
            )

            self.tournament_sections_settings(
                f"\n Victoire Joueur 1 : Tapez 1 \n Victoire Joueur 2 : Tapez 2 \n Match Nul : Tapez 3 \n"
            )

    def get_choices_match_result(self, round: Round):
        """Displays choices of match results and returns the user's response"""

        choice = self.get_user_answer(label="\n Entrez votre choix ")

        if choice in ["1", "2", "3"]:
            return choice

        else:
            self.display_error_message(f"\n Choix invalide !\n")
