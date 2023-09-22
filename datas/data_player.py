from tinydb import TinyDB
from tinydb import Query
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

    def update_player_from_table(self, item, doc_id):
        """Update the player in the database"""
        pass

    def remove_player_from_table(self, item, doc_id):
        """Delete the player in the database"""
        pass

    def extract_players_list(self):
        """Extracts players saved in Players.json as a dictionary list"""
        players = self.player_table.all()
        # add the db id for each player
        for player in players:
            player["db_id"] = str(player.doc_id)
            return players

    def get_player_by_doc_id(self, doc_id):
        """Extracts player by searching by surname in the Players.json"""

        player = self.player_table.get(doc_id=doc_id)
        return player

    def get_player_by_surname(self, surname):
        """Extracts player by searching by surname in the Players.json"""

        search = Query()

        player = self.player_table.get(search.surname == surname)
        player_id = player.doc_id
        return player_id
