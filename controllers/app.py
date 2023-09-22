from controllers.tournament import TournamentController
from controllers.player import PlayerController
from views.view_app import ViewApp

import datetime


class AppController:

    """Crée un objet qui centralise l'éxécution du programme"""

    def __init__(self) -> None:
        self.view_app = ViewApp()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()

    def start(self):
        """Affiche le MENU PRINCIPAL et renvoie le résultat du choix de l'utilisateur : Menu Gestion de tournoi, Menu Gestion des joueurs, Quitter le programme"""

        exit_requested = False

        while not exit_requested:
            choice = self.view_app.display_main_menu()

            if choice == "1":
                self.tournament_controller.manage_tournament()
            elif choice == "2":
                self.player_controller.manage_player()
            elif choice == "Q" or choice == "q":
                exit()
