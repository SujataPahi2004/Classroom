import random
import sys

def play_game():
    choices = ['rock', 'paper', 'scissors']
    wins_against = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    user_wins = 0
    computer_wins = 0

    print("Welcome to Rock Paper Scissors!")
    print("Enter your choice (rock, paper, scissors) or 'quit' to exit.")

    while True:
        user_choice = input("\nYour choice: ")  # Get input from the user
        print(f"\nYour choice: {user_choice}")
        
        if user_choice == 'quit':
            print(f"Final score - You: {user_wins} | Computer: {computer_wins}")
            print("Thanks for playing!")
            sys.exit()  # Exit the program
            
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif wins_against[user_choice] == computer_choice:
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"Current score - You: {user_wins} | Computer: {computer_wins}")

        play_again = input("\nPlay again? (yes/no): ")  # Get input for playing again
        if play_again not in ['yes', 'y']:
            print(f"Final score - You: {user_wins} | Computer: {computer_wins}")
            print("Thanks for playing!")
            break

    restart_game()

def restart_game():
    play_again = input("\nDo you want to restart the game? (yes/no): ")
    if play_again.lower() in ['yes', 'y']:
        play_game()
    else:
        print("Thanks for playing!")
        sys.exit()  # Exit the program

if __name__ == "__main__":
    play_game()
