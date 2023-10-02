from datas.data_tournament import DataTournament
from datas.data_player import DataPlayer
from views.view_base import PlayerNotFound

from operator import itemgetter


class Tournament:

    """Creates the Tournament object.
    Each instance of a tournament is filled by the user : name, place, start and end date, the number of the current round,
    the description for general remarks from the tournament director.
    """

    datas = DataTournament()  # Hors Init, Partagé par tous les objets de la classe

    def __init__(
        self,
        name,
        place,
        date,
        number_of_rounds,
        number_of_players,
        description,
        rounds,
        players,
    ):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = 0
        self.number_of_players = 8
        self.number_current_round = 4
        self.description = description
        self.rounds = []
        self.players = []

    def serialize(self):
        tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number of rounds": self.number_of_rounds,
            "number_of_players": self.number_of_players,
            "description": self.description,
            "rounds": self.rounds,
            "players": self.players,
        }
        return tournament

    def save(self):  # méthode d'instance = sur un objet
        "Saves the tournament in the database (from data_tournament)"
        data = self.serialize()
        self.datas.save_tournament(data)

    @classmethod
    def get_all_sort_by_name(cls):
        """Returns a list of tournaments by surname"""
        tournaments = cls.datas.extract_tournaments_list()
        sorted_tournaments = sorted(tournaments, key=itemgetter("name"))
        return sorted_tournaments


class Round:
    """Creates the Round object which is stored in the tournament rounds list of the Tournament object.
    The number of rounds in a tournament is set to 4 by default and therefore 8 players.
    Each instance must contain: name (round number: Round1, Round2), date, start and end time.
    """

    def __init__(
        self, name, start_date_time, end_date_time=None
    ):  # None = automatique selon durée
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs = []

    def round_list(self):
        round = [self.name, self.start_date_time, self.end_date_time]
        return round

        # Lien Tours et Matchs liste


class Match:
    """Creates the Match object which should contain a pair of players and their results.
    Each Match instance is automatically stored as a tuple in the instance of the round to which it belongs.
    This tuple contains two lists containing 2 elements: a player and a score.
    """

    def __init__(self, player_name_1, player_name_2, player_1_score, player_2_score):
        self.player_name_1 = player_name_1
        self.player_name_2 = player_name_2

        self.player_1_score = 0
        self.player_2_score = 0

    def match_list_tuple(self):
        match = (
            [self.player_name_1, self.player_1_score],
            [self.player_name_2, self.player_2_score],
        )
        return match

    def get_all_sort_tournaments_by_name(cls):
        """Returns a list of players by surname"""
        players = cls.datas.extract_tournament_list()
        sorted_players = sorted(players, key=itemgetter("surname"))
        return sorted_players
