import random

class hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word)
        self.word_guessed = ["_" for _ in word_list]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
    
    def ask_for_input(self):
        while True:
            guess = input("Please enter your guess: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guess:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                guess.append(self.list_of_guess)

    