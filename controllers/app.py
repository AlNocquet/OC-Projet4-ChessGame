from controllers.tournament import TournamentController
from controllers.player import PlayerController
from views.view_app import ViewApp
from views.view_base import QUIT_CODE


class AppController:
    """Creates AppController object which centralizes the execution of the app"""

    def __init__(self) -> None:
        self.view_app = ViewApp()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()

    def start(self):
        """Manages the MAIN MENU and returns the user's choice"""

        while True:
            choice = self.view_app.display_main_menu()

            if choice == "1":
                self.tournament_controller.manage_tournament_menu()
            elif choice == "2":
                self.player_controller.manage_player()
            elif choice == QUIT_CODE:
                exit()
