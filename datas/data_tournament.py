from tinydb import TinyDB
import os


class DataTournament:

    """"""

    if not os.path.exists("./Base"):
        os.makedirs("./Base")

    def __init__(self):
        self.db = TinyDB("./Base/Tournaments.json")
        self.tournament_table = self.db.table("Tournaments")

    def save_tournament(self, serialize):
        """Saves tournament in Tournaments.json"""
        self.tournament_table.insert(serialize)

    def extract_tournament_list(self):
        """Extracts tournaments saved in Tournaments.json as a dictionary list"""
        return self.tournament_table.all()
