# CHESS GAME

This program allows offline management of chess tournaments.


## Technology

Python


## Author

Alice Nocquet


## Environment setup and program launch

Use the following commands to create a virtual environment, install dependencies, and launch the program:

```bash
$ git clone https://github.com/AlNocquet/OC-Projet4-ChessGame.git
$ cd OC-Projet4-ChessGame
$ python3 -m venv venv           # On Windows: python -m venv venv
$ source venv/bin/activate       # On Windows: venv\Scripts\activate
$ pip install -r requirements.txt
$ python main.py
```


## USAGE

- The user starts by creating players in the database.  
- Only registered players can participate in tournaments.

- When creating a tournament, the user selects players by their JSON database ID (`id_db`).  
- The number of players must match the number of desired rounds.

- The first round matches are generated randomly based on selected players.  
- Subsequent matches are created automatically based on player scores.

- The user can resume an ongoing tournament to continue creating rounds or record scores.

- At any time, the user can type `exit` to cancel the current action and return to the previous menu, or `quit` to exit the program.

- Several reports are available depending on the state of the database.


### MAIN MENU:

- **Tournament Management Menu**
- **Player Management Menu**


### TOURNAMENT MANAGEMENT MENU:

- Create a tournament  
- Load a tournament  
- Show list of tournaments (by date)  
- View list of **ROUNDS** of a tournament  
- View list of **MATCHES** of a tournament  


### PLAYER MANAGEMENT MENU:

- Create a player  
- Edit a player  
- Delete a player  
- View players sorted alphabetically  


## PEP8

`flake8`

Create a `setup.cfg` file with the following configuration:

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

Use the following command to generate a `flake8-html` error report inside the `flake-report` directory:

```bash
flake8 --format html --htmldir flake-report
```
