from datas.data_tournament import DataTournament

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
        current_round=0,
        rounds=[],
        players=[],
    ):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.number_of_players = number_of_players
        self.current_round = current_round
        self.description = description
        self.rounds = rounds
        self.players = players

    def serialize(self):
        tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_of_rounds": self.number_of_rounds,
            "number_of_players": self.number_of_players,
            "current_round": self.current_round,
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

    @classmethod
    def get_tournaments_selected_fields_list(cls):
        """Returns a list of tournaments with selected fields"""

        tournaments_list = []

        tournaments = cls.datas.extract_tournaments_list()

        for t in tournaments:
            new_t = {
                "name": t.get("name"),
                "place": t.get("place"),
                "date": t.get("date"),
                "number_of_rounds": t.get("number_of_rounds"),
                "number_of_players": t.get("number_of_players"),
                "description": t.get("description"),
            }
            tournaments_list.append(new_t)

        return tournaments_list

    # def get_all_sort_tournaments_by_date(cls):
    # """Returns a list of players by surname"""
    # players = cls.datas.extract_tournament_list()
    # sorted_players = sorted(players, key=itemgetter("surname"))
    # return sorted_players
