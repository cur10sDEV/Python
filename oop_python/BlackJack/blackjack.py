import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
your_cards = []
computer_cards = []

def sum_of_cards():
    total = 0
    for card in your_cards:
        total += card
    return total

def turn(times):
        for i in range(times):
            your_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
        print(f"Your Cards: {your_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        return

def final():
        print(f"Your final hand: {your_cards}")
        print(f"Computer's final hand: {computer_cards}")
        if sum(computer_cards) > 21:
            print("Computer Lose")
        elif sum(your_cards) == sum(computer_cards):
            print("Draw")
        elif sum(your_cards) > sum(computer_cards):
            print("You Win")
        else:
            print("Computer Wins")
        return

def start():
    enter = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if enter == "y":
        turn(2)
        return True
    else:
        return False
        
to_continue = start()

while to_continue == True:
    another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if another == "y":
        total = sum_of_cards()
        if total > 21:
            print(f"Your final hand: {your_cards}")
            print(f"Computer's final hand: {computer_cards}")
            print("You Lose because your cards exceed 21")
        elif total <= 21:
            turn(1)
            total = sum_of_cards()    
            if total > 21:
                print(f"Your final hand: {your_cards}")
                print(f"Computer's final hand: {computer_cards}")
                print("You Lose because your cards exceed 21")
                start()
                
    elif another == "n":
        final()
        your_cards = []
        computer_cards = []
        to_continue = start()
        if to_continue == False:
            break
