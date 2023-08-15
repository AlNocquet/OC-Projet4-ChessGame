from models.model_player import Player
from views.view_player import ViewPlayer
from datas.data_player import DataPlayer


class PlayerController:
    def __init__(self) -> None:
        self.view = ViewPlayer()
        self.datas = DataPlayer()

    def manage_player(self):
        """Affiche le MENU "GESTION DES JOUEURS" et renvoie le résultat du choix de l'utilisateur"""

        exit_requested = False

        while not exit_requested:
            choice = self.view.display_player_menu()

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.edit_player()
            elif choice == "3":
                self.show_players_by_surname()
            elif choice == "4":
                exit_requested = True

    def create_player(self):
        print("============[Création joueur]============")
        surname = self.view.get_player_surname()
        name = self.view.get_player_name()
        date_of_birth = self.view.get_player_date_of_birth()
        national_chess_id = self.view.get_player_national_chess_id()
        player = Player(surname, name, date_of_birth, national_chess_id)
        serialized_player = player.serialized_player()
        self.Database.save_player(serialized_player)

        return

    # def edit_player(self):

    # def show_players_by_surname(self):

    # tabulate
