class Tournament:

    """Créée l'objet Tournament qui doit s'enregistrer automatiquement dans la base. Chaque instance d'un tournoi est renseigné
    par (manager/utilisateur ?): le nom, le lieu, la date de début et de fin (automatique ? = voir import module ressources cours),
    le numéro du tour en cours, la description  pour les remarques générales du directeur du tournoi.
       Le nombre de tours d'un tournoi est fixé à 4 par défaut et donc de 8 joueurs.
       Les instances de tours sont répertoriés dans la liste rounds.
       La liste des joueurs enregistrés sont répertoriés dans la liste players."""

    def __init__(
        self, name, place, date, description, number_of_rounds=4, number_of_players=8
    ):
        self.name = name
        self.place = place
        self.date = date
        # self.time = temps ?
        self.number_of_rounds = number_of_rounds
        self.number_current_round = 0
        self.description = description
        self.rounds = []
        self.players = []

    def serialize_tournament(self):
        tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number of rounds": self.number_of_rounds,
            "description": self.description,
            "rounds": self.rounds,
            "players": self.players,
        }
        return tournament


class Round:

    """Créée l'objet Round qui est stocké dans la liste des tours du tournoi de l'objet Tournament pour être enregistré dans la base. Chaque instance
    de tour doit contenir : le nom (numéro de tour : Round1, Round2), la date et le temps de début et de fin.
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

        # Lien Tours et Matches liste


class Match:

    """Créée l'objet Match qui doit contenir une paire de joueurs et leurs résultats. Chaque instance de Match est automatiquement
    stockée sous forme de tuple dans l'instance du tour auquel il appartient. Ce tuple contient deux listes contenant 2 éléments :
    un joueur et un score."""

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
