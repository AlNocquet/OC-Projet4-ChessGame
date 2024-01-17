from datas.data_tournament import DataTournament
from views.view_base import TournamentNotFound
from .model_round import Round
from .model_player import Player

from operator import itemgetter
from rich.console import Console
from rich.table import Table


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
        start_date,
        number_of_rounds,
        number_of_players,
        description,
        status="Launched",
        id_db=None,
        end_date=None,
        current_round=0,
        rounds=[],
        players=[],
    ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.number_of_rounds: int = number_of_rounds
        self.number_of_players = number_of_players
        self.current_round = current_round
        self.description = description
        self.status = status
        self.end_date = end_date
        self.id_db = id_db
        self.rounds: list = rounds
        self.players = players

    def serialize(self):
        tournament = {
            "name": self.name,
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "number_of_rounds": self.number_of_rounds,
            "number_of_players": self.number_of_players,
            "current_round": self.current_round,
            "description": self.description,
            "status": self.status,
            "rounds": [round.serialize() for round in self.rounds],
            "players": [player.id_db for player in self.players],
        }
        return tournament

    def save(self):  # méthode d'instance = sur un objet
        "Saves the tournament in the database (from data_tournament)"
        data = self.serialize()
        self.datas.save_tournament(data)

    @classmethod
    def search(self, field_name: str, value: str):
        "Returns records where fields value match - to resume ONE tournament"
        return self.datas.search(field_name, value)

    @classmethod
    def get_all_sorted_by_date(cls):
        """Returns a list of tournaments by date"""
        tournaments = cls.datas.extract_tournaments_list()
        sorted_tournaments = sorted(
            tournaments, reverse=True, key=itemgetter("start_date")
        )
        return sorted_tournaments

    @classmethod
    def get_tournaments_selected_fields_list(cls):
        """Returns a list of tournaments (from data_tournament) with selected fields"""

        tournaments_list = []

        tournaments = cls.get_all_sorted_by_date()

        for t in tournaments:
            new_t = {
                "name": t.get("name"),
                "place": t.get("place"),
                "start_date": t.get("start_date"),
                "end_date": t.get("end_date"),
                "number_of_rounds": t.get("number_of_rounds"),
                "number_of_players": t.get("number_of_players"),
                "description": t.get("description"),
                "status": t.get("status"),
                "id_db": t.get("id_db"),
            }
            tournaments_list.append(new_t)

        return tournaments_list

    @classmethod
    def get_tournament_by_id(cls, id_db: int) -> "Tournament":
        """Returns a Tournament instance matching the id_db from data_player"""
        data = cls.datas.get_t_by_id(id_db)

        if data is None:
            raise TournamentNotFound(
                f"Le tournoi avec l'identifiant {id_db} n'existe pas dans la base de données"
            )
        return Tournament(**data)
