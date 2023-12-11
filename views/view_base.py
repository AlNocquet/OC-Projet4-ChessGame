from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.table import Column, Padding
from colorama import Fore, Style, Back


console = Console()

EXIT_CODE = "exit"


class CancelError(Exception):
    ...


class PlayerNotFound(Exception):
    ...


class TournamentNotFound(Exception):
    ...


class BaseView:
    """BaseView object manage all formats and characteristics of user's requests."""

    @classmethod
    def display_message(self, msg: str):
        "Displays messages of view app, view_player or view_tournament which uses it"
        print(Fore.WHITE + Style.BRIGHT + msg + Style.RESET_ALL)

    def display_message_sections(self, msg: str):
        "Displays messages under menus of view app, view_player or view_tournament which uses it"
        print(Fore.BLACK + Style.BRIGHT + msg + Style.RESET_ALL)

    def display_error_message(self, msg: str):
        "Displays error messages related to view_player or view_tournament which uses it"
        print(Fore.RED + Style.BRIGHT + msg + Style.RESET_ALL)

    def display_success_message(self, msg: str):
        "Displays success messages related to view_player or view_tournament which uses it"
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

    def display_message_score_section(self, msg: str):
        "Displays messages related to view_tournament which uses it"
        print(Fore.BLUE + Style.DIM + msg + Style.RESET_ALL)

    def table_settings(self, headers, title: str, items: list):
        "Defines the visual of a dynamic table with datas ( from Player or Tournament object) with Rich"

        table = Table(
            title=title,
            padding=(0, 1),
            header_style="blue bold",
            title_style="purple bold",
            title_justify="center",
            width=75,
        )

        try:
            headers = items[0].keys()

        except IndexError:
            headers = ["Liste vide"]

        for title in headers:
            table.add_column(title, style="white", justify="center")

        for item in items:
            table.add_row(*item.values())

        console = Console()
        print("")
        console.print(table)

    def get_int(self, label):
        """Returns a value compatible with int from the input of the user"""

        while True:
            value = input(Fore.MAGENTA + Style.NORMAL + f"{label} : " + Style.RESET_ALL)
            value = str.capitalize(value)

            try:
                int(value)
                return value
            except ValueError:
                self.display_error_message(f"\n Vous devez rentrer un entier.\n")

    def get_int_rounds(self, label):
        """Returns a value compatible with int from the input of the user for Rounds to serialize (without capitalize)"""

        while True:
            value = input(Fore.BLUE + Style.NORMAL + f"{label} : " + Style.RESET_ALL)

            try:
                int(value)
                return value
            except ValueError:
                self.display_error_message(f"\n Vous devez rentrer un entier.\n")

    def get_alpha_string(self, label: str) -> str:
        """Returns an alpha string + value > 0 from the input of the user"""

        while True:
            value = input(Fore.MAGENTA + Style.NORMAL + f"{label} : " + Style.RESET_ALL)
            value = str.capitalize(value)

            if value.lower() == EXIT_CODE:
                raise CancelError

            if value.isalpha() or value.split():
                return value
            self.display_error_message(
                f"\n La chaine de caractère ne doit être composée que de lettres (Au moins une).\n"
            )

    def get_alphanum(self, label: str, min_len=1, max_len=255) -> str:
        """Returns a alphanumeric string + value > 0 from the input from the user"""

        while True:
            value = input(Fore.MAGENTA + Style.NORMAL + f"{label} : " + Style.RESET_ALL)
            value = str.capitalize(value)

            if not min_len <= len(value) <= max_len:
                self.display_error_message(
                    f"\n La chaine de caractères doit comprendre entre {min_len} et {max_len} caractères.\n"
                )
                continue

            if value.isalnum() or value.split():
                return value

            if value.lower() == EXIT_CODE:
                raise CancelError

            self.display_error_message(
                f"\n La chaine de caractère ne doit être composée que de lettres et de chiffres.\n"
            )

    def get_date(self, label) -> str:
        """Returns a date(str) for tournament enter by the user"""

        while True:
            date_value = input(
                Fore.MAGENTA
                + Style.NORMAL
                + f"{label} au format JJ-MM-AAAA : "
                + Style.RESET_ALL
            )
            date_value = str.capitalize(date_value)

            try:
                formated_date = datetime.strptime(date_value, "%d-%m-%Y")
                return date_value

            except ValueError:
                self.display_error_message(
                    f"\n Veuillez entrer une date valide au format JJ-MM-AAAA \n"
                )

    def get_date_rounds(self, label):
        """Returns a date(str) for tournament enter by the user for Rounds to serialize (without capitalize)"""

        while True:
            date_value = input(
                Fore.BLUE
                + Style.NORMAL
                + f"{label} au format JJ-MM-AAAA : "
                + Style.RESET_ALL
            )

            try:
                formated_date = datetime.strptime(date_value, "%d-%m-%Y")
                return date_value

            except ValueError:
                self.display_error_message(
                    f"\n Veuillez entrer une date valide au format JJ-MM-AAAA \n"
                )

    def get_player_number(self, label):
        """Returns the player number checking that number is even"""
        while True:
            player_number = self.get_int(label)

            if int(player_number) % 2 == 0:
                return player_number
            else:
                self.display_error_message(f"\n Le nombre de joueur doit être pair.\n")

    def get_data_rounds(self, label, min_len=1, max_len=255):
        """Returns a alphanumeric string + value > 0 from the input from the user for Rounds to serialize (without capitalize)"""

        while True:
            value = input(Fore.BLUE + Style.NORMAL + f"{label} : " + Style.RESET_ALL)

            if not min_len <= len(value) <= max_len:
                self.display_error_message(
                    f"\n La chaine de caractères doit comprendre entre {min_len} et {max_len} caractères.\n"
                )
                continue

            if value.isalnum() or value.split():
                return value

            if value.lower() == EXIT_CODE:
                raise CancelError

            self.display_error_message(
                f"\n La chaine de caractère ne doit être composée que de lettres et de chiffres.\n"
            )
