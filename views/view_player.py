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
        valid_birthday = False

        while valid_birthday == False:
            date_of_birth = str.capitalize(
                input("Date de naissance du joueur, format jj/mm/aaaa : ")
            )
            try:
                if len(date_of_birth) == 0:
                    print("Veuillez renseigner votre date de naissance.")

            except ValueError:
                if len(date_of_birth) > 0:
                    return date_of_birth

            try:
                formated_date = int
                if formated_date != datetime.strptime(date_of_birth, "%d-%m-%Y"):
                    continue

            except ValueError:
                print("Format invalide : utilisez le format jj/mm/aaaa.")

            now = datetime.now()

            if now.year - formated_date >= 18:
                valid_birthday = True
            else:
                print("Vous devez avoir 18 ans pour vous inscrire.")

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

    def print_players_list_by_surname(sorted_players):
        print(sorted_players)

    # PARAMETRAGE AFFICHAGE TABLEAU
