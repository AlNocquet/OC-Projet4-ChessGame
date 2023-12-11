from .view_base import BaseView
from models.model_round import Round
from datetime import datetime

from colorama import Fore, Style, Back


class ViewTournament(BaseView):
    def display_tournament_menu(self):
        """ "Display tournament's main menu and returns the user's response"""

        while True:
            print("\n")
            self.tournament_menu_settings(
                f"============================[ MENU TOURNOI ]============================"
            )
            self.display_message_section(
                f"\n                Tapez E pour revenir au menu précédent\n"
            )

            print("1. Créer un Tournoi")
            print("2. Charger un Tournoi")
            print("3. Afficher liste des Tournois")
            print("4. Consulter liste des ROUNDS d'un Tournoi")
            print("5. Consulter liste des MATCHS d'un Tournoi")
            print("Q. Quitter le programme")

            choice = input(
                Fore.BLACK
                + Style.BRIGHT
                + f"\n Entrez votre choix : "
                + Style.RESET_ALL
            )

            if choice in ["1", "2", "3", "4", "5", "6", "E", "e", "Q", "q"]:
                if choice.lower() == "e":
                    self.display_message(f"\n Ok !\n")

                elif choice.lower() == "q":
                    self.display_message(f"\n Au revoir !\n")

                return choice

            else:
                self.display_error_message(f"\n Choix invalide !\n")

    def request_new_tournament(self) -> dict:
        """Displays field requested for tournament creation and returns the user's response"""
        self.tournament_sections_settings(
            f"\n =========================[ CRÉATION DU TOURNOI ]======================== \n"
        )

        name = self.get_data_rounds(label="Nom du tournoi")
        place = self.get_data_rounds(label="Lieu du tournoi")
        date = self.get_date_rounds(label="Date du tournoi")
        number_of_rounds = self.get_int_rounds(label="Nombre de tours")
        number_of_players = self.get_int_rounds(label="Nombre de joueurs")
        description = self.get_data_rounds(
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

    def request_create_rounds(self, round: Round):
        """Request for rounds creation and returns the user's response"""

        choice = input(
            Fore.CYAN
            + Style.BRIGHT
            + f"\n Lancer nouveau round ? (Y/N) : "
            + Style.RESET_ALL
        )

        if choice.lower() == "n":
            self.display_message(f"\n Ok !")
            self.display_tournament_menu()

        elif choice.lower() == "y":
            self.display_message(f"\n GO !")
            return choice

        else:
            self.display_error_message(f"\n Choix invalide !\n")

    def request_add_scores(self, round: Round):
        """Request to add player's scores of each round and returns the user's response"""
        choice = input(
            Fore.CYAN
            + Style.BRIGHT
            + f"\n Enregistrer les scores ? (Y/N) : "
            + Style.RESET_ALL
        )

        if choice.lower() == "n":
            self.display_message(f"\n Ok !")
            self.display_tournament_menu()

        elif choice.lower() == "y":
            self.display_message(f"\n GO !")
            self.rounds_menu_settings(
                f"\n ---------------------[ Enregistrement scores du {round.name}]---------------------"
            )

            return choice

        else:
            self.display_error_message(f"\n Choix invalide !\n")

    def get_match_result(self):
        """Display choice of match results and returns the user's response"""

        self.display_message_score_section(
            f"\n Victoire Joueur 1 : Tapez 1 \n Victoire Joueur 2 : Tapez 2 \n Match Nul : Tapez 3 \n"
        )

        choice = input(
            Fore.BLACK + Style.BRIGHT + f"Entrez votre choix : " + Style.RESET_ALL
        )

        if choice in ["1", "2", "3"]:
            return choice

        else:
            self.display_error_message(f"\n Choix invalide !\n")

    def request_tournament_by_id(self):
        """Display tournament's menu section and field to return the user's response"""

        self.tournament_menu_settings(
            f"\n========[ RECHERCHE DU TOURNOI PAR ID ]========"
        )

        request = self.get_int(
            label="Voici le(s) tournoi(s) enregistré(s) : \n Lequel voulez vous charger ? \n"
        )
        return request
