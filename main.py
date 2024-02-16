from colorama import init


from chess.controllers.app import AppController

init(autoreset=True)


def main():
    """Starts the app via app_controller object"""

    app = AppController()
    app.start()


if __name__ == "__main__":
    main()
