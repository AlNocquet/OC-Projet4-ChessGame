from .model_player import Player


######
# PAS BESOIN DE nommer model_match.py ==> match.py
######


class Match:
    """Creates the Match object which should contain a pair of players and their results.
    Each Match instance is automatically stored as a tuple in the instance of the round to which it belongs.
    This tuple contains two lists containing 2 elements: a player and a score.
    """

    def __init__(self, player_1, player_2, p1_score=0, p2_score=0):
        self.player_1 = player_1
        self.player_2 = player_2

        self.p1_score = p1_score
        self.p2_score = p2_score

    @property  # (property() - décorateur intégré - pour obtenir le comportement des getters et des setters)
    def p1_score(self):
        return self._p1_score

    @p1_score.setter
    # Changing the score value of player 1
    def p1_score(self, value: int):
        self._p1_score = value
        self.player_1.score += value

    @property
    def p2_score(self):
        return self._p2_score

    @p2_score.setter
    def p2_score(self, value: int):
        self._p2_score = value
        self.player_2.score += value

    def serialize(self):
        """Return a dict from the Match attributes"""
        match = {
            "player_1": self.player_1.id_db,
            "player_2": self.player_2.id_db,
            "p1_score": self.p1_score,
            "p2_score": self.p2_score,
        }
        return match

    @classmethod
    def deserialize(cls, data: dict) -> "Match":
        """Returns a Match object"""

        p1 = data.get("player_1")
        p2 = data.get("player_2")

        player_1 = Player.get_player_by_id(p1)
        player_2 = Player.get_player_by_id(p2)

        score_1 = data.get("p1_score")
        score_2 = data.get("p2_score")

        return Match(player_1, player_2, p1_score=score_1, p2_score=score_2)
