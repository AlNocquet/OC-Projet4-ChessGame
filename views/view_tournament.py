from .view_base import BaseView

from datetime import datetime


class ViewTournament(BaseView):
    def display_tournament_menu(self):
        """Affiche le menu Tournoi et renvoie le résultat du choix de l'utilisateur"""

        while True:
            self.tournament_menu_settings(
                f"===============[ MENU TOURNOI ]==============="
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

    def get_new_tournament(self) -> dict:
        """Displays field requested for tournament creation and returns the user's response"""
        self.tournament_sections_settings(
            f"\n============[ CRÉATION DU TOURNOI ]=============\n"
        )
        # self.display_message(f"\n-- Tapez Exit pour revenir au menu précédent --\n")

        name = self.get_alphanum(label="Nom du tournoi")
        place = self.get_alpha_string(label="Lieu du tournoi")
        date = self.get_date(label="Date du tournoi")
        number_of_rounds = self.get_alphanum(label="Nombre de tours")
        number_of_players = self.get_alphanum(label="Nombre de joueurs")
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
        choice = self.get_alpha_string(
            label="\n Voulez-vous lancer un nouveau round ? (y/n)"
        )

        if choice.lower() == "n":
            self.display_message(f"\n Ok !\n")

        elif choice.lower() == "y":
            self.display_message(f"\n Go !\n")

        else:
            self.display_error_message(f"\n Choix invalide !\n")

        return choice

    def request_add_scores(self):
        """Request for player's scores of each round and returns the user's response"""
        choice = self.get_alpha_string(
            label="\n Voulez-vous enregistrer les scores du round ? (y/n) \n"
        )

        if choice.lower() == "n":
            self.display_message(f"\n Ok !\n")

        elif choice.lower() == "y":
            self.display_message(f"\n Go !\n")

        else:
            self.display_error_message(f"\n Choix invalide !\n")

        return choice
