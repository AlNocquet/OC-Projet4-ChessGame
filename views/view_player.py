from datetime import datetime
from .view_base import BaseView

from colorama import Fore, Style, Back


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            print(
                Fore.WHITE
                + Back.MAGENTA
                + Style.BRIGHT
                + "================[MENU JOUEUR]================"
                + Style.RESET_ALL
            )
            print("1. Créer un joueur")
            print("2. Consulter Joueurs par ordre alphabétique")
            print("3. Revenir au MENU PRINCIPAL")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3"]:
                if choice == "3":
                    print("\n     Ok !\n")

                return choice

            else:
                print(Fore.RED + "Choix invalide !" + Style.RESET_ALL)

    def get_player_surname(self):
        """Displays field requested for player creation and returns the user's response"""

        while True:
            surname = str.capitalize(input("Nom de famille du joueur :"))

            # if surname.isalpha() == False:
            # print("Les caractères numériques ne sont pas acceptés")

            # continue

            if len(surname) > 0:
                return surname

            else:
                print(Fore.RED + "Veuillez entrer un nom de famille." + Style.RESET_ALL)

    def get_player_name(self):
        while True:
            name = str.capitalize(input("Prénom du joueur :"))

            # if name.isalpha() == False:
            # print("Les caractères numériques ne sont pas acceptés")

            # continue

            if len(name) > 0:
                return name

            else:
                print(Fore.RED + "Veuillez entrer un prénom." + Style.RESET_ALL)

    def get_player_date_of_birth(self):
        valid_birthday = False

        while valid_birthday == False:
            date_of_birth = input("Date de naissance au format JJ-MM-AAAA : ")

            try:
                formated_date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            except ValueError:
                print(
                    Fore.RED
                    + "Veuillez entrer une date valide au format JJ-MM-AAAA."
                    + Style.RESET_ALL
                )

                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
                return date_of_birth

            else:
                print(
                    Fore.RED
                    + "Vous devez avoir au moins 18 ans pour vous inscrire."
                    + Style.RESET_ALL
                )

    def get_player_national_chess_id(self):
        while True:
            national_chess_id = input("Identifiant national d échec de la fédération :")

            if len(national_chess_id) == 7:
                return national_chess_id

            else:
                len(national_chess_id) != 7
                print(
                    Fore.RED
                    + "Veuillez entrer un identifiant valide (7 caractères)."
                    + Style.RESET_ALL
                )

    def get_player_score(self):
        pass

    def get_player_surname_to_add(self):
        while True:
            surname = str.capitalize(input("Nom de famille du joueur à ajouter :"))

            # if name.isalpha() == False:
            # print("Les caractères numériques ne sont pas acceptés")

            if len(surname) > 0:
                return surname

            else:
                BaseView.display_message("Veuillez entrer un nom de famille.")

    def error_requesting_name(surname):
        BaseView.display_message(
            f"Désolé, {surname} ne fait pas partie des joueurs enregistrés."
        )

    def error_requesting_name_already_registered(surname):
        BaseView.display_message(f"Désolé, {surname} est déjà inscrit(e) au tournoi.")
