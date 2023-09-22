from models.model_player import Player
from views.view_player import ViewPlayer
from views.view_base import BaseView, CancelError
from datas.data_player import DataPlayer

from colorama import Fore, Style
import os


class PlayerController:
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
                self.display_players_by_surname()
            elif choice == "5":
                self.player_by_id()
            elif choice == "6":
                self.player_by_surname()
            elif choice == "7":
                exit_requested = True
            elif choice == "Q" or choice == "q":
                exit()

    def create_player(self):
        """Get players datas (unpack dictionary) from view_player and save it from the model_player"""

        try:
            player = self.view.get_new_player()
            player = Player(**player)
            player.save()
            self.view.display_message(f"\n Joueur sauvegardé avec succès ! \n")

        except CancelError:
            self.view.display_message(f"\n Création du joueur annulée.\n")
            return

    def update_player(self, item, doc_id):
        """Update the player in the database (from data_player)"""

        try:
            self.view.get_update_player()
            self.view.requesting_player_by_surname()
            self.data.update_player_from_table()
            self.view.display_message(f"\n Joueur modifié avec succès ! \n")

        except CancelError:
            self.view.display_message(f"\n Modification du joueur annulée.\n")
            return

    def remove_player(self, item, doc_id):
        """Delete the player in the database (from data_player)"""

        try:
            self.view.get_remove_player()
            self.view.requesting_player_by_surname()
            self.data.remove_player_from_table()
            self.view.display_message(f"\n Joueur supprimé avec succès ! \n")

        except CancelError:
            self.view.display_message(f"\n Supression du joueur annulée.\n")
            return

    def display_players_by_surname(self):
        """Get players list from the model_player and display it with rich from base_view"""
        players = []
        for p in Player.get_all_sort_by_surname():
            p["score"] = str(p.get("score"))
            players.append(p)

        title = f"[LISTE DES {len(players)} JOUEURS PAR ORDRE ALPHABETIQUE]"
        BaseView.table_settings(title, players)

    def player_by_id(self):
        """Ask for player by id from view_player and get it from data_player"""
        try:
            self.view.get_player_by_id()
            self.view.requesting_player_by_id()
            player = self.data.get_player_by_doc_id()
            return player

        except ValueError:
            self.view.display_message(
                f"\n Désolé, cet ID ne fait pas partie de ceux enregistrés.\n"
            )
            return

    def player_by_surname(self):
        """Ask for player by surname from view_player and get it from data_player"""

        try:
            self.view.get_player_by_surname()
            self.view.requesting_player_by_surname()
            player = self.data.get_player_by_doc_id()
            return player

        except ValueError:
            self.view.display_message(
                f"\n Désolé, ce joueur ne fait pas partie de ceux enregistrés.\n"
            )
            return
