from POKESTARTER import delete_save

action_dict = {
    "fight": lambda: print("You chose to fight!"),
    "run": lambda: print("You chose to run!"),
    "catch": lambda: print("You chose to catch!"),
    "delete save": delete_save,
    "exit": lambda: (print("Exiting the game."), exit())
}