from operator import itemgetter

from datas.data_tournament import DataTournament
from views.view_base import TournamentNotFound

from .model_player import Player
from .model_round import Round


class Tournament:
    """Creates the Tournament object. Each instance of a tournament is filled by the user :
    name, place, start and end date, the number of the current round,
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
        """Returns a dict from the Tournament attributes"""
        tournament = {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "number_of_rounds": self.number_of_rounds,
            "number_of_players": self.number_of_players,
            "current_round": self.current_round,
            "description": self.description,
            "status": self.status,
            "end_date": self.end_date,
            "rounds": [round.serialize() for round in self.rounds],
            "players": [player.id_db for player in self.players],
        }
        return tournament

    def save(self):
        """Saves the tournament in the database - including updates to avoid duplicates"""

        data = self.serialize()
        if self.id_db is None:
            # Create the tournament
            self.id_db = self.datas.save_tournament(data)
        else:
            # Update the tournament
            self.datas.update_tournament(data, [int(self.id_db)])

    @classmethod
    def search(self, field_name: str, value: str):
        "Returns records where fields value match"
        return self.datas.search(field_name, value)

    @classmethod
    def get_all_sorted_by_date(cls):
        """Returns a list of tournaments by date"""
        tournaments = cls.datas.extract_tournaments_list()
        sorted_tournaments = sorted(
            tournaments, reverse=False, key=itemgetter("start_date")
        )
        return sorted_tournaments

    @classmethod
    def get_tournaments_selected_fields_list(cls, tournaments=None):
        """Returns a list of tournaments with selected fields"""

        tournaments_list = []

        if tournaments is None:
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
        """Returns a Tournament instance matching the id_db"""
        data = cls.datas.get_t_by_id(id_db)

        if data is None:
            raise TournamentNotFound(
                f"Le tournoi avec l'identifiant {id_db} n'existe pas dans la base de données"
            )
        return Tournament(**data)

    @classmethod
    def get_tournaments_in_progress(cls):
        """Returns a list of tournaments with status "Launched" with selected fields"""
        tournaments = cls.search(field_name="status", value="Launched")
        list_tournaments_in_progress = cls.get_tournaments_selected_fields_list(
            tournaments=tournaments
        )
        return list_tournaments_in_progress

    @classmethod
    def get_tournament(cls, tournament_id):
        """Returns a tournament object matching tournament's id from tiny_db"""

        tournament_data = cls.datas.get_t_by_id(id_db=tournament_id)
        tournament = Tournament(**tournament_data)

        # Clears the players cache - in case of previous tournament management
        Player.cache_players.clear()

        # Unpack Players
        players = [
            Player.get_player_by_id(id_db=player_id) for player_id in tournament.players
        ]
        tournament.players = players

        # Unpack Rounds
        tournament.rounds = [
            Round.deserialize(data=round_dict) for round_dict in tournament.rounds
        ]

        return tournament
