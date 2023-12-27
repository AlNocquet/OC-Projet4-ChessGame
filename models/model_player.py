from datas.data_player import DataPlayer
from views.view_base import PlayerNotFound

from operator import itemgetter


class Player:

    """Creates the Player object which should automatically register in the database "Players.json" from data_player.
    The player instance must contain at least:
    the name, first name, date of birth, classification, national failure identifier of the federation.
    """

    datas = DataPlayer()

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

    @property  # décorateur property // definition de méthode pour concaténation nom + prénom
    def full_name(self):
        return " " + self.first_name + " " + self.surname + " "

    def serialize(self):
        player = {
            "surname": self.surname,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_chess_id": self.national_chess_id,
            "id_db": self.id_db,
            "score": self.score,
        }
        return player

    def save(self):  # méthode d'instance = sur un objet
        """Saves the player in the database (from data_player)"""
        data = self.serialize()
        self.datas.save_player(data)

    @classmethod
    # Non propre à un objet player mais toute la base "joueurs" = pas méthode d'instance mais de classe (cls, pointeur vers la classe par convention)
    # DataPlayer sort du constructeur de Player : pas en variable d'instance, pas seulement propre à chaque objet de Player = commun à tous les objets (variable de classe)
    def get_all_sort_by_surname(cls):
        """Returns a list of players by surname"""
        players = cls.datas.extract_players_list()
        sorted_players = sorted(players, key=itemgetter("surname"))
        return sorted_players

    @classmethod
    def get_player_updated(self):
        """Returns a Player instance matching the id in db from data_player"""
        data = self.datas.update_player()

        if data is None:
            raise PlayerNotFound(f"Ce joueur n'existe pas dans la base de données")

        return data

    def get_player_removed(self):
        """Returns a Player instance matching the id in db from data_player"""
        data = self.datas.remove_player()

        if data is None:
            raise PlayerNotFound(f"Ce joueur n'existe pas dans la base de données")

        return data

    @classmethod
    def get_player_by_id(cls, id_db: int) -> "Player":
        """Returns a Player instance matching the id_db from data_player"""
        data = cls.datas.get_by_id(id_db)

        if data is None:
            raise PlayerNotFound(
                f"Le joueur avec l'identifiant {id_db} n'existe pas dans la base de données"
            )
        return Player(**data)
