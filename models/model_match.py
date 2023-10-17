class Match:
    """Creates the Match object which should contain a pair of players and their results.
    Each Match instance is automatically stored as a tuple in the instance of the round to which it belongs.
    This tuple contains two lists containing 2 elements: a player and a score.
    """

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