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
                self.resume_tournament()
            elif choice == "3":
                self.get_all_tournaments_sorted_by_date()
            elif choice == "4":
                self.get_rounds_by_tournament()
            elif choice == "5":
                pass
            elif choice == "e":
                exit_requested = True
            elif choice == "q":
                exit()

    def create_tournament(self):
        """Get tournament's datas and saves it in the database from the model_tournament.
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

    def manage_rounds(self, tournament: Tournament, round: Round):
        """Manages the launch of the rounds' creation with a random sorting of players for the first round and a sorting
        by player's scores for the following ones"""

        continue_rounds = True

        while continue_rounds:
            choice_next_round = self.get_yes_or_no(f"Lancer un round ? (Y/N) : ")

            if choice_next_round == "n":
                break

            round = None
            try:
                round = tournament.rounds[tournament.current_round]
            except IndexError:
                pass

            players = tournament.players.copy()
            if tournament.current_round == 0:
                shuffle(players)
            else:
                players.sort(reverse=True, key=lambda player: player.score)

            tournament.current_round += 1
            round = self.create_round(players, tournament.current_round)
            tournament.rounds.append(round)

            self.get_matches_list(round)

            choice_scores = self.add_scores_to_tournament(round)
            if choice_scores == "n":
                break

            if tournament.current_round >= int(tournament.number_of_rounds):
                continue_rounds = False
                date = datetime.now()
                tournament.end_date = date.strftime("%Y-%m-%d %H:%M:%S")
                tournament.status = "Done"
                self.view.display_message(f"Tournoi terminé !")

        tournament.save()
        self.view.display_success_message(f"Tournoi sauvegardé avec succès !")

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

    def get_matches_list(self, round: Round):
        """Displays matches with pair of players"""

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

        choice = self.get_yes_or_no(f"Enregistrer les scores ? (Y/N) : ")

        if choice == "n":
            return "n"

        for match in round.matches:
            self.view.get_current_match(round, match)

            if choice == "1":
                match.player_1_score = 1
                match.player_1.score += 1

            elif choice == "2":
                match.player_2_score = 1
                match.player_2.score += 1

            elif choice == "3":
                match.player_1_score = 0.5
                match.player_2_score = 0.5
                match.player_1.score += 0.5
                match.player_2.score += 0.5

            choice = self.view.get_choices_match_result(round)

        now = datetime.now().date()
        round.end_date = f"Date et heure de fin : {now.strftime('%Y-%m-%d %H:%M:%S')}"
        round.status = "Done"
        self.view.display_message(f"Round terminé !")

        return

    def resume_tournament(self):
        """Displays list of tournaments "Launched" and resumes the selected one"""

        self.tournament_sections_settings(f"CHARGEMENT DU TOURNOI ")

        # Fonction(tournaments) view table rich des tournois lancé
        tournaments = Tournament.search("status", "Launched")

        # Fonction Input du View tournament du tournoi à sélectionné
        tournament_id = self.view.get_tournament_id()

        tournament = Tournament.get(
            tournament_id
        )  # Ici mettre nom fonction input du View tournament
        self.manage_rounds(tournament)

    def get_all_tournaments_sorted_by_date(self):
        """Displays tournaments list sorted by date from the model_tournament and display it with rich from base_view"""

        tournaments = []

        for t in Tournament.get_tournaments_selected_fields_list():
            t["start_date"] = str(t.get("start_date"))
            tournaments.append(t)

        title = f"[LISTE DES {len(tournaments)} TOURNOIS PAR DATE]"

        headers = [
            "Nom",
            "Lieu",
            "Date",
            "Nbre de Rounds",
            "Nbre de joueurs",
            "description",
            "status",
            "id_db",
        ]
        self.view.table_settings(headers, title, tournaments)

        return tournaments

    def get_rounds_by_tournament(self):
        """Displays tournaments' list and loads the selected one to display the associated rounds"""

        tournaments = self.get_all_tournaments_sorted_by_date()

        valid_tournament_id = [t.get("id_db") for t in tournaments]

        tournament_id_to_select = self.view.get_tournament_id(valid_tournament_id)

        if tournament_id_to_select:
            tournaments = [
                Tournament.get_tournament_by_id(t_id)
                for t_id in tournament_id_to_select
            ]
        else:
            tournaments = []

        return tournaments
