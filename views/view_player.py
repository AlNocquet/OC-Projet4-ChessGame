from datetime import datetime
from .view_base import BaseView


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            self.player_menu_settings(
                f"\n ===============[ MENU JOUEUR ]===============\n"
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
                    self.display_message(f"\n Ok !\n")

                elif choice == "Q" or choice == "q":
                    self.display_message(f"\n Au revoir !\n")

                return choice

            else:
                self.display_error_message(f"\n Choix invalide !\n")

    def get_new_player(self) -> dict:
        """Displays field requested for player creation and returns the user's response"""

        self.player_sections_settings(
            f"\n ===========[ CRÉATION DU JOUEUR ]============\n  Tapez Exit pour revenir au menu précédent  \n"
        )

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
                self.display_error_message(
                    f"\n Veuillez entrer une date valide au format JJ-MM-AAAA.\n"
                )
                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
                return date_of_birth

            else:
                self.display_error_message(
                    f"\n Vous devez avoir au moins 18 ans pour vous inscrire."
                )

    def get_update_player(self):
        self.player_sections_settings(
            f"\n ==========[ MODIFICATION DU JOUEUR ]==========\n  Tapez Exit pour revenir au menu précédent  \n"
        )
        self.request_player_by_id()

    def get_remove_player(self):
        self.player_sections_settings(
            f"\n ==========[ SUPPRESSION DU JOUEUR ]==========\n  Tapez Exit pour revenir au menu précédent  \n"
        )
        self.request_player_by_id()

    def get_player_by_id(self):
        self.player_sections_settings(
            f"\n ========[ RECHERCHE DU JOUEUR PAR ID ]========\n  Tapez Exit pour revenir au menu précédent  \n"
        )
        self.request_player_by_id()

    def request_player_by_id(self):
        return self.get_alphanum(label="Quel est l'ID du joueur recherché")

    def get_player_by_fullname(self):
        self.player_sections_settings(
            f"\n ===[ RECHERCHE DU JOUEUR PAR NOM et PRENOM ]=== \n  Tapez Exit pour revenir au menu précédent  \n"
        )
        self.request_player_by_fullname()

    def request_player_by_fullname(self):
        surname = self.get_alpha_string(
            label="Quel est le Nom de famille du joueur recherché"
        )
        first_name = self.get_alpha_string(
            label="Quel est le Prénom du joueur recherché"
        )

        return {"surname": surname, "first_name": first_name}
