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
from colorama import Fore, Style


class TournamentController(BaseView):
    def __init__(self) -> None:
        self.view = ViewTournament()
        self.view_player = ViewPlayer()
        self.data = DataTournament()

    def manage_tournament_menu(self):
        """Manages the menu "GESTION DES TOURNOIS" and returns the user's choice or None if user enter exit or quit"""

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
                self.get_matches_by_tournament()
            elif choice.lower() == EXIT_CODE:
                exit_requested = True
            elif choice.lower() == QUIT_CODE:
                exit()

    def create_tournament(self):
        """Gets tournament's datas and saves them.
        Adds registered players with the condition of a sufficient number of players per round.
        Or None if user enter exit or quit"""

        try:
            tournament = self.view.display_fields_new_tournament()

        except CancelError:
            self.view.display_message("\n Création du tournoi annulé.\n")
            return

        # Unpack les valeurs d'un itérable pas encore affectées
        tournament = Tournament(**tournament)

        if len(DataPlayer().player_table) < int(tournament.number_of_rounds) * 2:
            self.view.display_error_message(
                f"\n Vous devez avoir au moins {tournament.number_of_rounds * 2} joueurs dans la base.\n"
            )
            return

        # Nettoyage du cache Player
        Player.cache_players.clear()

        tournament.players = self.add_players_to_tournament(
            tournament.number_of_players
        )
        self.manage_rounds(tournament)

    def add_players_to_tournament(self, player_number):
        """Displays saved players and add them according to user's choices or None if user enter exit or quit"""

        players = PlayerController().get_all_players_sorted_by_surname()

        # Création liste de joueurs id_db valides > itérer sur les players "sorted by surname"
        valid_players_id = [p.get("id_db") for p in players]

        # Input players id à ajouter au tournoi
        players_id_to_add = self.view_player.get_tournament_players_id(
            int(player_number), valid_players_id
        )

        # Liste players : Itérer sur players avec appel model_player pour PlayerNotFound + appel DataPlayer -
        # > id_db = doc_id + enregistrement id_db

        if players_id_to_add:
            players = [Player.get_player_by_id(p_id) for p_id in players_id_to_add]
        else:
            players = []

        return players

    def manage_rounds(self, tournament: Tournament):
        """Manages the launch of the rounds' creation with a random sorting of players for the first round and a sorting
        by player's scores for the following ones - or None if user enter N"""

        continue_rounds = True

        while continue_rounds:
            choice_next_round = self.get_yes_or_no("Lancer un round ? (Y/N) : ")

            if choice_next_round == "n":
                break

            # REPRISE TOURNOI : Initialise Round a None
            round = None

            # Test reprendre liste des rounds et enregistrement des scores (continue self.get_matches_list(round))
            try:
                round = tournament.rounds[tournament.current_round]
            except IndexError:
                pass

            # Sinon > création du round avec pairs de players et incrémentation round
            if round is None:
                players = tournament.players.copy()
                if tournament.current_round == 0:
                    shuffle(players)
                else:
                    players.sort(reverse=True, key=lambda player: player.score)

                tournament.current_round += 1
                round = self.create_round(players, tournament.current_round)
                tournament.rounds.append(round)

            # Enregistrement des scores
            self.get_matches_list(round)

            choice_scores = self.add_scores_to_tournament(round)
            if choice_scores == "n":
                break

            # Validation de la fin de tournoi avec enregistrement status "Done" et "date de fin"
            if tournament.current_round >= int(tournament.number_of_rounds):
                continue_rounds = False
                date = datetime.now()
                tournament.end_date = date.strftime("%d-%m-%Y")
                tournament.status = "Done"
                self.view.display_message("Tournoi terminé !")
                self.display_player_ranking(tournament)

        tournament.save()

    def create_round(self, players: list, current_round) -> Round:
        "Returns a Round object with matches"

        # Round = liste de matches
        matches = []

        name = f"Round {current_round}"

        date = datetime.now()
        start_date = date.strftime("%d-%m-%Y")

        # Création de Match avec sortie de la liste des joueurs déjà sélectionnés
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

        # Création d'une liste de matches
        matches = []

        # Enumarate : attribuer un index > Parcourir la liste et utiliser l'index + ajout à la liste des valeurs (Match = pair of players)
        for index, match in enumerate(round.matches):
            matches.append(
                {
                    "N° de Match": str(index + 1),
                    "player_1": match.player_1.full_name,
                    "player_2": match.player_2.full_name,
                }
            )

        # Display Match
        headers = ["N° de Match", "Joueur 1", "Joueur 2"]
        self.view.table_settings(headers, title, matches)

    def add_scores_to_tournament(self, round: Round):
        """Returns player's scores of each match and ends the round (status + end_date) or None if user enter N"""

        choice = self.get_yes_or_no("Enregistrer les scores ? (Y/N) : ")

        if choice == "n":
            return "n"

        for match in round.matches:
            self.view.get_current_match(round, match)

            choice = self.view.get_choices_match_result(round)

            if choice == "1":
                match.p1_score = 1.0

            elif choice == "2":
                match.p2_score = 1.0

            elif choice == "3":
                match.p1_score = 0.5
                match.p2_score = 0.5

        date = datetime.now()
        round.end_date = date.strftime("%d-%m-%Y")
        round.status = "Done"
        self.view.display_message("Round terminé !")

    def resume_tournament(self):
        """Displays list of tournaments "Launched" and resumes the selected one or None if user enter exit or quit"""

        try:
            self.tournament_sections_settings("CHARGEMENT DU TOURNOI")
            self.display_section_subtitles(
                "Tapez Exit pour revenir au menu précédent, Quit pour quitter le programme"
            )

            tournaments = Tournament.get_tournaments_in_progress()

            if len(tournaments) == 0:
                self.view.display_message("Aucun tournoi en cours")
                return

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

            # Gestion tournament_id valide
            valid_tournament_id = [t.get("id_db") for t in tournaments]

            # Input + Gestion valid_id
            tournament_id = self.view.get_tournament_id(
                valid_tournament_id=valid_tournament_id
            )

            tournament = Tournament.get_tournament(tournament_id)

            self.manage_rounds(tournament)

        except CancelError:
            self.view.display_message("Reprise du tournoi annulée")
            return

    def display_player_ranking(self, tournament: Tournament):
        """Display player ranking (actual score) for the tournament"""

        # Boucle convertir liste players en dict et sort sur le score
        players = [player.serialize() for player in tournament.players]
        players.sort(key=itemgetter("score"), reverse=True)

        self.view.table_settings("", "Classement des joueurs", players)

        input("Tapez Entrée pour continuer :")

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

    def get_one_tournament(self):
        """Return a Tournament object or None if user enter exit"""

        # Afficher les tournois
        tournaments = Tournament.get_tournaments_selected_fields_list()

        title = f"[LISTE DES {len(tournaments)} TOURNOIS]"

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

        # Input + Gestion valid_id
        valid_tournament_id = [t.get("id_db") for t in tournaments]

        try:
            tournament_id = self.view.get_tournament_id(
                valid_tournament_id=valid_tournament_id
            )
        except CancelError:
            return None

        tournament = Tournament.get_tournament(tournament_id)
        return tournament

    def get_rounds_by_tournament(self):
        """Displays tournaments' list, loads the selected one to display the associated rounds and players by ranking"""

        self.tournament_sections_settings("CONSULTER LISTE DES ROUNDS D'UN TOURNOI")
        self.display_section_subtitles(
            "Tapez Exit pour revenir au menu précédent, Quit pour quitter le programme"
        )

        tournament = self.get_one_tournament()

        # Affichage des rounds associés
        rounds = []
        for round in tournament.rounds:
            # Chaque round du tournament to dict pour travailler avec Table
            dict_round = round.serialize()
            # Enlève les matches du dict
            dict_round.pop("matches")
            # Création liste de rounds avec les nveaux dicos Round
            rounds.append(dict_round)

        title = f"[LISTE DES ROUNDS DU TOURNOI {tournament.name}]"

        headers = [
            "name",
            "start_date",
            "self.end_date",
            "status",
        ]

        self.view.table_settings(headers, title, rounds)

        # Affichage des joueurs participants par rang (score)
        self.display_player_ranking(tournament)

    def get_matches_by_tournament(self):
        """Displays tournaments' list, loads the selected one to display the associated matches and players by ranking"""

        self.tournament_sections_settings("CONSULTER LISTE DES MATCHS D'UN TOURNOI")
        self.display_section_subtitles(
            "Tapez Exit pour revenir au menu précédent, Quit pour quitter le programme"
        )

        tournament = self.get_one_tournament()

        round = Round

        for round in tournament.rounds:
            self.view.round_sections_settings(f"{round.name}")
            for match in round.matches:
                print(
                    "\n"
                    + f"{match.player_1.full_name}: "
                    + f"{match.p1_score}"
                    + Fore.YELLOW
                    + Style.DIM
                    + "  VS  "
                    + Style.RESET_ALL
                    + f"{match.player_2.full_name}: "
                    + f"{match.p2_score}"
                )

        self.display_player_ranking(tournament)
