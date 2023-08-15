from datetime import datetime


class ViewPlayer:
    def display_player_menu(self):
        """Affiche le menu Joueur et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print("===============[MENU JOUEUR]===============")
            print("1. Créer un joueur")
            print("2. Modifier joueur")
            print("3. Consulter Joueurs par ordre alphabétique")
            print("4. Revenir au MENU PRINCIPAL")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3", "4"]:
                if choice == "4":
                    print("Ok !")

                return choice

            else:
                print("Choix invalide !")

    def get_player_surname(self):
        """Affiche le champs demandé pour création du joueur et renvoie le résultat de la réponse de l'utilisateur"""

        object_test = 0

        while True:
            surname = str.capitalize(input("Nom de famille :"))

            try:
                surname = int(surname)
                print("Les caractères numériques ne sont pas acceptés")

            except:
                object_test = +1
                print("Veuillez entrer un nom de famille.")

            return surname

    def get_player_name(self):
        object_test = 0

        while True:
            name = str.capitalize(input("Prénom du joueur :"))

            try:
                name = int(name)
                print("Les caractères numériques ne sont pas acceptés")

            except:
                object_test = +1
                return name

            else:
                print("Veuillez entrer un prénom.")

    def get_player_date_of_birth():
        test = 0
        while True:
            date_of_birth = str.capitalize(
                input("Date anniversaire du joueur : format jj/mm/aaaa")
            )

            try:
                date_of_birth = str(date_of_birth)
                print("Veuillez entrer des caractères numériques.")

            except:
                test == 0
                print("Veuillez entrer votre date d'anniversaire.")

            try:
                datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")

            except:
                print("Format invalide : format jj/mm/aaaa.")

            if date_of_birth == 0:
                print("Veuillez entrer votre date d'anniversaire.")

                continue

            if date_of_birth < 18:
                current_year = datetime.now()
                age = current_year - date_of_birth

                if age < 18:
                    print("Vous devez avoir 18 ans pour vous inscrire.")

                continue

            return date_of_birth

    def get_player_national_chess_id(self):
        while True:
            national_chess_id = str.capitalize(
                input("Identifiant national d échec de la fédération :")
            )

            if national_chess_id == 0:
                print(
                    "Veuillez entrer votre identifiant national d échec de la fédération."
                )

            return national_chess_id
