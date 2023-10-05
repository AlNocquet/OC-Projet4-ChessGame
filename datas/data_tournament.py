from tinydb import TinyDB
from tinydb import Query
from tinydb import where
import os


class DataTournament:

    """DataTournament object handles user requests linked to the Tournament.json database"""

    if not os.path.exists("./Base"):
        os.makedirs("./Base")

    def __init__(self):
        self.db = TinyDB("./Base/Tournaments.json")
        self.tournament_table = self.db.table("Tournaments")

    def save_tournament(self, serialize):
        """Saves tournament in Tournaments.json"""
        self.tournament_table.insert(serialize)

    def extract_tournaments_list(self):
        """Extracts tournaments saved in Tournaments.json as a dictionary list"""
        tournaments = self.tournament_table.all()
        # add the db id for each tournament
        for tournament in tournaments:
            tournaments["id_db"] = int(tournament.doc_id)
            return tournaments
