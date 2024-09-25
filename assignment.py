import random

# تعريف البطاقات
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

# دالة لتحديد قيمة البطاقة
def card_value(card):
    rank = card.split(' ')[0]
    return ranks.index(rank)

# خلط الأوراق
random.shuffle(deck)

# توزيع الأوراق على اللاعبين
player1_card = deck.pop()
player2_card = deck.pop()

print(f"Player 1 card: {player1_card}")
print(f"Player 2 card: {player2_card}")

# تحديد الفائز
if card_value(player1_card) > card_value(player2_card):
    print("Player 1 wins!")
elif card_value(player1_card) < card_value(player2_card):
    print("Player 2 wins!")
else:
    print("It's a tie!")