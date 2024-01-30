from .model_match import Match


class Round:
    """Creates the Round object which is stored in the tournament rounds list of the Tournament object.
    The number of rounds in a tournament is set to 4 by default and therefore 8 players.
    Each instance must contain: name (round number: Round1, Round2), date, start and end time.
    """

    def __init__(self, name, start_date, end_date=None, matches=[], status="Launched"):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches: list = matches
        self.status = status

    def serialize(self):
        """"""
        round = {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [match.serialize() for match in self.matches],
            "status": self.status,
        }
        return round

    @classmethod
    def deserialize(cls, data: dict) -> "Round":
        """"""
        round: Round = cls(**data)

        round.matches = [Match.deserialize(data) for data in round.matches]

        return round
