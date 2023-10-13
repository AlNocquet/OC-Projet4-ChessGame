from datetime import datetime
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style, Back


console = Console()

EXIT_CODE = "exit"


class CancelError(Exception):
    ...


class PlayerNotFound(Exception):
    ...


class BaseView:
    """BaseView object manage all formats and characteristics of user's requests."""

    @classmethod
    def display_message(self, msg: str):
        "Displays the message related to the function from view_player or view_tournament which uses it"
        print(Fore.YELLOW + Style.BRIGHT + msg + Style.RESET_ALL)

    def display_error_message(self, msg: str):
        "Displays the error message related to the function from view_player or view_tournament which uses it"
        print(Fore.RED + Style.BRIGHT + msg + Style.RESET_ALL)

    def display_success_message(self, msg: str):
        "Displays the success message related to the function from view_player or view_tournament which uses it"
        print(Fore.GREEN + Style.BRIGHT + msg + Style.RESET_ALL)

    def main_menu_settings(self, msg: str.center) -> str:
        "Displays the menu related to the section from view_app which uses it"
        print(Fore.WHITE + Back.RED + Style.BRIGHT + msg + Style.RESET_ALL)

    def player_menu_settings(self, msg: str):
        "Displays the menu related to the section from view_player which uses it"
        print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + msg + Style.RESET_ALL)

    def tournament_menu_settings(self, msg: str):
        "Displays the menu related to the section from tournament_player which uses it"
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT + msg + Style.RESET_ALL)

    def player_sections_settings(self, msg: str):
        "Displays the title related to the section from view_player which uses it"
        print(Fore.MAGENTA + Style.BRIGHT + msg + Style.RESET_ALL)

    def tournament_sections_settings(self, msg: str):
        "Displays the title related to the section from view_tournament which uses it"
        print(Fore.CYAN + Style.BRIGHT + msg + Style.RESET_ALL)

    def table_settings(self, title: str, items=list):
        "Defines the visual of a dynamic table with datas ( from Player or Tournament object) with Rich"

        table = Table(
            title=title,
            header_style="yellow bold",
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

    def get_int(self, label):
        """Return an value compatible with int from the input from the user"""

        while True:
            value = input(f"{label} : ")
            try:
                int(value)
                return value
            except ValueError:
                self.display_error_message(f"\n Vous devez rentrer un entier.\n")

    def get_alpha_string(self, label: str) -> str:
        """Returns an alpha string + value > 0 from the input from the user"""

        while True:
            value = str.capitalize(input(f"{label} : "))

            if value.lower() == EXIT_CODE:
                raise CancelError

            if value.isalpha():
                return value
            self.display_error_message(
                f"\n La chaine de caractère ne doit être composée que de lettres (Au moins une).\n"
            )

    def get_alphanum(self, label: str, min_len=1, max_len=255) -> str:
        """Returns a alphanumeric string + value > 0 from the input from the user"""

        while True:
            value = str.capitalize(input(f"{label} : "))

            if not min_len <= len(value) <= max_len:
                self.display_error_message(
                    f"\n La chaine de caractères doit comprendre entre {min_len} et {max_len} caractères.\n"
                )
                continue

            if value.isalnum():
                return value

            if value.lower() == EXIT_CODE:
                raise CancelError

            self.display_error_message(
                f"\n La chaine de caractère ne doit être composée que de lettres et de chiffres.\n"
            )

    def get_date(self, label) -> str:
        """Return a date(str) for tournament enter by the user"""

        while True:
            date_value = input(f"{label} au format JJ-MM-AAAA : ")

            try:
                formated_date = datetime.strptime(date_value, "%d-%m-%Y")
                return date_value

            except ValueError:
                self.display_error_message(
                    f"\n Veuillez entrer une date valide au format JJ-MM-AAAA \n"
                )

    def get_player_number(self, label):
        """Return the player number checking that number is even"""
        while True:
            player_number = self.get_int(label)

            if int(player_number) % 2 == 0:
                return player_number
            else:
                self.display_error_message(f"\n Le nombre de joueur doit être pair.\n")
