from models.model_player import Player
from views.view_player import ViewPlayer
from views.view_base import BaseView

from colorama import Fore, Style
import os


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
                self.display_players_by_surname()
            elif choice == "3":
                exit_requested = True

    def create_player(self):
        """Get players datas (unpack dictionary) from view_player and save it from the model_player"""

        player = self.view.get_new_player()
        player = Player(**player)
        player.save()
        self.view.display_message(f"Joueur sauvegardé avec succès !")

    def display_players_by_surname(self):
        """Get players list from the model_player and display it with rich from base_view"""
        players = []
        for p in Player.get_all_sort_by_surname():
            p["score"] = str(p.get("score"))
            players.append(p)

        title = f"[LISTE DES {len(players)} JOUEURS PAR ORDRE ALPHABETIQUE]"
        BaseView.table_settings(title, players)
