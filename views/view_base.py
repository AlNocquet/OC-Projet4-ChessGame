from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.table import Column, Padding
from colorama import Fore, Style, Back


console = Console()

EXIT_CODE = "exit"

date = datetime.now()

START_DATE = date.strftime("%Y-%m-%d %H:%M:%S")

END_DATE = date.strftime("%Y-%m-%d %H:%M:%S")

# STATUS_START


class CancelError(Exception):
    ...


class PlayerNotFound(Exception):
    ...


class TournamentNotFound(Exception):
    ...


class BaseView:
    """BaseView object manage all formats and characteristics of user's requests."""

    @classmethod
    def get_yes_or_no(self, msg: str) -> str:
        """Input Enter your choice - Return string 'y' or 'n' + value > 0 from the input from the user"""

        valid_choice = ["y", "n"]

        while True:
            choice = input(Fore.WHITE + Style.DIM + f"\n {msg}").lower()

            if choice in valid_choice:
                return choice

            else:
                self.display_error_message(self, msg="Choix invalide")

    def display_message(self, msg: str):
        """Displays messages of view app, view_player or view_tournament which uses it"""
        print("\n")
        print(Fore.WHITE + Style.BRIGHT + msg)

    def display_section_subtitles(self, msg: str):
        """Displays messages under menus of view app, view_player or view_tournament which uses it"""
        print(Fore.WHITE + Style.DIM + msg.center(100) + "\n")

    def display_error_message(self, msg: str):
        """Displays error messages related to view_player or view_tournament which uses it"""
        print("\n" + Fore.RED + Style.BRIGHT + msg)

    def display_success_message(self, msg: str):
        """Displays success messages related to view_player or view_tournament which uses it"""
        print("\n" + Fore.GREEN + Style.BRIGHT + msg)

    def main_menu_settings(self, msg: str) -> str:
        """Displays the menu related to view_app which uses it"""
        print("\n")
        print(Fore.WHITE + Back.RED + Style.BRIGHT + msg.center(100))

    def player_menu_settings(self, msg: str):
        """Displays the menu related to view_player which uses it"""
        print("\n")
        print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + msg.center(100))

    def tournament_menu_settings(self, msg: str):
        """Displays the menu related to tournament_player which uses it"""
        print("\n")
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT + msg.center(100))

    def player_sections_settings(self, msg: str):
        """Displays the title related to the section of view_player which uses it"""
        print("\n" + Fore.MAGENTA + Back.BLACK + Style.BRIGHT + msg.center(100))

    def player_sections_messages_settings(self, msg: str):
        """Displays the title related to the section of view_player which uses it"""
        print("\n" + Fore.MAGENTA + Back.BLACK + Style.BRIGHT + msg)

    def tournament_sections_settings(self, msg: str):
        """Displays the title related to the section of view_tournament which uses it"""
        print("\n" + Fore.CYAN + Style.BRIGHT + msg.center(100))

    def scores_section_settings(self, msg: str):
        """Defines the visual of scores' section of view_tournament which uses it"""
        print("\n" + Fore.CYAN + Style.BRIGHT + msg)

    def scores_section_choice_settings(self, msg: str):
        """Defines the visual of scores' choices of view_tournament which uses it"""
        print("\n" + Fore.BLUE + Style.DIM + msg)

    def table_settings(self, headers, title: str, items: list):
        """Defines the visual of a dynamic table with datas ( from Player or Tournament object) with Rich"""

        print("\n")

        table = Table(
            title=title,
            padding=(0, 1),
            header_style="blue bold",
            title_style="purple bold",
            title_justify="center",
            width=120,
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

    def get_user_answer(self, label):
        """Input Enter your choice - Returns a alphanumeric string + value > 0 from the input from the user"""

        while True:
            value = input(Fore.WHITE + Style.BRIGHT + f"\n {label}").lower()
            return value

    def get_int(self, label):
        """Returns a value compatible with int from the input of the user"""

        while True:
            value = input(Fore.WHITE + Style.DIM + f"{label} : ")

            try:
                int(value)
                return value
            except ValueError:
                self.display_error_message(f"Veuillez entrer uniquement un entier")

    def get_alpha_string(self, label: str) -> str:
        """Returns an alpha string + value > 0 from the input of the user"""

        while True:
            value = input(Fore.WHITE + Style.DIM + f"{label} : ")
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
            value = input(Fore.WHITE + Style.DIM + f"{label} : ")
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
                Fore.WHITE + Style.DIM + f"{label} au format JJ-MM-AAAA : "
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

    def get_player_date_of_birth(self):
        """Displays field requested for player creation and returns the user's response"""
        valid_birthday = False

        while valid_birthday == False:
            date_of_birth = input(
                Fore.WHITE + Style.DIM + "\n Date de naissance au format JJ-MM-AAAA : "
            )

            try:
                formated_date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            except ValueError:
                self.display_error_message(
                    f"Veuillez entrer une date valide au format JJ-MM-AAAA"
                )
                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
                return date_of_birth

            else:
                self.display_error_message(
                    f"Vous devez avoir au moins 18 ans pour vous inscrire"
                )

    def get_player_number(self, label):
        """Returns the player number checking that number is even"""
        while True:
            player_number = self.get_int(label)

            if int(player_number) % 2 == 0:
                return player_number
            else:
                self.display_error_message(f"Veuillez entrer un nombre de joueurs pair")
