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
from colorama import Fore, Style, Back


class TournamentController(BaseView):
    def __init__(self) -> None:
        self.view = ViewTournament()
        self.view_player = ViewPlayer()
        self.data = DataTournament()

    def manage_tournament_menu(self):
        """Displays the menu "GESTION DES TOURNOIS" from view_tournament and return the user's choice"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.get_tournament_menu()

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
            elif choice.lower() == "e":
                exit_requested = True
            elif choice.lower() == "q":
                exit()

    def create_tournament(self):
        """Get tournament's datas  and saves it in the database from the model_tournament.
        Adds registered players of the database from data_player with the condition of a sufficient number of players per round.
        """

        try:
            tournament = self.view.get_create_tournament()
            tournament = Tournament(**tournament)

            if len(DataPlayer().player_table) < int(tournament.number_of_rounds) * 2:
                self.view.display_error_message(
                    f"\n Vous devez avoir au moins {tournament.number_of_rounds * 2} joueurs dans la base.\n"
                )
                return

            tournament.players = self.add_players_to_tournament(
                tournament.number_of_players
            )  # Réceptionner les players retournés par add_players

            self.manage_rounds(tournament, round)
            tournament.save()
            self.view.display_success_message(f"Tournoi sauvegardé avec succès !")

        except CancelError:
            self.view.display_message(f"\n Création du tournoi annulé.\n")
            return

        return

    def add_players_to_tournament(self, player_number):
        """Displays saved players in Database.json and add them according to user's choices"""

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
        "Returns a Round object with matches"

        matches = []

        name = f"Round {current_round}"

        date = datetime.now()
        start_date = date.strftime("%Y-%m-%d %H:%M:%S")

        while len(players) > 0:
            player_1 = players.pop(0)
            player_2 = players.pop(0)
            match = Match(player_1=player_1, player_2=player_2)
            matches.append(match)

        round = Round(name=name, start_date=start_date, matches=matches)

        return round

    def manage_rounds(self, tournament: Tournament, round: Round):
        """Manages the launch of the rounds' creation with a random sorting of players for the first round and a sorting
        by player's scores for the following ones"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.get_create_round(round)

            if choice.lower() == "n":
                exit_requested = True

            elif choice.lower() == "y":
                players = tournament.players.copy()
                if tournament.current_round == 0:
                    shuffle(players)
                else:
                    players.sort(reverse=True, key=lambda player: player.score)

                tournament.current_round += 1
                round = self.create_round(players, tournament.current_round)
                tournament.rounds.append(round)

                self.create_pair_of_players(round)
                self.add_scores_to_tournament(round)

            else:
                tournament.current_round >= int(tournament.number_of_rounds)
                exit_requested = True

    def create_pair_of_players(self, round: Round):
        """Returns a Match object with 2 players"""

        title = f"[Liste des matchs du {round.name}]"

        matches = []

        for index, match in enumerate(round.matches):
            # Parcourir la liste et utiliser l'index de la liste parcourue, enumarate contient l’indice et l’élément parcouru

            matches.append(
                {
                    "N° de Match": str(index + 1),
                    "player_1": match.player_1.full_name,
                    "player_2": match.player_2.full_name,
                }
            )

        headers = ["N° de Match", "Joueur 1", "Joueur 2"]
        self.view.table_settings(headers, title, matches)

    def add_scores_to_tournament(self, round: Round):
        """Returns player's scores of each match and ends it"""

        try:
            choice = self.get_user_answer(f"\n Enregistrer les scores ? (Y/N) : ")

            if choice.lower() == "n":
                self.display_message(f"\n Ok !")
                return

            for match in round.matches:
                self.view.get_current_match()
                choice = self.view.get_choices_match_result()

                if choice == "1":
                    match.player_1.score += 1

                elif choice == "2":
                    match.player_2.score += 1

                elif choice == "3":
                    match.player_1.score += 0.5
                    match.player_2.score += 0.5

            now = datetime.now()
            round.end_date = (
                f"Date et heure de fin : {now.strftime('%d/%m/%Y %H:%M:%S')}"
            )

            round.status = "Round terminé"

        except CancelError:
            self.view.display_message(f"\n Enregistrement des scores annulé.\n")

        return
