from datetime import datetime

from colorama import Back, Fore, Style
from rich.console import Console
from rich.table import Table

console = Console()

EXIT_CODE = "exit"

QUIT_CODE = "quit"


class CancelError(Exception):
    pass


class PlayerNotFound(Exception):
    pass


class TournamentNotFound(Exception):
    pass


class BaseView:
    """Creates BaseView object wich manages all formats and characteristics of user's requests."""

    @classmethod
    def get_yes_or_no(self, msg: str) -> str:
        """Display field "Enter your choice" and returns the user's response Yes or No"""

        valid_choice = ["y", "n"]

        while True:
            choice = input(Fore.WHITE + Style.DIM + f"\n {msg}").lower()

            if choice in valid_choice:
                return choice

            else:
                self.display_error_message(self, msg="Choix invalide")

    def display_message(self, msg: str):
        """Settings messages of view app, view_player or view_tournament which use it"""
        print("\n")
        print(Fore.WHITE + Style.BRIGHT + msg)

    def display_section_subtitles(self, msg: str):
        """Settings messages under menus of view app, view_player or view_tournament which use it"""
        print(Fore.WHITE + Style.DIM + msg.center(100) + "\n")

    def display_error_message(self, msg: str):
        """Settings error messages in App's / Player's / Tournament's controller and view which uses it"""
        print("\n" + Fore.RED + Style.BRIGHT + msg)

    def display_success_message(self, msg: str):
        """Settings success messages in App's / Player's / Tournament's controller and view which uses it"""
        print("\n" + Fore.GREEN + Style.BRIGHT + msg)

    def main_menu_settings(self, msg: str) -> str:
        """Settings the title of main menu in view_app"""
        print("\n")
        print(Fore.WHITE + Back.RED + Style.BRIGHT + msg.center(100))

    def player_menu_settings(self, msg: str):
        """Settings the title of player menu in view_player"""
        print("\n")
        print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + msg.center(100))

    def tournament_menu_settings(self, msg: str):
        """Settings the title of tournament menu in view_tournament"""
        print("\n")
        print(Fore.WHITE + Back.BLUE + Style.BRIGHT + msg.center(100))

    def player_sections_settings(self, msg: str):
        """Settings the title of each section of player menu"""
        print("\n" + Fore.MAGENTA + Back.BLACK + Style.BRIGHT + msg.center(100))

    def player_fields_settings(self, msg: str):
        """Settings fields of each section of player menu which uses it"""
        print("\n" + Fore.MAGENTA + Back.BLACK + Style.BRIGHT + msg)

    def tournament_sections_settings(self, msg: str):
        """Settings the title of each section of tournament menu"""
        print("\n" + Fore.CYAN + Style.BRIGHT + msg.center(100))

    def round_sections_settings(self, msg: str):
        """Settings the title of each section of tournament menu"""
        print("\n" + Fore.YELLOW + Style.BRIGHT + msg.center(100))

    def table_settings(self, headers, title: str, items: list):
        """Settings the visual of a dynamic table with datas ( from Player or Tournament object) with Rich"""

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
            # Convertion en str des éventuels int pour compatibilité avec le rendu de Table
            values = [str(value) for value in item.values()]
            table.add_row(*values)

        console = Console()
        print("")
        console.print(table)

    def get_user_answer(self, label):
        """Display field "Enter your choice" and returns the user's response"""

        while True:
            value = input(Fore.WHITE + Style.BRIGHT + f"\n {label}").lower()
            return value

    def get_int(self, label):
        """Returns a value compatible with integer"""

        while True:
            value = input(Fore.WHITE + Style.DIM + f"{label} : ")

            if value.lower() == EXIT_CODE:
                raise CancelError

            if value.lower() == QUIT_CODE:
                self.display_message("Au revoir !")
                exit()

            try:
                int(value)
                return value

            except ValueError:
                self.display_error_message("Veuillez entrer uniquement un entier")

    def get_alpha_string(self, label: str) -> str:
        """Returns a value compatible with an alpha string and a value > 0"""

        while True:
            value = input(Fore.WHITE + Style.DIM + f"{label} : ")
            value = str.capitalize(value)

            if value.lower() == EXIT_CODE:
                raise CancelError

            if value.lower() == QUIT_CODE:
                self.display_message("Au revoir !")
                exit()

            if value.isalpha() or value.split():
                return value
            self.display_error_message(
                "Veuillez entrer une chaîne de caractères uniquement composée de lettres (au moins une)"
            )

    def get_alphanum(self, label: str, min_len=1, max_len=255) -> str:
        """Returns a value compatible with a alphanumeric string and a value > 0"""

        while True:
            value = input(Fore.WHITE + Style.DIM + f"{label} : ")
            value = str.capitalize(value)

            if value.lower() == EXIT_CODE:
                raise CancelError

            if value.lower() == QUIT_CODE:
                self.display_message("Au revoir !")
                exit()

            if not min_len <= len(value) <= max_len:
                self.display_error_message(
                    f"Veuillez entrer une chaîne de caractères entre {min_len} et {max_len} caractères"
                )
                continue

            if value.isalnum() or value.split():
                return value

            self.display_error_message(
                "Veuillez entrer une chaîne de caractère uniquement composée de lettres et de chiffres"
            )

    def get_date(self, label) -> str:
        """Returns a date value in string format"""

        valid_date = False

        while valid_date is False:
            date_value = input(
                Fore.WHITE + Style.DIM + f"{label} au format JJ-MM-AAAA : "
            )

            try:
                formated_date = datetime.strptime(date_value, "%d-%m-%Y").date()

                if date_value.lower() == EXIT_CODE:
                    raise CancelError

                if date_value.lower() == QUIT_CODE:
                    self.display_message("Au revoir !")
                    exit()

            except ValueError:
                self.display_error_message(
                    "Veuillez entrer une date valide au format JJ-MM-AAAA"
                )

                continue

            now = datetime.now().date()

            if not formated_date < now:
                valid_date = True
                return date_value

            else:
                self.display_error_message(
                    "Veuillez entrer une date égale ou supérieure à la date du jour"
                )

    def get_player_date_of_birth(self):
        """Displays field for date of birth with age limit condition and returns the user's response"""
        valid_birthday = False

        while valid_birthday is False:
            date_of_birth = input(
                Fore.WHITE + Style.DIM + "Date de naissance au format JJ-MM-AAAA : "
            )

            if date_of_birth.lower() == EXIT_CODE:
                raise CancelError

            if date_of_birth.lower() == QUIT_CODE:
                self.display_message("Au revoir !")
                exit()

            try:
                formated_date = datetime.strptime(date_of_birth, "%d-%m-%Y")

            except ValueError:
                self.display_error_message(
                    "Veuillez entrer une date valide au format JJ-MM-AAAA"
                )
                continue

            now = datetime.now()

            if now.year - formated_date.year >= 18:
                valid_birthday = True
                return date_of_birth

            else:
                self.display_error_message(
                    "Vous devez avoir au moins 18 ans pour vous inscrire"
                )

    def get_player_number(self, label):
        """Returns the player number checking that number is even"""
        while True:
            player_number = self.get_int(label)

            if int(player_number) % 2 == 0:
                return player_number
            else:
                self.display_error_message("Veuillez entrer un nombre de joueurs pair")
