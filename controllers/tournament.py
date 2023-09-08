from models.model_tournament import Tournament
from views.view_tournament import ViewTournament
from datas.data_player import DataPlayer


class TournamentController:
    def __init__(self) -> None:
        self.view = ViewTournament()

    def manage_tournament(self):
        """Displays the menu "GESTION DES TOURNOIS" from view_tournament and return the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.display_tournament_menu(self)

            if choice == "1":
                pass
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

    def create_tournament(self):
        """Get tournament's datas  and saves it in the database from the model_tournament.
        Adds registered players of the database from data_player with the condition of a sufficient number of players per round.
        """
        name = self.view.get_tournament_name()
        place = self.view.get_tournament_place()
        date = self.view.get_tournament_date()
        # time_control = self.view.get_tournament_time_control()
        description = self.view.get_tournament_description()
        player_number = self.view.get_tournament_player_number()
        round_number = self.view.get_tournament_round()

        player_table = DataPlayer.player_table
        if len(player_table) < round_number * 2:
            self.view.display_message(
                f"Vous devez avoir au moins {round_number * 2} joueurs dans la base."
            )
            return

        tournament = Tournament()
        tournament.save()

        self.add_players_tournament()

        # self.create_turn()
        return

    def add_players_tournament(self):
        """Displays saved players in Database.json and returns user's player choice"""
        # DataPlayer.extract_players_list(self)
        pass

    def create_turn(self):
        """"""
        pass

    def get_tournaments(self):
        Tournaments = Tournament.get_all_tournaments()
        ViewTournament.print_registered_tournaments(self)

        return
