import os
from tinydb import TinyDB  # Représente la base de données

# from tinydb import Query    #Permet d'interroger la base de données
# from tinydb import where    #Permet d'affiner les critères de recherche


class DataPlayer:

    """"""

    if not os.path.exists("./DataBase"):
        os.makedirs("./DataBase")

    def __init__(self):
        self.db = TinyDB("./Database/Database.json")
        self.player_table = self.db.table("Players")

    def save_player(self, serialized_player):
        """Sauvegarde un joueur sur le Database.json"""
        self.player_table.insert(serialized_player)

    def extract_players_list(self):
        """Extrait les joueurs enregistrés dans le Database.json sous forme de liste"""
        players_list = []
        players_table = self.player_table.all()
        for player in players_table:
            player_list = []
            surname = player["surname"]
            player_list.append(surname)
            name = player["name"]
            player_list.append(name)
            date_of_birth = player["date_of_birth"]
            player_list.append(date_of_birth)
            total_score = player["score"]
            player_list.append(total_score)
            players_list.append(player_list)
        return players_list
