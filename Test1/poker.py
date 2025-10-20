import numpy as np
import random
from collections import Counter

# Rangovi i boje (suitovi)
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']

# Kreiraj špil (deck)
deck = [rank + suit for rank in ranks for suit in suits]

# Funkcija za vrednovanje ruke
def evaluate_hand(hand):
    values = [card[:-1] for card in hand]
    suits = [card[-1] for card in hand]  

    value_map = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    values_num = sorted([value_map[v] for v in values], reverse=True)
    counts = Counter(values)
    counts_values = sorted(counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = all(values_num[i] - 1 == values_num[i + 1] for i in range(len(values_num) - 1))

    # Provjera kombinacija
    if is_straight and is_flush:
        return (8, values_num)  # Straight Flush
    elif counts_values == [4, 1]:
        return (7, values_num)  # Four of a Kind
    elif counts_values == [3, 2]:
        return (6, values_num)  # Full House
    elif is_flush:
        return (5, values_num)  # Flush
    elif is_straight:
        return (4, values_num)  # Straight
    elif counts_values == [3, 1, 1]:
        return (3, values_num)  # Three of a Kind
    elif counts_values == [2, 2, 1]:
        return (2, values_num)  # Two Pair
    elif counts_values == [2, 1, 1, 1]:
        return (1, values_num)  # One Pair
    else:
        return (0, values_num)  # High Card

# Funkcija za izvlačenje ruke
def deal_hand():
    return random.sample(deck, 5)

# Primjer: poređenje dvije ruke
hand1 = deal_hand()
hand2 = deal_hand()

print("Ruka 1:", hand1)
print("Ruka 2:", hand2)

rank1 = evaluate_hand(hand1)
rank2 = evaluate_hand(hand2)

if rank1 > rank2:
    print("Ruka 1 je jača")
elif rank1 < rank2:
    print("Ruka 2 je jača")
else:
    print("Izjednačeno!")