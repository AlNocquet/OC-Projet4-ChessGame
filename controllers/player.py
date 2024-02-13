from colorama import Fore, Style

from datas.data_player import DataPlayer
from models.model_player import Player
from views.view_base import EXIT_CODE, QUIT_CODE, CancelError
from views.view_player import ViewPlayer


class PlayerController:
    """Creates PlayerController object that centralizes the execution of the player part of the app"""

    def __init__(self) -> None:
        self.view = ViewPlayer()
        self.data = DataPlayer()

    def manage_player(self):
        """Manages the menu "GESTION DES JOUEURS" and returns the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.display_player_menu()

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.update_player()
            elif choice == "3":
                self.remove_player()
            elif choice == "4":
                self.get_all_players_sorted_by_surname()
            elif choice.lower() == EXIT_CODE:
                exit_requested = True
            elif choice.lower() == QUIT_CODE:
                exit()

    def create_player(self):
        """Gets players' datas and saves them"""

        try:
            player = self.view.display_fields_new_player()
            player = Player(**player)
            player.save()
            self.view.display_success_message("Joueur sauvegardé avec succès !")
            print(
                "\n"
                + Fore.MAGENTA
                + Style.DIM
                + f"{player.full_name}"
                + " "
                + f"{player.date_of_birth}"
                + " "
                + f"{player.national_chess_id}"
                + Style.RESET_ALL
            )

        except CancelError:
            self.view.display_message("Création du joueur annulée")
            return

    def update_player(self):
        """Gets players' datas to update"""

        try:
            while True:
                self.get_all_players_sorted_by_surname()
                player_id = self.view.get_player_id_to_update()
                field_to_update = self.view.display_fields_player_to_update()
                self.data.update_data_player(
                    field_to_update=field_to_update, id_db=[int(player_id)]
                )
                self.view.display_success_message("Joueur modifié avec succès !")

        except CancelError:
            self.view.display_message("Modification du joueur annulée")
            return

    def remove_player(self):
        """Gets the player to delete"""

        try:
            while True:
                self.get_all_players_sorted_by_surname()
                player_id = self.view.get_player_id_to_remove()
                Player.remove(id_db=player_id)
                self.view.display_success_message("Joueur supprimé avec succès !")

        except ValueError:
            self.view.display_error_message(
                "Suppression impossible : Joueur en tournoi"
            )

        except CancelError:
            self.view.display_message("Suppression du joueur annulée")
            return

    def get_all_players_sorted_by_surname(self):
        """Gets players list and display it with rich from base_view"""
        players = []
        for p in Player.get_all_sort_by_surname():
            # Enlève score de la liste d'affichage / pop élèment hors de la liste des valeurs de l'objet Player
            p.pop("score")
            players.append(p)

        title = f"[LISTE DES {len(players)} JOUEURS PAR ORDRE ALPHABETIQUE]"

        headers = [
            "Nom",
            "Prénom",
            "Date Naissance",
            "National Chess Id",
            "id_db",
        ]
        self.view.table_settings(headers, title, players)

        input("Tapez Entrée pour continuer :")

        return players
