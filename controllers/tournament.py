from models.model_tournament import Tournament
from models.model_round import Round
from models.model_match import Match
from models.model_player import Player
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer
from views.view_base import BaseView, CancelError, PlayerNotFound, console as c
from datas.data_player import DataPlayer
from datas.data_tournament import DataTournament
from controllers.player import PlayerController

from datetime import datetime
from operator import itemgetter
from random import random, shuffle


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

            if len(DataPlayer().player_table) < int(tournament.number_of_rounds) * 2:
                self.view.display_error_message(
                    f"\n Vous devez avoir au moins {tournament.number_of_rounds * 2} joueurs dans la base.\n"
                )
                return

            tournament.players = self.add_players_tournament(
                tournament.number_of_players
            )  # Réceptionner les players retournés par add_players

            self.manage_rounds(tournament)
            tournament.save()
            self.view.display_success_message(f"Tournoi sauvegardé avec succès !")

        except CancelError:
            self.view.display_message(f"\n Création du tournoi annulé.\n")
            return

        return

    def add_players_tournament(self, player_number):
        """Displays saved players in Database.json and add them according to user's choice"""

        players = PlayerController().get_all_players_sorted_by_surname()

        valid_players_id = [p.get("id_db") for p in players]

        players_id_to_add = self.view_player.get_tournament_players_id(
            int(player_number), valid_players_id
        )

        if players_id_to_add:
            players = [Player.get_player_by_id(p_id) for p_id in players_id_to_add]
        else:
            players = []

        return players

    def create_round(self, players: list, current_round) -> Round:
        "Return a Round object with matches"

        matches = []

        current_round += 1
        name = f"Round {current_round}"
        start_date = datetime.now()

        while len(players) > 0:
            player_1 = players.pop(0)
            player_2 = players.pop(0)
            match = Match(player_1_name=player_1, player_2_name=player_2)
            matches.append(match)

        round = Round(name=name, start_date=start_date, matches=matches)

        return round

    def manage_rounds(self, tournament: Tournament):
        """Manages the launch of the rounds' creation with a random sorting of players for the first round and a sorting by player's scores for the following ones"""

        exit_requested = False

        players = tournament.players.copy()

        choice = self.view.request_create_round()

        while not exit_requested:
            if choice == "N" or choice == "n":
                break
            else:
                if tournament.current_round == 0:
                    shuffle(players)
                    print(players)
                else:
                    players = players.sort(reverse=True, key=Player.score)
                    print(players)

                round = self.create_round(players, tournament.current_round)
                tournament.rounds.append(round)
                # inscrire les scores : def view + def score

            if len(tournament.current_round) > len(tournament.number_of_rounds):
                exit_requested = True

    def add_scores():
        pass

    def display_tournaments(self):
        """Get players list from the model_player and display it with rich from base_view"""

        tournaments = Tournament.get_tournaments_selected_fields_list()

        title = f"[LISTE DE {len(tournaments)} TOURNOIS]"
        self.view.table_settings(title, tournaments)
        return tournaments
