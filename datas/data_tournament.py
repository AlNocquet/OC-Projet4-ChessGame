import os

from tinydb import Query, TinyDB
from tinydb.table import Document


class DataTournament:
<<<<<<< HEAD
    """DataTournament object handles user requests linked to the Tournament.json database"""
=======
    """DataTournament object handles the user's requests linked to the Tournament.json database"""
>>>>>>> ea92fce1d928403647592553bc28f57c236cb946

    if not os.path.exists("./Base"):
        os.makedirs("./Base")

    def __init__(self):
        self.db = TinyDB("./Base/Tournaments.json")
        self.tournament_table = self.db.table("Tournaments")

    def save_tournament(self, serialize):
        """Saves tournament in Tournaments.json"""
        self.tournament_table.insert(serialize)

    def update_tournament(self, data, db_id):
        """Updates tournament in Tournaments.json"""
        self.tournament_table.update(data, doc_ids=db_id)

    def extract_tournaments_list(self):
        """Extracts ALL tournaments saved as a dictionary list and matching the id with doc_id"""
        tournaments = self.tournament_table.all()
        # add the db id for each tournament
        for tournament in tournaments:
            tournament["id_db"] = tournament.doc_id
<<<<<<< HEAD
        return tournaments
=======
            return tournaments
>>>>>>> ea92fce1d928403647592553bc28f57c236cb946

    def get_t_by_id(self, id_db: int) -> dict:
        """Returns a tournament dict matching the id (id_db matching doc_id)"""
        record = self.tournament_table.get(cond=None, doc_id=id_db)
        if record is not None:
            # add the db_id in the record
            record["id_db"] = str(record.doc_id)
        return record

    def search(self, field_name: str, value: str) -> list[Document]:
        "Returns records where fields value match"

        q = Query()
        if self.tournament_table.search(~(q[field_name].exists())):
            raise NameError(f"Le champs '{field_name}' n'existe pas")

        records = self.tournament_table.search(q[field_name] == value)

        # add the db_id in the record
        for record in records:
            record["id_db"] = record.doc_id
        return records
