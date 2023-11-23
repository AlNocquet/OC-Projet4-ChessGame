from .view_base import BaseView

from datetime import datetime


class ViewTournament(BaseView):
    def display_tournament_menu(self):
        """ "Display tournament's main menu and returns the user's response"""

        while True:
            self.tournament_menu_settings(
                f"\n ============================[ MENU TOURNOI ]============================"
            )
            self.display_message(f"\n--- Tapez E pour revenir au menu précédent ---\n")

            print("1. Créer un Tournoi")
            print("2. Afficher liste des Tournois")
            print("3. Consulter données d un Tournoi")
            print("4. Consulter liste Joueurs d un Tournoi par ordre alphabétique")
            print("5. Consulter liste des Tours d un Tournoi")
            print("6. Consulter liste des Matchs d un Tournoi")
            print("Q. Quitter le programme")

            choice = input(f"\n Entrez votre choix :")

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

        name = self.get_alphanum(label="Nom du tournoi")
        place = self.get_alpha_string(label="Lieu du tournoi")
        date = self.get_date(label="Date du tournoi")
        number_of_rounds = self.get_int(label="Nombre de tours")
        number_of_players = self.get_int(label="Nombre de joueurs")
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

    def request_create_rounds(self):
        """Request for rounds creation and returns the user's response"""
        choice = self.get_alpha_string(label="\n LANCER UN ROUND ? (Y/N)")

        if choice.lower() == "n":
            self.display_message(f"\n Ok !\n")

        elif choice.lower() == "y":
            self.display_message(f"\n Go !\n")
            self.rounds_menu_settings(
                f"\n -------------------------[ CRÉATION D'UN ROUND ]------------------------ \n"
            )

        else:
            self.display_error_message(f"\n Choix invalide !\n")

        return choice

    def request_add_scores(self):
        """Request to add player's scores of each round and returns the user's response"""
        choice = self.get_alpha_string(label="\n ENREGISTRER LES SCORES ? (Y/N)")

        if choice.lower() == "n":
            self.display_message(f"\n Ok !\n")

        elif choice.lower() == "y":
            self.display_message(f"\n Go !\n")
            self.rounds_menu_settings(
                f"\n ---------------------[ ENREGISTREMENTS DES SCORES ]--------------------- \n"
            )

        else:
            self.display_error_message(f"\n Choix invalide !\n")

        return choice

    def request_tournament_by_id(self):
        """Display tournament's menu section and field to return the user's response"""

        self.tournament_menu_settings(
            f"\n========[ RECHERCHE DU TOURNOI PAR ID ]========"
        )

        request = self.get_int(
            label="Voici le(s) tournoi(s) enregistré(s) : \n Lequel voulez vous charger ? \n"
        )
        return request
