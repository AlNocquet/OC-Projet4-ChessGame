from models.model_app import Tournament
from models.model_app import Round
from models.model_app import Match
from views.view_tournament import ViewTournament
from datas.data_player import DataPlayer
from datas.data_app import DataApp


class TournamentController:
    def __init__(self) -> None:
        self.view = ViewTournament()

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

    def create_tournament(self):
        print("============[Création de tournoi]============")
        player_table = DataPlayer.player_table
        if len(player_table) == 8:
            name = self.view.get_tournament_name()
            place = self.view.get_tournament_place()
            date = self.view.get_tournament_date()
            # time_control = self.view.get_tournament_time_control()
            description = self.view.get_tournament_description()
            tournament = Tournament(name, place, date, description)
            tournament.save()  # Enregistre le tournoi dans Database.json via model_app.py
            self.add_players_tournament()  # Ajoute joueurs (au moins 8) suite création du tournoi
            # Def ou import def : print(f"Désolé, {joueur} ne fait pas partie de la liste des joueurs")
            # Def ou import def : Pairer les joueur, Else : print(f"Désolé, {joueur} ne fait pas partie de la liste des joueurs")
            self.create_turn()  # Créer un Round (Tour) suite création du tournoi
            return

        else:
            return self.view.create_tournament_false(
                player_table
            )  # Pas assez de joueurs

    def add_players_tournament(self):
        """Affiche les joueurs enregistrés dans Database.json et renvoie le choix du joueur de l'utilisateur"""
        DataPlayer.extract_players_list(self)

    def create_turn(self):
        """Créer un Round (Tour)"""
        pass

    def display_tournaments(self):
        print("==[Affichage des tournoir enregistrés]==")
        Tournament.display(self)
        ViewTournament.print_registered_tournaments(self)

        return

    def show_tournament_list():
        pass

    def show_tournament_players_by_surname():
        pass

    def show_tournament_rounds():
        pass

    def show_tournament_matchs():
        pass
