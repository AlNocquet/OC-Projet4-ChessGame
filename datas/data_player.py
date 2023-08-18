import os
from tinydb import TinyDB

# from tinydb import Query    #Permet d'interroger la base de données
# from tinydb import where    #Permet d'affiner les critères de recherche


class DataPlayer:

    """"""

    if not os.path.exists("./DataBase"):
        os.makedirs("./DataBase")

    def __init__(self):
        self.db = TinyDB("./Database/Database.json")
        self.player_table = self.db.table("Players")

    def save_player_database(self, serialize):
        """Sauvegarde un joueur sur le Database.json"""
        self.player_table.insert(serialize)

    def extract_players_list(self):
        """Extrait les joueurs enregistrés dans le Database.json sous forme de liste"""
        return self.player_table.all()  # Retourne liste entière extraite
