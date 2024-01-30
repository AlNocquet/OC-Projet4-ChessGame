from views.view_base import BaseView, CancelError, EXIT_CODE, QUIT_CODE

from colorama import Fore, Style


class ViewPlayer(BaseView):
    def display_player_menu(self):
        """Displays the Player Menu and returns the user's choice"""

        while True:
            print("\n")
            self.player_menu_settings("MENU JOUEUR")
            self.display_section_subtitles(
                "Tapez Exit pour revenir au menu précédent, Quit pour quitter le programme"
            )

            print("1. Créer un joueur")
            print("2. Modifier un joueur")
            print("3. Supprimer un joueur")
            print("4. Consulter Joueurs par ordre alphabétique")

            choice = self.get_user_answer(label=f"Entrez votre choix : ")

            if choice in ["1", "2", "3", "4", "exit", "quit"]:
                if choice.lower() == EXIT_CODE:
                    self.display_message(f"Ok !")

                if choice.lower() == QUIT_CODE:
                    self.display_message(f"Au revoir !")

                return choice

            else:
                self.display_error_message(f"Choix invalide")

    def display_fields_new_player(self) -> dict:
        """Displays fields for player's creation and returns the user's response"""

        self.player_sections_settings("CRÉATION DU JOUEUR")
        self.display_section_subtitles(
            "Tapez Exit pour revenir au MENU JOUEUR, Quit pour quitter le programme"
        )

        print("\n")

        surname = self.get_alpha_string(label=f"\n Nom de famille du joueur")
        first_name = self.get_alpha_string(label=f"\n Prénom du joueur")
        date_of_birth = self.get_player_date_of_birth()
        national_chess_id = self.get_alphanum(
            f"\n Identifiant national d échec de la fédération", min_len=7, max_len=7
        )

        return {
            "surname": surname,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "national_chess_id": national_chess_id,
        }

    def get_player_id_to_update(self):
        """Displays field to get player's id and returns the user's response"""

        self.player_sections_settings("MODIFICATION DU JOUEUR")
        self.display_section_subtitles(
            "Tapez Exit pour revenir au MENU JOUEUR, Quit pour quitter le programme"
        )

        player_id = input(
            Fore.MAGENTA
            + Style.BRIGHT
            + "\n Indiquez l'id_db du joueur à modifier dans la base : "
            + Style.RESET_ALL
        )

        if player_id.lower() == EXIT_CODE:
            raise CancelError

        if player_id.lower() == QUIT_CODE:
            self.display_message(f"Au revoir !")
            exit()

        return player_id

    def display_fields_player_to_update(self):
        """Displays choices and fields for player's updating and returns the user's response"""

        while True:
            self.player_fields_settings(f"Indiquez le champs à modifier : \n")

            print("1. Nom de famille")
            print("2. Prénom")
            print("3. Date de naissance")
            print("4. Identifiant national d'échec de la fédération")

            choice = self.get_user_answer(label=f"Entrez votre choix : ")

            if choice in ["1", "2", "3", "4"]:
                if choice == "1":
                    surname = self.get_alpha_string(
                        label=f"\n Nom de famille du joueur"
                    )
                    return {"surname": surname}

                elif choice == "2":
                    first_name = self.get_alpha_string(label=f"\n Prénom du joueur")
                    return {"first_name": first_name}

                elif choice == "3":
                    date_of_birth = self.get_player_date_of_birth()
                    return {"date_of_birth": date_of_birth}

                elif choice == "4":
                    national_chess_id = self.get_alphanum(
                        f"\n Identifiant national d échec de la fédération",
                        min_len=7,
                        max_len=7,
                    )
                    return {"national_chess_id": national_chess_id}

                return choice

            else:
                self.display_error_message(f"Choix invalide")

    def get_player_id_to_remove(self):
        """Displays field to get player's id and returns the user's response"""

        self.player_sections_settings(f"SUPPRESSION DU JOUEUR")
        self.display_section_subtitles(
            "Tapez Exit pour revenir au MENU JOUEUR, Quit pour quitter le programme"
        )

        player_id = input(
            Fore.MAGENTA
            + Style.BRIGHT
            + "\n Indiquez l'id_db du joueur à supprimer de la base : "
            + Style.RESET_ALL
        )

        if player_id.lower() == EXIT_CODE:
            raise CancelError

        if player_id.lower() == QUIT_CODE:
            self.display_message(f"Au revoir !")
            exit()

        return player_id

    def get_tournament_players_id(
        self, player_number: int, valid_players_id: list
    ) -> list[str]:
        """Displays field to get list of player's ids and returns the user's response"""

        while True:
            players_id_str: str = input(
                Fore.BLUE
                + Style.BRIGHT
                + f"\n Indiquez l'id_db des {player_number} joueurs à ajouter au tournoi, séparés par un espace : "
                + Style.RESET_ALL
            )

            if not players_id_str:
                return

            if players_id_str.lower() == EXIT_CODE:
                raise CancelError

            if players_id_str.lower() == QUIT_CODE:
                self.display_message(f"Au revoir !")
                exit()

            players_id: list = players_id_str.split()

            bad_id = []
            for db_id in players_id:
                if db_id not in valid_players_id:
                    bad_id.append(db_id)

            if len(bad_id) > 0:
                self.display_error_message(
                    f"\n Les identifiants suivants ne sont pas valides : {bad_id}"
                )
                continue

            if len(players_id) == player_number:
                return players_id

            else:
                self.display_error_message(
                    f"\n Saisie invalide. Vous devez indiquer {player_number} identifiants"
                )
