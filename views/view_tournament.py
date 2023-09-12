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
                + "================[MENU TOURNOI]================"
                + Style.RESET_ALL
            )

            print("1. Créer un Tournoi")
            print("2. Consulter données d un Tournoi")
            print("3. Consulter liste des Tournois")
            print("4. Consulter liste Joueurs d un Tournoi par ordre alphabétique")
            print("5. Consulter liste des Tours d un Tournoi")
            print("6. Consulter liste des Matchs d un Tournoi")
            print("7. Revenir au MENU PRINCIPAL")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                if choice == "7":
                    print("\n     Ok !\n")

                return choice

            else:
                print("Choix invalide !")

    def get_tournament_name(self):
        """Affiche le champs demandé pour création du tournoi et renvoie le résultat de la réponse de l'utilisateur"""

        while True:
            name = str.capitalize(input("Nom du tournoi :"))

            if name.isalpha() == False:
                print("Les caractères numériques ne sont pas acceptés")

                continue

            if len(name) > 0:
                return name

            else:
                print("Veuillez entrer un nom de tournoi.")

                continue

    def get_tournament_place(self):
        while True:
            place = str.capitalize(input("Lieu du tournoi :"))

            if place.isalpha() == False:
                print("Les caractères numériques ne sont pas acceptés")

                continue

            if len(place) > 0:
                return place

            else:
                print("Veuillez entrer un nom de tournoi.")

                continue

    def get_tournament_date():
        valid_date = False

        while valid_date == False:
            tournament_date = input("Date du tournoi au format JJ-MM-AAAA : ")

            try:
                formated_date = datetime.strptime(tournament_date, "%d-%m-%Y")

            except ValueError:
                print("Veuillez entrer une date valide au format JJ-MM-AAAA.")

    def get_tournament_time_control():
        pass

    def get_tournament_description():
        description = str.capitalize(
            input("Remarques générales (réservé au directeur): ")
        )
        return description

    def create_tournament_false(player_table):
        print(
            "La base de données doit contenir 8 joueurs pour pouvoir créer un tournoi \n"
            f"Actuellement, elle contient {len(player_table)} joueurs"
        )

    def print_registered_tournaments(self):
        pass
