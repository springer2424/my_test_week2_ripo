def ask_player_action() -> str:
    chois = input("enter H/S")
    while chois == "H" or chois == "S":
        if chois == "S":
            return "S"
        elif chois == "H":
            return "H"



    