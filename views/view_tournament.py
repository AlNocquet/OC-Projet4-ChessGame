from .view_base import BaseView

from datetime import datetime
from colorama import Fore, Style, Back


class ViewTournament(BaseView):
    def display_tournament_menu(self):
        """Affiche le menu Tournoi et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print(
                Fore.WHITE
                + Back.BLUE
                + Style.BRIGHT
                + "================[MENU TOURNOI]================\n"
                + Style.RESET_ALL
            )

            print("1. Créer un Tournoi")
            print("2. Consulter données d un Tournoi")
            print("3. Consulter liste des Tournois")
            print("4. Consulter liste Joueurs d un Tournoi par ordre alphabétique")
            print("5. Consulter liste des Tours d un Tournoi")
            print("6. Consulter liste des Matchs d un Tournoi")
            print("7. Revenir au MENU PRINCIPAL")
            print("8. Quitter le programme")

            choice = input("\n Entrez votre choix :")

            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                if choice == "7":
                    print("\n     Ok !\n")

                if choice == "8":
                    print("\n                  Au revoir !")

                return choice

            else:
                print("Choix invalide !\n")

    def get_new_tournament(self) -> dict:
        """Displays field requested for tournament creation and returns the user's response"""
        print(
            Fore.CYAN
            + Style.BRIGHT
            + "============[CRÉATION DU TOURNOI]=============\n"
            + Style.RESET_ALL
        )

        name = self.get_alphanum(label="Nom du tournoi")
        place = self.get_alpha_string(label="Lieu du tournoi")
        date = self.get_date(label="Date du tournoi")
        description = self.get_alphanum(
            "Remarques générales (réservé au directeur)", max_len=300
        )

        return {
            "name": name,
            "place": place,
            "date": date,
            "description": description,
        }

    def create_tournament_false(player_table):
        print(
            "La base de données doit contenir 8 joueurs pour pouvoir créer un tournoi \n"
            f"Actuellement, elle contient {len(player_table)} joueurs"
        )
