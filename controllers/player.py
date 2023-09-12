from models.model_player import Player
from views.view_player import ViewPlayer
from views.view_base import BaseView


class PlayerController:
    def __init__(self) -> None:
        self.view = ViewPlayer()

    def manage_player(self):
        """Display the menu "GESTION DES JOUEURS" from view_player and return the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = ViewPlayer.display_player_menu(self)

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.get_players_by_surname()
            elif choice == "3":
                exit_requested = True

    def create_player(self):
        """Get players datas and save it from the model_player"""
        surname = self.view.get_player_surname()
        first_name = self.view.get_player_name()
        date_of_birth = self.view.get_player_date_of_birth()
        national_chess_id = self.view.get_player_national_chess_id()
        total_score = 0
        player = Player(
            surname, first_name, date_of_birth, national_chess_id, total_score
        )
        player.save()

        return

    def get_players_by_surname(self):
        """Get players list from the model_player and display it with rich from base_view"""
        players = Player.get_all_sort_by_surname()
        title = f"[LISTE DES {len(players)} JOUEURS PAR ORDRE ALPHABETIQUE]"
        BaseView.table_settings(players, items=list)
        return
