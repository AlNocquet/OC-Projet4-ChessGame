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
        player_data = self.view.get_player_data # import def inputs + dict ViewPlayer
        player = Player(**player_data) # Unpack dico
        self.database_save_player(player) # import def sauvegarde Model Player
        print("Joueur enregistré !")
        return

    # def edit_player(self):

    # def show_players_by_surname(self):

    # tabulate
