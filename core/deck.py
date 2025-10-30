def create_card(rank:str,suite:str):
   
    card = dict(rank = rank.upper(), suite = suite.upper())
    
    return card



def build_standard_deck() -> list[dict]:
    deck_of_cards = []
    LIST_SUITE = ["h","c","d","s"]
    LIST_RANK = ["2","3","4","5","6","7","8","9","10","j","k","q","a"]
    for suite in LIST_SUITE:
        for rank in LIST_RANK:
            deck_of_cards.append(create_card(rank,suite))
    
    return deck_of_cards

 
    






def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    return [{}]

