class Match:
    """Creates the Match object which should contain a pair of players and their results.
    Each Match instance is automatically stored as a tuple in the instance of the round to which it belongs.
    This tuple contains two lists containing 2 elements: a player and a score.
    """

    def __init__(
        self, player_1_name, player_2_name, player_1_score=0, player_2_score=0
    ):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name

        self.player_1_score = player_1_score
        self.player_2_score = player_2_score

    def serialize(self):
        match = {
            "player_1_name": self.player_1_name,
            "player_2_name": self.player_2_name,
            "player_1_score": self.player_1_score,
            "player_2_score": self.player_2_score,
        }
        return match
