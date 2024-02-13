from colorama import init

from controllers.app import AppController

init(autoreset=True)


def main():
    """Starts the app via app_controller object"""

    app = AppController()
    app.start()


if __name__ == "__main__":
    main()
