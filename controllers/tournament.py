from models.model_tournament import Tournament
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer
from views.view_base import BaseView
from datas.data_player import DataPlayer
from controllers.player import PlayerController

from colorama import Fore, Style, Back  # ,init


class TournamentController:
    def __init__(self) -> None:
        self.view = ViewTournament()
        self.view_player = ViewPlayer()

    def manage_tournament(self):
        """Displays the menu "GESTION DES TOURNOIS" from view_tournament and return the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.display_tournament_menu()

            if choice == "1":
                self.create_tournament()

            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                exit_requested = True
            elif choice == "8":
                exit()

    def create_tournament(self):
        """Get tournament's datas  and saves it in the database from the model_tournament.
        Adds registered players of the database from data_player with the condition of a sufficient number of players per round.
        """

        tournament = self.view.get_new_tournament()
        tournament = Tournament(**tournament)

        player_number = self.view.get_player_number("Nombre de joueurs")
        round_number = 2

        player_table = DataPlayer.player_table
        if len(player_table) < round_number * 2:
            self.view.display_message(
                f"Vous devez avoir au moins {round_number * 2} joueurs dans la base."
            )
            return

        tournament.save()
        self.view.display_message(f"Tournoi sauvegardé avec succès !")

        self.add_players_tournament()

        return

    def add_players_tournament(self):
        """Displays saved players in Database.json and add them according to user's choice"""

        PlayerController.get_players_by_surname()
        # DataPlayer.get_doc_id_by_player()

    def create_turn(self):
        """"""
        pass

    def get_tournaments(self):
        Tournaments = Tournament.get_all_tournaments()
        ViewTournament.print_registered_tournaments(self)

        return
