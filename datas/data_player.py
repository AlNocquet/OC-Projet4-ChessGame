from tinydb import TinyDB
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
