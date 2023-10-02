from models.model_tournament import Tournament
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer
from views.view_base import BaseView, CancelError, PlayerNotFound
from datas.data_player import DataPlayer
from controllers.player import PlayerController


class TournamentController(BaseView):
    def __init__(self) -> None:
        self.view = ViewTournament()
        self.view_player = ViewPlayer()
        self.data = DataPlayer()

    def manage_tournament(self):
        """Displays the menu "GESTION DES TOURNOIS" from view_tournament and return the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.display_tournament_menu()

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.display_tournaments_by_name()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "E" or choice == "e":
                exit_requested = True
            elif choice == "Q" or choice == "q":
                exit()

    def create_tournament(self):
        """Get tournament's datas  and saves it in the database from the model_tournament.
        Adds registered players of the database from data_player with the condition of a sufficient number of players per round.
        """

        try:
            tournament = self.view.get_new_tournament()
            tournament = Tournament(**tournament)

            player_number = self.view.get_player_number("Nombre de joueurs")
            round_number = 2

            player_table = DataPlayer.player_table
            if len(player_table) < round_number * 2:
                self.view.display_error_message(
                    f"Vous devez avoir au moins {round_number * 2} joueurs dans la base."
                )
                return

            tournament.save()
            self.view.display_success_message(f"Tournoi sauvegardé avec succès !")

            self.add_players_tournament()
            self.view.request_new_turn(self.create_turn())

        except CancelError:
            self.view.display_message(f"\n Création du tournoi annulé.\n")
            return

        return

    def add_players_tournament(self):
        """Displays saved players in Database.json and add them according to user's choice"""
        pass

    def create_turn(self):
        """Create a new Turn"""
        pass

    def display_tournaments_by_name(self):
        """Get players list from the model_player and display it with rich from base_view"""

        tournaments = []

        for t in Tournament.get_all_sort_by_name():
            t["number_of_rounds"] = str(t.get("number_of_rounds"))
            t["number_of_players"] = str(t.get("number_of_players"))
            tournaments.append(t)

        title = f"[LISTE DES {len(tournaments)} JOUEURS PAR ORDRE ALPHABETIQUE]"
        BaseView.table_settings(title, tournaments)
