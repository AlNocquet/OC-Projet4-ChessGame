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

        while True:
            surname = str.capitalize(input("Nom de famille :"))
            try:
                if int(surname):
                    print("Les caractères numériques ne sont pas acceptés")

            except ValueError:
                if len(surname) > 0:
                    return surname

                else:
                    print("Veuillez entrer un nom de famille.")

    def get_player_name(self):
        while True:
            name = str.capitalize(input("Prénom du joueur :"))
            try:
                if int(name):
                    print("Les caractères numériques ne sont pas acceptés")

            except ValueError:
                if len(name) > 0:
                    return name

                else:
                    print("Veuillez entrer un prénom.")

    def get_player_date_of_birth(self):
        while True:
            date_of_birth = str.capitalize(
                input("Date de naissance du joueur, format jjmmaaaa : ")
            )
            try:
                if len(date_of_birth) == 0:
                    print("Veuillez renseigner votre date de naissance.")

            except ValueError:
                if len(date_of_birth) > 0:
                    return date_of_birth

            try:
                if date_of_birth != datetime.strptime(date_of_birth, "%d/%m/%Y"):
                    print("Format invalide : utilisez le format jj/mm/aaaa.")

            except ValueError:
                if len(date_of_birth) > 0:
                    return date_of_birth

            try:
                current_year = datetime.now()
                age = current_year - date_of_birth

                if age < 18:
                    print("Vous devez avoir 18 ans pour vous inscrire.")

            except ValueError:
                if len(date_of_birth) > 0:
                    return date_of_birth

    def get_player_national_chess_id(self):
        while True:
            national_chess_id = str.capitalize(
                input("Identifiant national d échec de la fédération :")
            )
            try:
                if len(national_chess_id) == 0:
                    print(
                        "Veuillez entrer votre identifiant national d échec de la fédération."
                    )

            except ValueError:
                return national_chess_id
