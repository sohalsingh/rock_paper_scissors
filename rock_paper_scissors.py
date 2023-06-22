import random

def play_game():
    print("Let's play Rock-Paper-Scissors!")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

# Start the game
play_game()
