from datas.data_tournament import DataTournament
from datas.data_player import DataPlayer
from views.view_base import PlayerNotFound

from operator import itemgetter


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
