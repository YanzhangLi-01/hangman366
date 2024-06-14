while True:
    guess = input("Please guess a letter among alphabet: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

print("You guess: ", guess)
