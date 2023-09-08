from datetime import datetime


class ViewPlayer:
    def display_player_menu(self):
        """Displays the Player menu and returns the user's choice"""

        while True:
            print("===============[MENU JOUEUR]===============")
            print("1. Créer un joueur")
            print("2. Consulter Joueurs par ordre alphabétique")
            print("3. Revenir au MENU PRINCIPAL")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3"]:
                if choice == "3":
                    print("Ok !")

                return choice

            else:
                print("Choix invalide !")

    def get_player_surname(self):
        """Displays field requested for player creation and returns the user's response"""

        while True:
            surname = str.capitalize(input("Nom de famille du joueur :"))

            if surname.isalpha() == False:
                print("Les caractères numériques ne sont pas acceptés")

                continue

            if len(surname) > 0:
                return surname

            else:
                print("Veuillez entrer un nom de famille.")

                continue

    def get_player_name(self):
        while True:
            name = str.capitalize(input("Prénom du joueur :"))

            if name.isalpha() == False:
                print("Les caractères numériques ne sont pas acceptés")

                continue

            if len(name) > 0:
                return name

            else:
                print("Veuillez entrer un prénom.")

                continue

    def get_player_date_of_birth(self):
        valid_birthday = False

        while valid_birthday == False:
            date_of_birth = input("Date de naissance au format JJ-MM-AAAA : ")

            try:
                formated_date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            except ValueError:
                print("Veuillez entrer une date valide au format JJ-MM-AAAA.")

                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
                return date_of_birth

            else:
                print("Vous devez avoir au moins 18 ans pour vous inscrire.")

    def get_player_national_chess_id(self):
        while True:
            national_chess_id = input("Identifiant national d échec de la fédération :")

            if len(national_chess_id) == 7:
                return national_chess_id

            else:
                len(national_chess_id) != 7
                print("Veuillez entrer un identifiant valide (7 caractères).")

    def get_player_score(self):
        pass

    def display_all_sort_by_surname(self, players: list):
        "Display list of all players ordered by surname (from model_player), with rich from base_view"

        title = f"[LISTE DES {len(players)} JOUEURS PAR ORDRE ALPHABETIQUE]"
        # self.view_base.table_settings(players, title)
