import os

from tinydb import TinyDB

# from tinydb import Query


class DataPlayer:
    """Creates DataPlayer object which handles user's requests linked to the Players.json database"""

    if not os.path.exists("./Base"):
        os.makedirs("./Base")

    def __init__(self):
        self.db = TinyDB("./Base/Players.json")
        self.player_table = self.db.table("Players")

    def save_player(self, serialize):
        """Saves player in Players.json"""
        self.player_table.insert(serialize)

    def extract_players_list(self):
        """Extracts players saved in Players.json as a dictionary list, add the id_db for each player"""
        players = self.player_table.all()
        for player in players:
            player["id_db"] = str(player.doc_id)
        return players

    def update_data_player(self, field_to_update: dict, id_db: list) -> list[int]:
        """Update the player in the database Players.json"""
        return self.player_table.update(field_to_update, doc_ids=id_db)

    def remove_data_player(self, id_db: list) -> list[int]:
        """Delete the player in the database Players.json"""
        return self.player_table.remove(doc_ids=id_db)

    def get_p_by_id(self, id_db: int) -> dict:
        """Return a player dict matching the id (id_db = doc_id), add the db_id in the record"""
        record = self.player_table.get(cond=None, doc_id=id_db)
        if record is not None:
            record["id_db"] = str(record.doc_id)
        return record

    # def get_by_fullname(self, surname, first_name):
    # """Extracts a player by searching the surname in the Players.json"""

    # User = Query()

    # player = self.player_table.search((User.surname == surname) & (User.first_name == first_name))

    # return player
