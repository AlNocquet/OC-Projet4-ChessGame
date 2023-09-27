from tinydb import TinyDB
from tinydb import Query
from tinydb import where
import os


class DataPlayer:

    """DataPlayer object handles user requests linked to the Players.json database"""

    if not os.path.exists("./Base"):
        os.makedirs("./Base")

    def __init__(self):
        self.db = TinyDB("./Base/Players.json")
        self.player_table = self.db.table("Players")

    def save_player(self, serialize):
        """Saves player in Players.json"""
        self.player_table.insert(serialize)

    def update_player_from_table(self, item, ids: list[int]):
        """Update the player in the database"""
        return self.player_table.update(item, doc_ids=ids)

    def remove_player_from_table(self, ids: list[int]):
        """Delete the player in the database"""
        return self.player_table.remove(doc_ids=ids)

    def extract_players_list(self):
        """Extracts players saved in Players.json as a dictionary list"""
        players = self.player_table.all()
        # add the db id for each player
        for player in players:
            player["id_db"] = str(player.doc_id)
            return players

    def player_by_doc_id(self, db_id):
        """Extracts player by searching by surname in the Players.json"""

        player = self.player_table.get((where("db_id") == db_id))
        return player

    def player_by_fullname(self, surname, first_name):
        """Extracts player by searching by surname in the Players.json"""

        search = Query

        player = self.player_table.get(
            search.surname == surname, search.first_name == first_name
        )
        player_id = player.doc_id

        return player_id

    def player_by_fullname_2(self, first_name: str, name: str) -> dict:
        """Return first document matching the first_name and name"""
        record = self.player_table.get(
            (where("surname") == name) & (where("name") == first_name)
        )
        # add the id inside the record.
        if record:
            record["id"] = record.doc_id

        return record
