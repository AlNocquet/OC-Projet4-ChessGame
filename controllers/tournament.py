from models.model_app import Tournament
from models.model_app import Round
from models.model_app import Match
from views.view_tournament import ViewTournament


class TournamentController:
    def __init__(self) -> None:
        self.view = ViewTournament

    def manage_tournament(self):
        """Affiche le MENU "GESTION DES TOURNOIS" et renvoie le résultat du choix de l'utilisateur"""

        exit_requested = False

        while not exit_requested:
            choice = self.display_tournament_menu(self)

            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                exit_requested = True

    def create_tournament():
        pass

    def show_tournament_datas():
        pass  # names, dates

    def show_tournament_list():
        pass

    def show_tournament_players_by_surname():
        pass

    def show_tournament_rounds():
        pass

    def show_tournament_matchs():
        pass
