from controllers.app import AppController


def main():
    """Démarre l'application via l'objet app_controller qui centralise la gestion du programme"""

    app = AppController()
    app.start()


if __name__ == "__main__":
    main()
