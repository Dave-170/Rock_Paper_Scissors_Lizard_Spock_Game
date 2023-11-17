import random

def get_user_choice():
    """Get the user's choice (rock, paper, scissors, lizard, or spock)."""
    while True:
        user_choice = input("Choose: rock, paper, scissors, lizard, or spock: ").lower()
        if user_choice in ["rock", "paper", "scissors", "lizard", "spock"]:
            return user_choice
        else:
            print("Invalid choice. Please choose from rock, paper, scissors, lizard, or spock.")

def get_computer_choice():
    """Generate the computer's random choice."""
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or
        (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or
        (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or
        (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or
        (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock"))
    ):
        return f"You win! {user_choice} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice} beats {user_choice}."

def main():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    
    play_game = input("Would you like to play? (yes/no): ")

    """Check if the user wants to play."""
    if play_game.lower() != "yes":
        print("Goodbye!") 
        return

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

