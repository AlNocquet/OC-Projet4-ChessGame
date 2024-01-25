from models.model_player import Player
from views.view_player import ViewPlayer
from views.view_base import BaseView, CancelError, EXIT_CODE, QUIT_CODE
from datas.data_player import DataPlayer


class PlayerController(BaseView):
    """Creates PlayerController object that centralizes the execution of the player part of the app"""

    def __init__(self) -> None:
        self.view = ViewPlayer()
        self.data = DataPlayer()

    def manage_player(self):
        """Manages the menu "GESTION DES JOUEURS" and returns the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = ViewPlayer.display_player_menu(self)

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
            self.view.display_success_message(f"Joueur sauvegardé avec succès !")

        except CancelError:
            self.view.display_message(f"Création du joueur annulée")
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
                self.view.display_success_message(f"Joueur modifié avec succès !")

        except CancelError:
            self.view.display_message(f"Modification du joueur annulée")
            return

    def remove_player(self):
        """Gets the player to delete"""

        try:
            while True:
                self.get_all_players_sorted_by_surname()
                player_id = self.view.get_player_id_to_remove()
                Player.remove(id_db=player_id)
                self.view.display_success_message(f"Joueur supprimé avec succès !")

        except ValueError:
            self.view.display_error_message(
                f"Suppression impossible : Joueur en tournoi"
            )

        except CancelError:
            self.view.display_message(f"Suppression du joueur annulée")

            return

    def get_all_players_sorted_by_surname(self):
        """Gets players list and display it with rich from base_view"""
        players = []
        for p in Player.get_all_sort_by_surname():
            p["score"] = str(p.get("score"))
            players.append(p)

        title = f"[LISTE DES {len(players)} JOUEURS PAR ORDRE ALPHABETIQUE]"

        headers = [
            "Nom",
            "Prénom",
            "Date Naissance",
            "National Chess Id",
            "id_db",
            "Score",
        ]
        self.view.table_settings(headers, title, players)

        return players
