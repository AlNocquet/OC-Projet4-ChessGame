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
    def get_yes_or_no(self, msg: str, min_len=1) -> str:
        """Return string 'y' or 'n' and value = 1 from the input from the user"""

        valid_choice = ["y", "n", "Y", "N"]

        while True:
            choice = input(Fore.BLACK + Style.DIM + f"\n {msg}" + Style.RESET_ALL)

            if choice in valid_choice:
                return choice

            elif len(valid_choice) < min_len:
                self.display_error_message(self, msg="Veuillez saisir un choix.")

            else:
                self.display_error_message(self, msg="Choix invalide")

    def display_message(self, msg: str):
        """Displays messages of view app, view_player or view_tournament which uses it"""
        print("\n")
        print(Fore.WHITE + Style.BRIGHT + msg + Style.RESET_ALL)

    def display_section_subtitles(self, msg: str):
        """Displays messages under menus of view app, view_player or view_tournament which uses it"""
        print(Fore.BLACK + Style.BRIGHT + msg.center(100) + Style.RESET_ALL)

    def display_error_message(self, msg: str):
        """Displays error messages related to view_player or view_tournament which uses it"""
        print("\n")
        print(Fore.RED + Style.BRIGHT + msg + Style.RESET_ALL)

    def display_success_message(self, msg: str):
        """Displays success messages related to view_player or view_tournament which uses it"""
        print("\n")
        print(Fore.GREEN + Style.BRIGHT + msg + Style.RESET_ALL)

    def main_menu_settings(self, msg: str) -> str:
        """Displays the menu related to view_app which uses it"""
        print("\n")
        print(Fore.WHITE + Back.RED + Style.BRIGHT + msg.center(100) + Style.RESET_ALL)

    def player_menu_settings(self, msg: str):
        """Displays the menu related to view_player which uses it"""
        print("\n")
        print(
            Fore.WHITE + Back.MAGENTA + Style.BRIGHT + msg.center(100) + Style.RESET_ALL
        )

    def tournament_menu_settings(self, msg: str):
        """Displays the menu related to tournament_player which uses it"""
        print("\n")
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT + msg.center(100) + Style.RESET_ALL)

    def player_sections_settings(self, msg: str):
        """Displays the title related to the section of view_player which uses it"""
        print("\n")
        print(
            Fore.MAGENTA + Back.BLACK + Style.BRIGHT + msg.center(100) + Style.RESET_ALL
        )

    def tournament_sections_settings(self, msg: str):
        """Displays the title related to the section of view_tournament which uses it"""
        print("\n")
        print(Fore.CYAN + Style.BRIGHT + msg.center(100) + Style.RESET_ALL)

    def scores_section_settings_1(self, msg: str):
        """Defines the visual of scores' section of view_tournament which uses it"""
        print("\n")
        print(Fore.CYAN + Style.BRIGHT + msg + Style.RESET_ALL)

    def scores_section_settings_2(self, msg: str):
        """Defines the visual of scores' section of view_tournament which uses it"""
        print("\n")
        print(Fore.BLUE + Style.DIM + msg + Style.RESET_ALL)

    def table_settings(self, headers, title: str, items: list):
        """Defines the visual of a dynamic table with datas ( from Player or Tournament object) with Rich"""

        print("\n")

        table = Table(
            title=title,
            padding=(0, 1),
            header_style="blue bold",
            title_style="purple bold",
            title_justify="center",
            width=100,
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

    def get_user_answer(self, label, min_len=1):
        """Returns a alphanumeric string and value = 1 from the input from the user"""

        while True:
            value = input(Fore.BLACK + Style.DIM + f"\n {label}" + Style.RESET_ALL)
            value = str.capitalize(value)

            if len(value) < min_len:
                self.display_error_message(f"Veuillez saisir un choix")

            return value

    def get_int(self, label):
        """Returns a value compatible with int from the input of the user"""

        while True:
            value = input(Fore.BLUE + Style.BRIGHT + f"{label} : " + Style.RESET_ALL)
            value = str.capitalize(value)

            try:
                int(value)
                return value
            except ValueError:
                self.display_error_message(f"Veuillez entrer uniquement un entier")

    def get_alpha_string(self, label: str) -> str:
        """Returns an alpha string + value > 0 from the input of the user"""

        while True:
            value = input(Fore.BLUE + Style.BRIGHT + f"{label} : " + Style.RESET_ALL)
            value = str.capitalize(value)

            if value.lower() == EXIT_CODE:
                raise CancelError

            if value.isalpha() or value.split():
                return value
            self.display_error_message(
                f"Veuillez entrer une chaîne de caractères uniquement composée de lettres (au moins une)"
            )

    def get_alphanum(self, label: str, min_len=1, max_len=255) -> str:
        """Returns a alphanumeric string + value > 0 from the input from the user"""

        while True:
            value = input(Fore.BLUE + Style.BRIGHT + f"{label} : " + Style.RESET_ALL)
            value = str.capitalize(value)

            if not min_len <= len(value) <= max_len:
                self.display_error_message(
                    f"Veuillez entrer une chaîne de caractères entre {min_len} et {max_len} caractères"
                )
                continue

            if value.isalnum() or value.split():
                return value

            if value.lower() == EXIT_CODE:
                raise CancelError

            self.display_error_message(
                f"Veuillez entrer une chaîne de caractère uniquement composée de lettres et de chiffres"
            )

    def get_date(self, label) -> str:
        """Returns a date(str) for tournament enter by the user"""

        valid_date = False

        while valid_date == False:
            date_value = input(
                Fore.BLUE
                + Style.BRIGHT
                + f"{label} au format JJ-MM-AAAA : "
                + Style.RESET_ALL
            )

            try:
                formated_date = datetime.strptime(date_value, "%d-%m-%Y").date()

            except ValueError:
                self.display_error_message(
                    f"Veuillez entrer une date valide au format JJ-MM-AAAA"
                )
                continue

            now = datetime.now().date()

            if not formated_date < now:
                valid_date = True
                return date_value

            else:
                self.display_error_message(
                    f"Veuillez entrer une date égale ou supérieure à la date du jour"
                )

    def get_player_number(self, label):
        """Returns the player number checking that number is even"""
        while True:
            player_number = self.get_int(label)

            if int(player_number) % 2 == 0:
                return player_number
            else:
                self.display_error_message(f"Veuillez entrer un nombre de joueurs pair")
