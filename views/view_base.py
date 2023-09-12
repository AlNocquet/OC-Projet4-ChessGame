from rich.console import Console
from rich.table import Table

from colorama import Fore, Style, Back


class BaseView:
    @classmethod
    def display_message(self, msg: str):
        "Displays the message related to the function from view_player or view_tournament which uses it"
        print(Fore.RED + msg + Style.RESET_ALL)

    def table_settings(title: str, items=list):
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
            table.add_column(title, style="cyan")

        for item in items:
            table.add_row(*item.values())

        console = Console()
        print("")
        console.print(table)
