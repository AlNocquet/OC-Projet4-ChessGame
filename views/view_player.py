from datetime import datetime


class ViewPlayer:
    def display_player_menu():
        """Affiche le menu Joueur et renvoie le résultat du choix de l'utilisateur"""

        while True:
            print("===============[MENU JOUEUR]===============")
            print("1. Créer un joueur")
            print("2. Consulter Joueurs par ordre alphabétique")
            print("3. Revenir au MENU PRINCIPAL")

            choice = input("Entrez votre choix :")

            if choice in ["1", "2", "3", "4"]:
                if choice == "4":
                    print("Ok !")

                return choice

            else:
                print("Choix invalide !")

    def get_player_surname():
        """Affiche le champs demandé pour création du joueur et renvoie le résultat de la réponse de l'utilisateur"""

        while True:
            surname = str.capitalize(input("Nom de famille du joueur :"))

            try:
                if int(surname):
                    print("Les caractères numériques ne sont pas acceptés")

            except ValueError:
                if len(surname) > 0:
                    return surname

            else:
                print("Veuillez entrer un nom de famille.")

    def get_player_name():
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

    def get_player_date_of_birth():
        valid_birthday = False

        while valid_birthday == False:
            date_of_birth = input("Date de naissance sous format JJ-MM-AAAA : ")

            try:
                formated_date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            except ValueError:
                print("Format de date invalide")
                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
            else:
                print("Vous devez avoir au moins 18 ans pour vous inscrire.")

            if len(date_of_birth) == 0:
                print("Veuillez entrer votre date de naissance.")

            return date_of_birth

    def get_player_national_chess_id():
        while True:
            national_chess_id = input("Identifiant national d échec de la fédération :")

            if len(national_chess_id) == 7:
                print(
                    "Veuillez entrer votre identifiant national d échec de la fédération."
                )
                return national_chess_id

            print("Veuillez entrer un identifiant valide.")

    def print_players_list_by_surname():
        pass

        # PARAMETRAGE AFFICHAGE TABLEAU
