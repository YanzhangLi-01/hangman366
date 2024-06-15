secret_word = ["apple", "strawberry", "cherry", "grape", "banana"]

def check_guess(guess):
    guess = guess.lower()
    if any(guess in word for word in secret_word):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    while True:
            guess = input("Please guess a letter among alphabet: ")
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()