from operator import itemgetter

from datas.data_player import DataPlayer
from datas.data_tournament import DataTournament
from views.view_base import PlayerNotFound


class Player:
    """Creates the Player object. The player instance must contain at least:
    the name, first name, date of birth, classification, national failure identifier of the federation.
    """

    datas = DataPlayer()
    cache_players = {}

    def __init__(
        self,
        surname,
        first_name,
        date_of_birth,
        national_chess_id,
        id_db=None,
        score=0,
    ):
        self.surname = surname
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.id_db = id_db
        self.score = score

    @property
    def full_name(self):
        """Method for concatenation last name + first name"""
        return " " + self.first_name + " " + self.surname + " "

    def serialize(self):
        """Return a dict from the Player attributes"""
        player = {
            "surname": self.surname,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_chess_id": self.national_chess_id,
            "score": self.score,
        }
        return player

    def save(self):
        """Saves player in the database"""
        data = self.serialize()
        self.datas.save_player(data)

    @classmethod
    def get_all_sort_by_surname(cls):
        """Returns a list of players sorted by surname"""
        players = cls.datas.extract_players_list()
        sorted_players = sorted(players, key=itemgetter("surname"))
        return sorted_players

    @classmethod
    def remove(self, id_db):
        """Removes player in the database"""

        tournaments = DataTournament().extract_tournaments_list()

        for tournament in tournaments:
            if id_db in tournament["players"]:
                raise ValueError("Suppression joueur impossible")

        self.datas.remove_data_player([int(id_db)])

    @classmethod
    def get_player_by_id(cls, id_db: int) -> "Player":
        """Returns a Player instance matching the id"""

        # Try to get the player from cache
        player = cls.cache_players.get(id_db)

        # If player not found in cache get him from db
        if player is None:
            data = cls.datas.get_p_by_id(id_db)

            if data is None:
                raise PlayerNotFound(
                    f"Le joueur avec l'identifiant {id_db} n'existe pas dans la base de données"
                )

            player = Player(**data)
            # Add the player object in cache
            cls.cache_players[id_db] = player

        return player
