from models.model_player import Player

from tinydb import TinyDB  # Représente la base de données

# from tinydb import Query    #Permet d'interroger la base de données
# from tinydb import where    #Permet d'affiner les critères de recherche


class DataPlayer:

    """"""

    def __init__(self):
        self.db = TinyDB("ChessGame/Database.json")
        self.player_table = self.db.table("Players")

    def save_player(self, serialized_player):
        """Sauvegarde un joueur sur le Database.json"""
        self.player_table.insert(serialized_player)