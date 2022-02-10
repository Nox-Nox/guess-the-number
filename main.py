import random


def pick_a_number():
    num = int(input("choose a number between 1 to 10"))
    print(num)
    while num < 1 or num > 10:
        num = int(input("Your guessed number is out of the given range, please choose a number between 1 to 10"))
    return num


if __name__ == '__main__':
    guessed = False

while not guessed:

    ai_chosen_number = random.randrange(1, 10)
    number = pick_a_number()
    if number == ai_chosen_number:
        print("You guessed the right number!")
        guessed = True
    else:
        print(f"You failed, the right number was {ai_chosen_number}, try again!")
