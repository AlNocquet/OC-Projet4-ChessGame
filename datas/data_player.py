from tinydb import TinyDB, Query
import os


class DataPlayer:

    """"""

    if not os.path.exists("./Base"):
        os.makedirs("./Base")

    def __init__(self):
        self.db = TinyDB("./Base/Database.json")
        self.player_table = self.db.table("Players")

    def save_player(self, serialize):
        """Saves player in Database.json"""
        self.player_table.insert(serialize)

    def extract_players_list(self):
        """Extracts players saved in Database.json as a dictionary list"""
        return self.player_table.all()  # Retourne liste entière extraite

    def get_doc_id_by_player(self, surname):
        """Extracts player's doc_id by searching by surname in the Database.json"""

        User = Query()

        player = self.player_table.get(User.surname == surname)
        player_id = player.doc_id
        return player_id
