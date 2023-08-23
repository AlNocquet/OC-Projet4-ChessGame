from datas.data_player import DataPlayer

from operator import itemgetter, attrgetter


class Player:

    """Crée l'objet Player qui doit s'enregistrer automatiquement dans la base. L'instance du joueur doit contenir au moins :
    le nom, le prénom, la date de naissance, le classement, l'identifiant national d'échec de la fédération.
    """

    def __init__(
        self, surname, first_name, date_of_birth, national_chess_id, total_score
    ):
        self.surname = surname
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.total_score = 0

        self.datas = DataPlayer()

    def serialize(self):
        player = {
            "surname": self.surname,
            "name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_chess_id": self.national_chess_id,
            "score": self.total_score,
        }
        return player

    def save(self):
        data = self.serialize()
        self.datas.save_player(data)

    def display_by_surname(self):
        players = DataPlayer.extract_players_list(self)
        sorted_players = sorted(players, key=itemgetter("surname"))
        return sorted_players
