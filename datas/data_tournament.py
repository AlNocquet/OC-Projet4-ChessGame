from tinydb import TinyDB
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
        """Extracts ALL tournaments saved in Tournaments.json as a dictionary list"""
        tournaments = self.tournament_table.all()
        # add the db id for each tournament
        for tournament in tournaments:
            tournament["id_db"] = str(tournament.doc_id)
            return tournaments

    def get_t_by_id_(self, id_db: int) -> dict:
        """Return a tournament dict matching the id"""
        record = self.tournament_table.get(cond=None, doc_id=id_db)
        if record is not None:
            # add the db_id in the record
            record["id_db"] = str(record.doc_id)
        return record
