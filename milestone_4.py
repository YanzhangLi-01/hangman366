import random

class hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word)
        self.word_guessed = ["_" for _ in word_list]
        self.num_letters = len(set(self.word))
        self.list_of_guesses: []


    