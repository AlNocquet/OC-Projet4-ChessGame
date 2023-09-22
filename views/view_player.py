from datetime import datetime
from .view_base import BaseView

from colorama import Fore, Style, Back


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            print(
                "\n"
                + Fore.WHITE
                + Back.MAGENTA
                + Style.BRIGHT
                + "================[MENU JOUEUR]================\n"
                + Style.RESET_ALL
            )
            print("1. Créer un joueur")
            print("2. Modifier un joueur")
            print("3. Supprimer un joueur")
            print("4. Consulter Joueurs par ordre alphabétique")
            print("5. Trouver un joueur par ID")
            print("6. Trouver un joueur par son Nom")
            print("7. Revenir au MENU PRINCIPAL")
            print("Q. Quitter le programme")

            choice = input("\n Entrez votre choix :")

            if choice in ["1", "2", "3", "4", "5", "6", "7", "Q", "q"]:
                if choice == "7":
                    print("\n     Ok !\n")

                elif choice == "Q" or choice == "q":
                    print("\n                  Au revoir !\n")

                return choice

            else:
                print(Fore.RED + "\n Choix invalide !\n" + Style.RESET_ALL)

    def get_new_player(self) -> dict:
        """Displays field requested for player creation and returns the user's response"""

        print(
            "\n"
            + Fore.MAGENTA
            + Style.BRIGHT
            + "============[CRÉATION DU JOUEUR]=============\n"
            + Style.RESET_ALL
        )
        print("  Tapez Exit pour revenir au menu précédent  \n")

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

    def get_update_player(self):
        print(
            "\n"
            + Fore.MAGENTA
            + Style.BRIGHT
            + "==========[MODIFICATION DU JOUEUR]==========\n"
            + Style.RESET_ALL
        )
        print("  Tapez Exit pour revenir au menu précédent  \n")

    def get_remove_player(self):
        print(
            "\n"
            + Fore.MAGENTA
            + Style.BRIGHT
            + "==========[SUPPRESSION DU JOUEUR]==========\n"
            + Style.RESET_ALL
        )
        print("  Tapez Exit pour revenir au menu précédent  \n")

    def get_player_by_id(self):
        print(
            "\n"
            + Fore.MAGENTA
            + Style.BRIGHT
            + "========[RECHERCHE DU JOUEUR PAR ID]========\n"
            + Style.RESET_ALL
        )
        print("  Tapez Exit pour revenir au menu précédent  \n")

    def get_player_by_surname(self):
        print(
            "\n"
            + Fore.MAGENTA
            + Style.BRIGHT
            + "=======[RECHERCHE DU JOUEUR PAR NOM]=======\n"
            + Style.RESET_ALL
        )
        print("  Tapez Exit pour revenir au menu précédent  \n")

    def requesting_player_by_surname(self):
        surname = self.get_alpha_string(
            label="Quel est le Nom de famille du joueur recherché"
        )
        return surname

    def requesting_player_by_id(self):
        id = self.get_alphanum(label="Quel est l'ID du joueur recherché")
        return id
