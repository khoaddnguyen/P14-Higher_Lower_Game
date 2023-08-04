import random
from art import logo, vs
from game_data import data
from replit import clear



#Format the account data into a printatble format
def format_data(account):
    """Takes the account data and returns into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if user is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#Display art
print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

#Make the game repeatable
while should_continue:
    
    #Generate a random account from the game data
    ##Regenerate account B if acct A == account B
    ##Make account at position B --> position A --> move account_b to be global 
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Clear the screen
    clear()
    print(logo)

    #Give user feedback on their guess
    #Keep score
    if is_correct:
        score += 1
        print(f"You are right! Current score is : {score}.")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score is: {score}.")









