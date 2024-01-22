from controllers.app import AppController

from colorama import init

init(autoreset=True)


def main():
    """Starts the app via app_controller object"""

    app = AppController()
    app.start()


if __name__ == "__main__":
    main()
