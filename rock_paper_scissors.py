import random

def get_user_choice():
    print("Choose one of the following:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter your choice (1, 2, or 3): "))
    while choice < 1 or choice > 3:
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice (1, 2, or 3): "))
    return choice

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    choices = ["Rock", "Paper", "Scissors"]
    print(f"You chose {choices[user_choice - 1]}")
    print(f"The computer chose {choices[computer_choice - 1]}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()