from dataclasses import asdict, dataclass

from rich.console import Console
from rich.table import Table

# This module provides a decorator and functions for automatically adding generated special methods such as __init__() and __repr__() to user-defined classes.


# players = []


@dataclass
class Player:
    national_chess_id: str
    name: str
    first_name: str

    def __str__(self) -> str:
        return f", {self.national_chess_id}, {self.first_name}, {self.first_name}"

    def serialize(self):
        return asdict(self)

    def as_list(self) -> list[str]:
        """Returns the attributes values of the object in a str list"""
        return [self.national_chess_id, self.first_name, self.first_name]


@dataclass
class Tournament:
    name: str
    place: str
    description: str
    date: str

    def serialize(self):
        return asdict(self)


def display_message(self, msg: str):
    "Displays the message related to the function from view_player or view_tournament which uses it"
    print(msg)


def table_settings(title: str, items: list):
    "Defines the visual of a dynamic table with datas ( from Player or Tournament object) with Rich"

    table = Table(
        title=title, header_style="", title_style="purple bold", title_justify="center"
    )

    # Depuis le dictionnaire de l'objet Player ou Tournament
    headers = items[0].serialize.keys()

    # headers = items[0].keys()

    try:
        for header in headers:
            table.add_column(header, style="cyan", justify="center")

        for item in items:
            table.add_row(*item.serialize.values())
            # table.add_row(*item.values())

    except IndexError:
        headers = ["Liste vide"]

    console = Console()

    print("")
    console.print(table)


# table_settings("Liste des Players", players)
