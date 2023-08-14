from .base_view import BaseView
from datetime import datetime


class ViewPlayer(BaseView):
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

    def get_player_data(self):
        """Affiche les champs demandés pour création du joueur et renvoie le résultat des réponses de l'utilisateur"""

        print("============[Création joueur]============")

        player_data = {}

        player_data["surname"] = str.capitalize(input("Nom du joueur :"))
        if self.is_string_valid(player_data["surname"], 3):
            pass

        player_data["first_name"] = str.capitalize(input("Prénom du joueur :"))
        player_data["date_of_birth"] = str.capitalize(
            input("Date anniversaire du joueur : jj/mm/aaaa")
        )
        player_data["national_chess_id"] = str.capitalize(
            input("Identifiant national d échec de la fédération :")
        )

        return player_data
