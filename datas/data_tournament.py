from tinydb import TinyDB
from tinydb import Query
from tinydb import where
import os

from views.view_base import TournamentNotFound


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
            tournament["id_db"] = str(tournament.doc_id)
            return tournaments

    def get_tournament_by_name(self, name):
        """Extracts a Tournament by searching the name in le Tournaments.json"""
        search = Query()
        try:
            tournament = self.tournament_table.get(search.name == name)
            tournament_id = tournament.doc_id
            return tournament_id
        except:
            raise TournamentNotFound(f"Ce tournoi n'existe pas dans la base de données")
