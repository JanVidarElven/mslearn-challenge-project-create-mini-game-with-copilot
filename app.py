# write 'hello world' to the console
print('hello world')

# I want to create a mini game where I play rock, paper, scissors against the computer using the following specificiations: The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option. At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent. By the end of each round, the player can choose whether to play again. Display the player's score at the end of the game. The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def get_computer_choice():
    choices = ['stein', 'papir', 'saks']
    return random.choice(choices)

def get_user_choice():
    choice = input("Velg stein, papir eller saks: ").lower()
    while choice not in ['stein', 'papir', 'saks']:
        choice = input("Ugyldig valg. Prøv igjen: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'uavgjort'
    if (user_choice == 'stein' and computer_choice == 'saks') or \
       (user_choice == 'papir' and computer_choice == 'stein') or \
       (user_choice == 'saks' and computer_choice == 'papir'):
        return 'bruker'
    return 'datamaskin'

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'bruker':
            user_score += 1
            print(f"Du valgte {user_choice}, datamaskinen valgte {computer_choice}. Du vinner denne runden!")
        elif winner == 'datamaskin':
            computer_score += 1
            print(f"Du valgte {user_choice}, datamaskinen valgte {computer_choice}. Datamaskinen vinner denne runden!")
        else:
            print(f"Begge valgte {user_choice}. Det er uavgjort!")
        play_again = input("Vil du spille igjen? (ja/nei) ").lower()
        if play_again != 'ja':
            print(f"Spillet er over. Din poengsum: {user_score}, datamaskinens poengsum: {computer_score}")
            break

play_game()