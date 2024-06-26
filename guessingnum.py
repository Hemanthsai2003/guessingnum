import random
def gameplay():
    image_num = random.randrange(1, 59)
    print("Let me think of a number")
    level = input("Enter level of difficulty: Easy or Hard: ").strip().lower()
    if level == 'easy':
        lives = 10
        print("You have 10 attempts to guess the number.")
    else:
        lives = 5
        print("You have 5 attempts to guess the number.")

    end_operation = False

    while not end_operation:
        user_num = input("Make a guess: ")
        if not user_num.isdigit():
            print("Please enter a valid number.")
            continue

        user_num = int(user_num)
        if user_num == image_num:
            print(f"Your guess is correct! The answer is {image_num}.")
            break
        elif user_num > image_num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

        lives -= 1
        print(f"You have {lives} lives left.")
        if lives == 0:
            print(f"Your lives are completed. You lost! The correct number was {image_num}.")
            end_operation = True

while True:
    gameplay()
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay != 'yes':
        print("Thanks for playing!")
        break