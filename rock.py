import random

def get_user_choice():
    while True:
        user_choice = input("Choose 1, 2, or 3: ").lower()
        rock=1
        paper=2
        scissors=3
        if user_choice in ["1", "2", "3"]:
            return user_choice
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def get_computer_choice():
    return random.choice(["1", "2", "3"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "1" and computer_choice == "3") or
        (user_choice == "3" and computer_choice == "2") or
        (user_choice == "2" and computer_choice == "1")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
