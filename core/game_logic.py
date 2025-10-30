from deck import create_card,build_standard_deck
from player_io import ask_player_action
deck = build_standard_deck()
player = {"hand": [ ] }
dealer = {"hand": [ ] }

def calculate_hand_value(hand: list[dict]) -> int:
    val_hand = 0
    SPECIAL_RANK = {"J":10,"Q":10, "K":10, "A":1}
    special_rank_keys = SPECIAL_RANK.keys()
    for car in hand:
        if car["rank"] in special_rank_keys:
            val_hand += SPECIAL_RANK[car["rank"]]
        else:
            val_hand = int(car["rank"])

    return val_hand







def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    print(calculate_hand_value(dealer["hand"]))
    print(calculate_hand_value(player["hand"]))
   



   




def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while not val>= 17:
        dealer["hand"].append(deck.pop(0))
        val = calculate_hand_value(dealer["hand"])
        if val > 21:
            print(val)
            return False
        else:
            continue
        
    return True



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while True:
        player_t = ask_player_action()
        if player_t == "H":
            player["hand"].append(deck.pop(0))
            val_p = calculate_hand_value(player["hand"])
            print(val_p)
            if val_p > 21:
                print("you lost")
                break
            else:
                continue
        elif player_t == "S":
            break    
    if val_p <= 21:
        d_t = dealer_play(deck, dealer)
        if d_t:
            if val_p > calculate_hand_value(dealer["hand"]):
                print("you won")
            elif val_p < calculate_hand_value(dealer["hand"]):
                print("d won")
            else:
                print("teko")         
    else:
        print("you lost")







    