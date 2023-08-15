from datas.data_player import DataPlayer


class Player:

    """Crée l'objet Player qui doit s'enregistrer automatiquement dans la base. L'instance du joueur doit contenir au moins :
    le nom, le prénom, la date de naissance, le classement, l'identifiant national d'échec de la fédération.
    """

    def __init__(
        self, surname, first_name, date_of_birth, total_score, national_chess_id
    ):
        self.surname = surname
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.total_score = 0
        self.national_chess_id = national_chess_id

    def serialized_player(self):
        player = {
            "surname": self.surname,
            "first name": self.first_name,
            "date of birth": self.date_of_birth,
            "score": self.total_score,
            "National ID chess": self.national_chess_id,
        }
        return player

    def database_save_player(self, serialized_player):
        self.DataPlayer.save_player(serialized_player)