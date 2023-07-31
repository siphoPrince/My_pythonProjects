import random

def guess_the_letter_game():
    selected_letter = chr(random.randint(ord('a'), ord('z')))
    print("Welcome to the Guess the letter game!")
    print("Try to guess the random selected letter from a to z.")

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single alphabetical character.")
            continue

        attempts += 1

        if guess == selected_letter:
            print("Congratulations! You guessed the letter correctly:", selected_letter)
            break
        elif guess < selected_letter:
            print("the selected letter is after '{}' in the alphabet.".format(guess))
        else:
            print("the selected letter is before '{}' in the alphabet".format(guess))

    else:
        print("sorry, you've run out of attempts. The correct letter was:", selected_letter)


guess_the_letter_game()
