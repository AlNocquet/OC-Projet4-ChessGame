from models.model_player import Player
from views.view_player import ViewPlayer
from views.view_base import BaseView, CancelError, PlayerNotFound
from datas.data_player import DataPlayer


class PlayerController(BaseView):
    def __init__(self) -> None:
        self.view = ViewPlayer()
        self.data = DataPlayer()

    def manage_player(self):
        """Display the menu "GESTION DES JOUEURS" from view_player and return the user's choice"""

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
            elif choice.lower() == "e":
                exit_requested = True
            elif choice.lower() == "q":
                exit()

    def create_player(self):
        """Get players datas (unpack dictionary) from view_player and save it from the model_player"""

        try:
            player = self.view.get_new_player()
            player = Player(**player)
            player.save()
            self.view.display_success_message(f"Joueur sauvegardé avec succès !")

        except CancelError:
            self.view.display_message(f"Création du joueur annulée")
            return

    def update_player(self):
        """Update the player in the database (from data_player)"""

        while True:
            self.get_all_players_sorted_by_surname()
            player_id = self.view.get_player_updated()
            if player_id == "e":
                break
            field_to_update = self.view.get_fields_updated()
            self.data.update_player(field_to_update=field_to_update, id_db=[player_id])
            self.view.display_success_message(f"Joueur modifié avec succès !")

    def remove_player(self):
        """Delete the player in the database (from data_player)"""

        try:
            while True:
                self.get_all_players_sorted_by_surname()
                player_id = self.view.get_player_removed()
                if player_id == "e":
                    break
                Player.player_to_remove(id_db=player_id)
                self.view.display_success_message(f"Joueur supprimé avec succès !")

        except ValueError:
            self.view.display_error_message(
                f"Suppression impossible : Joueur en tournoi"
            )
            return

    def get_all_players_sorted_by_surname(self):
        """Get players list from the model_player and display it with rich from base_view"""
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
