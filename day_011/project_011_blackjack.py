import blackjack_art as ba
import random
import os

playing = True

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
       'J', 'Q', 'K', 'A',
       'J', 'Q', 'K', 'A',
       'J', 'Q', 'K', 'A',
       'J', 'Q', 'K', 'A']

player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0

def deal_card(hand):
    card = random.choice(deck)
    hand.append(card)

def score(hand):
    score = 0
    jack = ['J', 'Q', 'K']
    ace = ['A']

    for i in hand:
        if i in jack:
            score += 10
        elif isinstance(i, int):
            score += i
        else:
            score = score

    for i in hand:
        if i in ace:
            if score > 11:
                score += 1
            else:
                score += 11
    
    return score

def winner(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score == 21:
        return "It's a blackjack, you win!"
    elif dealer_score == 21:
        return "You lose, opponent has Blackjack!"
    elif player_score > 21:
        return "You went over, you lose!"
    elif dealer_score > 21:
        return "Opponent went over, you win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def reset_game():
    global player_score
    global dealer_score
    global playing
    global player_cards
    global dealer_cards

    playing = True
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    os.system('cls')

def play():
    global playing
    global player_score
    global dealer_score

    for i in range(2):
        deal_card(player_cards)
        deal_card(dealer_cards)

    while playing:
        print(ba.logo)

        player_score = score(player_cards)
        dealer_score = score(dealer_cards)

        if player_score < 21:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Dealer card: {dealer_cards[0]}")

            new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            
            if new_card == 'y':
                deal_card(player_cards)
                os.system('cls')
            else:
                playing = False
        else:
            playing = False

    while dealer_score < 17:
        deal_card(dealer_cards)
        dealer_score = score(dealer_cards)

    os.system('cls')

    player_score = score(player_cards)
    dealer_score = score(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer card: {dealer_cards}, current score: {dealer_score}")
    print(winner(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    reset_game()
    play()