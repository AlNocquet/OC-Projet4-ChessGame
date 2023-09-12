from rich.console import Console
from rich.table import Table

from dataclasses import asdict, dataclass


@dataclass
class BasePlayer:
    surname: str
    first_name: str
    date_of_birth: str
    national_chess_id: str
    score: str

    def __str__(self) -> str:
        return f", {self.surname}, {self.first_name}, {self.date_of_birth}, {self.national_chess_id}, {self.score} "

    def serialize(self):
        return asdict(self)

    def str_list(self) -> list[str]:
        """Return the values in str list"""
        return [
            self.surname,
            self.first_name,
            self.date_of_birth,
            self.national_chess_id,
            self.score,
        ]


class BaseView:
    @classmethod
    def display_message(self, msg: str):
        "Displays the message related to the function from view_player or view_tournament which uses it"
        print(msg)

    def table_settings(title: str, BasePlayer):
        "Defines the visual of a dynamic table with datas ( from Player or Tournament object) with Rich"

        table = Table(
            title=title,
            header_style="",
            title_style="purple bold",
            title_justify="center",
        )

        try:
            headers = items[0].keys()

        except IndexError:
            headers = ["Liste vide"]

        for title in headers:
            table.add_column(title, style="cyan", justify="center")

        for item in items:
            table.add_row(*item.values())

        console = Console()
        print("")
        console.print(table)
