from tinydb import TinyDB
import os


class DataApp:

    """"""

    if not os.path.exists("./Base"):
        os.makedirs("./Base")

    def __init__(self):
        self.db = TinyDB("./Base/Database.json")
        self.tournament_table = self.db.table("Tournaments")

    def save_tournament(self, serialize):
        """Sauvegarde un tournoi dans Database.json"""
        self.tournament_table.insert(serialize)
