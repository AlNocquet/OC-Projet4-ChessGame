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
            elif choice.lower() == "e":
                exit_requested = True
            elif choice.lower() == "q":
                exit()

    def create_tournament(self):
        """Get tournament's datas  and saves it in the database from the model_tournament.
        Adds registered players of the database from data_player with the condition of a sufficient number of players per round.
        """

        try:
            tournament = self.view.request_new_tournament()
            tournament = Tournament(**tournament)

            if len(DataPlayer().player_table) < int(tournament.number_of_rounds) * 2:
                self.view.display_error_message(
                    f"\n Vous devez avoir au moins {tournament.number_of_rounds * 2} joueurs dans la base.\n"
                )
                return

            tournament.players = self.add_players_to_tournament(
                tournament.number_of_players
            )  # Réceptionner les players retournés par add_players

            self.manage_rounds(tournament)
            tournament.save()
            self.view.display_success_message(f"Tournoi sauvegardé avec succès !")

        except CancelError:
            self.view.display_message(f"\n Création du tournoi annulé.\n")
            return

        return

    def add_players_to_tournament(self, player_number):
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

        name = f"Round {current_round}"

        # Create a datetime object
        date = datetime.now()
        # Convert the datetime object to a string in a specific format (Object of type datetime is not JSON serializable)
        start_date = date.strftime("%Y-%m-%d %H:%M:%S")

        while len(players) > 0:
            player_1 = players.pop(0)
            player_2 = players.pop(0)
            match = Match(player_1=player_1, player_2=player_2)
            matches.append(match)

        round = Round(name=name, start_date=start_date, matches=matches)

        return round

    def manage_rounds(self, tournament: Tournament):
        """Manages the launch of the rounds' creation with a random sorting of players for the first round and a sorting by player's scores for the following ones"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.request_create_rounds()
            if choice.lower() == "n":
                return

            players = tournament.players.copy()
            if tournament.current_round == 0:
                shuffle(players)
            else:
                players.sort(reverse=True, key=lambda player: player.score)

            tournament.current_round += 1
            round = self.create_round(players, tournament.current_round)
            tournament.rounds.append(round)

            self.display_pair_of_players(round)
            self.add_scores_tournament(round)

            now = datetime.now()
            end_date = f"Date et heure de fin : {now.strftime('%d/%m/%Y %H:%M:%S')}"
            tournament.rounds.append(end_date)

            status = "Round terminé"
            tournament.rounds.append(status)

            if tournament.current_round >= int(tournament.number_of_rounds):
                exit_requested = True

    def display_pair_of_players(self, round: Round):
        """Display players 1 and 2 (model_match via model_player) of each match"""

        title = f"[ADVERSAIRES PAR MATCH - ROUND EN COURS]"

        matches = []
        # num = 0

        for match in round.matches:
            # for index, match in enumerate(round.matches):
            # Parcourir la liste et utiliser l'index de la liste parcourue + enumarate OU à la main : instancier ex num = 0 et incrémenter
            # Problème : TypeError: 'bool' object is not iterable
            # Problème : num int et non str > ne marche pas
            # num = +1
            matches.append(
                {
                    # "N° de Match": num,
                    # "N° de Match": index + 1,
                    "JOUEURS 1": match.player_1.full_name,
                    "JOUEURS 2": match.player_2.full_name,
                }
            )
        self.view.table_settings(title, matches)

    def add_scores_tournament(self, round: Round):
        """Add player's scores of each match"""

        choice = self.view.request_add_scores()

        for match in round.matches:
            print(
                Fore.CYAN
                + Style.BRIGHT
                + match.player_1.full_name
                + " VS "
                + match.player_2.full_name
                + Style.RESET_ALL
            )
            self.view.display_message_score_section(
                f"\n Victoire Joueur 1 : Tapez 1 \n Victoire Joueur 2 : Tapez 2 \n Match Nul : Tapez 3 \n"
            )

            if choice in ["1", "2", "3"]:
                if choice == "1":
                    match.player_1.score += 1

                elif choice == "2":
                    match.player_2.score += 1

                elif choice == "3":
                    match.player_1.score += 0.5
                    match.player_2.score += 0.5

                return choice

        else:
            self.display_error_message(f"\n Choix invalide !\n")

    def display_tournaments(self):
        """Get tournaments list (from the model_tournament) and display it with rich (from base_view)"""

        tournaments = Tournament.get_tournaments_selected_fields_list()

        title = f"[LISTE DE {len(tournaments)} TOURNOIS]"
        self.view.table_settings(title, tournaments)
        return tournaments

    def load_tournament(self):
        """Display saved tournaments' list (from controller_tournament) and loads one (from data_tournament) selected by the user (from view_tournament)"""

        try:
            tournaments = (
                self.display_tournaments()
            )  # Afficher les tournois from controller
            tournament_requested = (
                self.view.get_tournament_by_id()
            )  # Selectionner tournoi via id from view

            while tournament_requested not in tournaments:
                self.display_error_message(
                    f"Désolé, {tournament_requested} ne fait pas partie de la liste des tournois enregistrés"
                )  # Gestion None

            tournament_loaded = self.data.get_t_by_id_(
                tournament_requested
            )  # Chargement tournoi
            self.view.display_message(
                f"\n Voici le tournoi {tournament_loaded} avec cet ID"
            )  # Afficher tournoi

        except CancelError:
            self.view.display_message(f"\n Chargement du tournoi annulé.\n")
            return
