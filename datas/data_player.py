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

    def extract_players_list(self):
        """Extracts players saved in Players.json as a dictionary list"""
        players = self.player_table.all()
        # add the db id for each player
        for player in players:
            player["id_db"] = str(player.doc_id)
            return players

    def player_by_fullname(self, surname, first_name):
        """Extracts player by searching by surname in the Players.json"""

        User = Query()

        player = self.player_table.search(
            (User.surname == surname) & (User.first_name == first_name)
        )

        return player

    def update_player_from_table(self, data: dict, ids: list) -> list[int]:
        """Update the player in the database"""
        return self.player_table.update(data, doc_ids=ids)

    def remove_player_from_table(self, ids: list[int]):
        """Delete the player in the database"""
        return self.player_table.remove(doc_ids=ids)

    def player_by_doc_id(self, id):
        """Extracts player by searching by surname in the Players.json"""
        player = self.player_table.get(doc_id=id)
        return player
