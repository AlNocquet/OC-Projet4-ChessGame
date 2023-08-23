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
        """Sauvegarde un joueur dans Database.json"""
        self.player_table.insert(serialize)

    def extract_players_list(self):
        """Extrait les joueurs enregistrés dans le Database.json sous forme de liste"""
        return self.player_table.all()  # Retourne liste entière extraite
