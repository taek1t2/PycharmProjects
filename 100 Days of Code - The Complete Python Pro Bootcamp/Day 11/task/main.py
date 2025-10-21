import random
def get_accurate_score(in_hand):
    score = 0
    num_ace = 0
    for card in in_hand:
        score += card
        if card == 11:
            num_ace += 1

    while score > 21 and num_ace > 0:
        score -= 10
        num_ace -= 1
    return score

while True:
    start_blackjack = input("Do you want to play a game of Blackjack? (y/n) \n").lower()
    print("\n" * 20)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)

    import art
    print(art.logo)

    player_hand = []
    computer_hand = []
    if start_blackjack == "y":
        first_draw = random.choice(cards)
        player_hand.append(first_draw)
        second_card = random.choice(cards)
        player_hand.append(second_card)
        current_score = get_accurate_score(player_hand)
        print(f"Your cards: {player_hand}, current score: {current_score}")

        computer_first_card = random.choice(cards)
        computer_hand.append(computer_first_card)
        hidden_display = "_"
        another_card = random.choice(cards)
        computer_hand.append(another_card)
        puter_score = get_accurate_score(computer_hand)
        print(f"Dealer's first card: {[computer_hand[0], hidden_display]}\n")

        round_over = False
        if current_score == 21 and puter_score == 21:
            print(f"Dealer's hand: {computer_hand}, Dealer's score: {puter_score}")
            print("Push! - Both are blackjack!")
            round_over = True
        elif current_score == 21:
            print(f"Dealer's hand: {computer_hand}, Dealer's score: {puter_score}")
            print("Blackjack! You win!")
            round_over = True
        elif puter_score == 21:
            print(f"Dealer's hand: {computer_hand}, Dealer's score: {puter_score}")
            print("Dealer Blackjack - You lose!")
            round_over = True

        if round_over:
            continue

        if not round_over:
            while True:
                hit_or_stand = input('Type "hit" to get another card OR type "stand" to pass: \n').lower()

                if hit_or_stand == "hit":
                    draw_another_card = random.choice(cards)
                    player_hand.append(draw_another_card)
                    current_score = get_accurate_score(player_hand)
                    print(f"Your cards: {player_hand}, current score: {current_score}")
                    print(f"Dealer's first card: {[computer_hand[0], hidden_display]}\n")
                    if current_score > 21:
                        puter_score = get_accurate_score(computer_hand)
                        print(f"Dealer's hand: {computer_hand}, Dealer's score: {puter_score}")
                        print("Player's bust - You lose!")
                        break

                elif hit_or_stand == "stand":
                    puter_score = get_accurate_score(computer_hand)
                    print(f"Dealer's hand: {computer_hand}, Dealer's score: {puter_score}")

                    while puter_score < 17:
                        dealer_draws = random.choice(cards)
                        computer_hand.append(dealer_draws)
                        puter_score = get_accurate_score(computer_hand)
                        print(f"Dealer's hand: {computer_hand}, Dealer's score: {puter_score}")

                        if puter_score > 21:
                            print("Dealer busts - You win!")
                        elif current_score == puter_score:
                            print("Push! It's a tie.")
                        elif current_score < 21 and puter_score < 21 and current_score > puter_score:
                            print("You win!")
                        elif puter_score < 21 and current_score < 21 and current_score < puter_score:
                            print("You lose!")
                        break

                else:
                    print("Type 'hit' or 'stand' to continue.")
                    break
    else:
        print("Thanks for playing! Goodbye.")
        break
