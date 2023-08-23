from models.model_player import Player
from views.view_player import ViewPlayer


class PlayerController:
    def __init__(self) -> None:
        self.view = ViewPlayer()

    def manage_player(self):
        """Affiche le MENU "GESTION DES JOUEURS" et renvoie le résultat du choix de l'utilisateur"""

        exit_requested = False

        while not exit_requested:
            choice = ViewPlayer.display_player_menu(self)

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.display_players_by_surname()
            elif choice == "3":
                exit_requested = True

    def create_player(self):
        print("============[Création joueur]============")
        surname = self.view.get_player_surname()
        first_name = self.view.get_player_name()
        date_of_birth = self.view.get_player_date_of_birth()
        national_chess_id = self.view.get_player_national_chess_id()
        total_score = 0
        player = Player(
            surname, first_name, date_of_birth, national_chess_id, total_score
        )
        player.save()

        return

    def display_players_by_surname(self):
        print("==[Affichage des joueurs par ordre Alphabétique]==")
        Player.display_by_surname(self)
        ViewPlayer.print_players_list_by_surname(self)

        return
