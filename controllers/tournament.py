from models.model_tournament import Tournament
from models.model_player import Player
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer
from views.view_base import BaseView, CancelError, PlayerNotFound, console as c
from datas.data_player import DataPlayer
from datas.data_tournament import DataTournament
from controllers.player import PlayerController


class TournamentController(BaseView):
    def __init__(self) -> None:
        self.view = ViewTournament()
        self.view_player = ViewPlayer()
        self.data = DataTournament()

    def manage_tournament(self):
        """Displays the menu "GESTION DES TOURNOIS" from view_tournament and return the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.display_tournament_menu()

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.display_tournaments()
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

            if len(self.data.player_table) < int(tournament.number_of_rounds) * 2:
                self.view.display_error_message(
                    f"\n Vous devez avoir au moins {tournament.number_of_rounds * 2} joueurs dans la base.\n"
                )
                return

            tournament.save()
            self.view.display_success_message(f"Tournoi sauvegardé avec succès !")

        except CancelError:
            self.view.display_message(f"\n Création du tournoi annulé.\n")
            return

        return

    def add_players_tournament(self, player_number):
        """Displays saved players in Database.json and add them according to user's choice"""

        players = PlayerController().display_players_by_surname()

        valid_players_id = [p.get("db_id") for p in players]

        players_id_to_add = self.view_player.get_tournament_players_id(
            int(player_number), valid_players_id
        )

        if players_id_to_add:
            players = [Player.get_player_by_id(p_id) for p_id in players_id_to_add]
        else:
            players = []

        # c.print(f"\n Variables dans add_players_tournament", style="green bold")
        # c.print(locals())

        return players

    def display_tournaments(self):
        """Get players list from the model_player and display it with rich from base_view"""

        tournaments = []

        for t in Tournament.get_all_sort_by_name():
            t["name"] = int(t.get("name"))
            t["place"] = int(t.get("place"))
            t["date"] = int(t.get("date"))
            t["number of rounds"] = int(t.get("number of rounds"))
            t["number of players"] = int(t.get("number of players"))
            t["description"] = int(t.get("description"))
            tournaments.append(t)

        title = f"[LISTE DES {len(tournaments)} TOURNOIS]"
        BaseView.table_settings(title, tournaments)

    def create_round(self):
        """Create a new Turn"""
        pass
