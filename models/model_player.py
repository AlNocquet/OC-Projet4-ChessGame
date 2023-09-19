from datas.data_player import DataPlayer

from operator import itemgetter


class Player:

    """Crée l'objet Player qui doit s'enregistrer automatiquement dans la base. L'instance du joueur doit contenir au moins :
    le nom, le prénom, la date de naissance, le classement, l'identifiant national d'échec de la fédération.
    """

    datas = DataPlayer()  # Hors Init, Partagé par tous les objets de la classe

    def __init__(self, surname, first_name, date_of_birth, national_chess_id, score=0):
        self.surname = surname
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.score = score

    def serialize(self):
        player = {
            "surname": self.surname,
            "name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_chess_id": self.national_chess_id,
            "score": self.score,
        }
        return player

    def save(self):  # méthode d'instance = sur un objet
        "Saves the player in the database (from data_player)"
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
