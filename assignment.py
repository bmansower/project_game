import random



def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck



def deal_cards(deck, num_players):
    player_hands = []
    hand_size = len(deck) // num_players
    for i in range(num_players):
        player_hands.append(deck[i * hand_size:(i + 1) * hand_size])
    return player_hands

def card_value(card):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return rank_values[card[0]]




def play_round(players_cards):
    played_cards = []
    for i, player_cards in enumerate(players_cards):
        if player_cards:
            played_card = player_cards.pop(0)
            played_cards.append((i, played_card))
            print(f"Player {i + 1} plays: {played_card[0]} of {played_card[1]}")


    winner = max(played_cards, key=lambda x: card_value(x[1]))
    winner_index = winner[0]
    
    for _, card in played_cards:
        players_cards[winner_index].append(card)
    
    print(f"Player {winner_index + 1} wins the round!\n")

def play_game(num_players):
    deck = create_deck()
    players_cards = deal_cards(deck, num_players)

    round_number = 1
    while all(players_cards):
        print(f"Round {round_number}:")
        play_round(players_cards)
        round_number += 1


    for i, player_cards in enumerate(players_cards):
        if player_cards:
            print(f"Player {i + 1} wins the game!")
            break



while True:
    try:
        num_players = int(input("Enter the number of players (2-4): "))
        if 2 <= num_players <= 4:
            break
        else:
            print("Please enter a valid number of players (between 2 and 4).")
    except ValueError:
        print("Invalid input. Please enter a number.")



play_game(num_players)



