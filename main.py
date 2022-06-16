from art import logo
from art import vs
from game_data import data
import random
from replit import clear


def dictionary_a():
    random_a_dictionary = random.choice(data)
    print(
        f"Compare A: {random_a_dictionary['name']}, {random_a_dictionary['description']}, from {random_a_dictionary['country']}. ")
    return random_a_dictionary['follower_count']


def dictionary_b():
    random_b_dictionary = random.choice(data)
    print(
        f"Compare B: {random_b_dictionary['name']}, {random_b_dictionary['description']}, from {random_b_dictionary['country']}. ")
    return random_b_dictionary['follower_count']


def compare(user_choice, current_score):
    if user_choice == "A":
        if compare_a > compare_b:
            return True
        else:
            return False
    else:
        if compare_b > compare_a:
            return True
        else:
            return False


def user_input():
    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice == "A":
            return "A"
            break
        elif user_choice == "B":
            return "B"
            break
        else:
            print("Invalid input. Try one more time.")


print("hello")
current_score = 0
print(logo)
compare_a = dictionary_a()
print(vs)
compare_b = dictionary_b()
user_choice = user_input()

while compare(user_choice, current_score):
    current_score += 1
    clear()
    print(logo)
    print(f"You are right! Current score: {current_score}.")
    compare_a = dictionary_a()
    print(vs)
    compare_b = dictionary_b()
    user_choice = user_input()

clear()
print(f"Sorry thats wrong. Final score: {current_score}")