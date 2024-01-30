from models.model_tournament import Tournament
from models.model_round import Round
from models.model_match import Match
from models.model_player import Player
from views.view_tournament import ViewTournament
from views.view_player import ViewPlayer
from views.view_base import BaseView, CancelError, EXIT_CODE, QUIT_CODE
from datas.data_player import DataPlayer
from datas.data_tournament import DataTournament
from controllers.player import PlayerController

from datetime import datetime
from random import shuffle
from operator import itemgetter


class TournamentController(BaseView):
    def __init__(self) -> None:
        self.view = ViewTournament()
        self.view_player = ViewPlayer()
        self.data = DataTournament()

    def manage_tournament_menu(self):
        """Manages the menu "GESTION DES TOURNOIS" and returns the user's choice"""

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
            elif choice.lower() == EXIT_CODE:
                exit_requested = True
            elif choice.lower() == QUIT_CODE:
                exit()

    def create_tournament(self):
        """Gets tournament's datas and saves them. Adds registered players with the condition of a sufficient number of players per round."""

        try:
            tournament = self.view.display_fields_new_tournament()
            tournament = Tournament(**tournament)

            if len(DataPlayer().player_table) < int(tournament.number_of_rounds) * 2:
                self.view.display_error_message(
                    f"\n Vous devez avoir au moins {tournament.number_of_rounds * 2} joueurs dans la base.\n"
                )
                return

            tournament.players = self.add_players_to_tournament(
                tournament.number_of_players
            )

            self.manage_rounds(tournament)

        except CancelError:
            self.view.display_message(f"\n Création du tournoi annulé.\n")
            return

        return

    def add_players_to_tournament(self, player_number):
        """Displays saved players and add them according to user's choices"""

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

    def manage_rounds(self, tournament: Tournament):
        """Manages the launch of the rounds' creation with a random sorting of players for the first round and a sorting
        by player's scores for the following ones"""

        continue_rounds = True

        while continue_rounds:
            choice_next_round = self.get_yes_or_no(f"Lancer un round ? (Y/N) : ")

            if choice_next_round == "n":
                break

            # Reprise TOURNOI

            # Initialise Round a None

            round = None

            # Si Round en cours > Display match (continue self.get_matches_list(round))
            try:
                round = tournament.rounds[tournament.current_round]
            except IndexError:
                pass

            # Si pas de Round en cours > Création des pairs players et incrémentation round
            if round is None:
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
                tournament.end_date = date.strftime("%d-%m-%Y")
                tournament.status = "Done"
                self.view.display_message(f"Tournoi terminé !")

        tournament.save()
        self.view.display_success_message(f"Tournoi sauvegardé avec succès !")

        self.players_tournament_by_scores(tournament)

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

            choice = self.view.get_choices_match_result(round)

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

        date = datetime.now()
        round.end_date = date.strftime("%Y-%m-%d %H:%M:%S")
        round.status = "Done"
        self.view.display_message(f"Round terminé !")

    def resume_tournament(self):
        """Displays list of tournaments "Launched" and resumes the selected one"""

        try:
            self.tournament_sections_settings(f"CHARGEMENT DU TOURNOI")
            self.display_section_subtitles(
                "Tapez Exit pour revenir au menu précédent, Quit pour quitter le programme"
            )

            tournaments = Tournament.get_tournaments_in_progress()

            title = f"[LISTE DES {len(tournaments)} TOURNOIS EN COURS]"

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

            valid_tournament_id = [t.get("id_db") for t in tournaments]

            tournament_id = self.view.get_tournament_id(
                valid_tournament_id=valid_tournament_id
            )

            tournament = Tournament.get_tournament(
                tournament_id
            )  # Retourne l'input avec l'id_db qui matche

            self.manage_rounds(tournament)

        except CancelError:
            self.view.display_message(f"Modification du joueur annulée")
            return

    def players_tournament_by_scores(self, tournament: Tournament):
        """Gets players list sorted by score and display it with rich from base_view"""

        players = [
            Player.get_player_by_id(id_db=player_id) for player_id in tournament.players
        ]

        sorted_players = sorted(players, key=itemgetter("score"))

        title = f"[LISTE DES {len(players)} JOUEURS PAR ORDRE ALPHABETIQUE]"

        headers = [
            "Nom",
            "Prénom",
            "Date Naissance",
            "National Chess Id",
            "id_db",
            "Score",
        ]

        self.view.table_settings(headers, title, sorted_players)

        return sorted_players

    def get_all_tournaments_sorted_by_date(self):
        """Displays tournaments list sorted by date from the model_tournament and display it with rich from base_view"""

        tournaments = Tournament.get_tournaments_selected_fields_list()

        title = f"[LISTE DES {len(tournaments)} TOURNOIS PAR DATE]"

        headers = [
            "name",
            "place",
            "start_date",
            "end_date",
            "number_of_rounds",
            "number_of_players",
            "description",
            "status",
            "id_db",
        ]
        self.view.table_settings(headers, title, tournaments)

    def get_rounds_by_tournament(self, tournament=Tournament):
        """Displays tournaments' list and loads the selected one to display the associated rounds"""

        try:
            self.tournament_sections_settings(
                f"CONSULTER LISTE DES ROUNDS D'UN TOURNOI"
            )
            self.display_section_subtitles(
                "Tapez Exit pour revenir au menu précédent, Quit pour quitter le programme"
            )

            # Afficher les tournois

            tournaments = Tournament.get_tournaments_selected_fields_list()

            title = f"[LISTE DES {len(tournaments)} TOURNOIS EN COURS]"

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

            # Sélectionner le tournoi (gestion valid_id)

            valid_tournament_id = [t.get("id_db") for t in tournaments]

            tournament_id = self.view.get_tournament_id(
                valid_tournament_id=valid_tournament_id
            )

            tournament = Tournament.get_tournament(tournament_id)

            # Affichage des rounds associés

            rounds = tournament.rounds(tournament)

            title = f"[LISTE DES ROUNDS]"

            headers = [
                "name",
                "start_date",
                "self.end_date",
                "status",
            ]

            self.view.table_settings(headers, title, rounds)

        except CancelError:
            self.view.display_message(f"Modification du joueur annulée")
            return
