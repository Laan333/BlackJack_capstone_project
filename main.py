import random
from imgs.ascii_imgs import *

user_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)


def random_card():
    return random.choice(cards)


def sum_cards(card_list: list) -> int:
    summ_cards = sum(card_list)
    if len(card_list) <= 2 and summ_cards == 21:
        return 0
    if summ_cards > 21:
        cards[0] = 1
    return summ_cards


def check_win():
    if user_sum == 0:
        return "User Win - BlackJack"
    elif computer_sum == 0:
        return "Computer win - BlackJack"
    elif user_sum < 21 and computer_sum < 21:
        if user_sum > computer_sum:
            return True
        elif user_sum == computer_sum:
            return "Draw"
        else:
            return False
    elif user_sum > 21:
        return False
    elif computer_sum > 21:
        return True


for i in range(2):
    user_cards.append(random_card())
    computer_cards.append(random_card())

user_sum = sum_cards(user_cards)
computer_sum = sum_cards(computer_cards)
print(f"Your cards is: {user_cards}, current score: {user_sum}")
print(f"Computer`s first card: {computer_cards[0]}")
user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
if user_choice == "y":
    user_cards.append(random_card())
    user_sum = sum_cards(user_cards)
    print(f"You took one more card {user_cards}, current score: {user_sum}")
    if computer_sum < 17:
        computer_cards.append(random_card())
        print(f"Computer took one more card {computer_cards}")
    computer_sum = sum_cards(computer_cards)
elif user_choice == "n":
    pass

result = check_win()
if result is True:
    print(f"User win {user_sum}, computer score : {computer_sum}")
elif result == "Draw":
    print(result)
elif result == "User Win - BlackJack":
    print(result)
elif result == "Computer win - BlackJack":
    print(result)
else:
    print(f"Computer win {computer_sum}, user score {user_sum}")
