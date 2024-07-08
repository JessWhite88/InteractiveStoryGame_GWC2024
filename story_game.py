def start_game():
    print("You are in a dark forest. Do you go left or right?")
    choice = input("Enter 'left' or 'right': ")
    if choice == 'left':
        encounter_dragon()
    elif choice == 'right':
        fall_in_pit()
    else:
        print("Invalid choice. Try again.")
        start_game()

def encounter_dragon():
    print("You encounter a friendly dragon. He gives you treasure. You win!")
    restart_game()

def fall_in_pit():
    print("You fall into a pit. Game over!")
    restart_game()

def restart_game():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        print("Thanks for playing!")
    else:
        print("Invalid choice. Try again.")
        restart_game()

start_game()