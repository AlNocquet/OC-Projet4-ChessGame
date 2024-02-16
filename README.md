
# CHESS GAME :

## A FAIRE EN ANGLAIS

## IL MANQUE UNE LICENCE


sections habituelles
## About 

## Install

## Usage 

## Contributing




Ce programme permet la gestion de tournois d'échecs en mode hors ligne.

## Technologie :

Python

## Author :

Alice Nocquet


## Installation de l'environnement et lancement du programme :

Utiliser les commandes suivantes pour créer un environnement, installer les requirements et lancer le programme :

```bash
$ git clone https://github.com/AlNocquet/OC-Projet4-ChessGame.git
$ cd OC-Projet4-ChessGame
$ python3 -m venv venv (Sous Windows => python -m venv venv)
$ source venv/bin/activate (Sous Windows => venv\Scripts\activate)
$ pip install -r requirements.txt
$ python main.py
```

## UTILISATION :

    L'utilisateur commence par créer des joueurs dans la base de données.
    Seuls les joueurs enregistrés dans la base de données peuvent participer aux tournois.

    A la création du tournoi, l'utilisateur sélectionne les joueurs par leur identifiant de la base JSON "id_db".
    Le nombre de joueurs du tournoi doit correspondre au nombre de tours (round) souhaité.

    Les matchs du 1er tour (round) sont automatiquement créés par pairage aléatoire des joueurs sélectionnés.
    Les matchs suivant sont automatiquement créés en fonction des scores de ces joueurs.

    L'utilisateur sélectionne le tournoi en cours pour reprendre la création des tours (rounds) et/ou l'enregistrement des scores.

    A tout moment, l'utilisateur peut taper "exit" pour annuler l'action en cours et revenir au menu précédent, "quit" pour quitter le programme.

    Différents rapports sont consultables suivant la mise à jour de la base de données.
        
        
        Dans le MENU PRINCIPAL :
            
            MENU Gestion des Tournois
            MENU Gestion des Joueurs
        
        Dans le menu GESTION DES TOURNOIS :

            Créer un tournoi
            Charger un tournoi
            Afficher liste des Tournois (par date)
            Consulter liste des ROUNDS d'un Tournoi
            Consulter liste des MATCHS d'un Tournoi

        Dans le menu GESTION DES JOUEURS :

            Créer un joueur
            Modifier un joueur
            Supprimer un joueur
            Consulter Joueurs par ordre alphabétique


## PEP8 :

flake8

Créer fichier setup.cfg avec la configuration suivante :

```
[flake8]
exclude =
    .git,    
    .venv,
    venv,
    .idea,
    .pytest_cache,
    .vscode,
    .mypy_cache,
max-complexity = 10
max-line-length = 119
```

Utiliser la commande suivante pour créer un rapport d'erreurs flake8-html qui sera publié dans le répertoire flake-report : 

```bash
flake8 --format html --htmldir flake-report
```
