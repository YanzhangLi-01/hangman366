while True:
    guess = input("Please guess a letter among alphabet: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

print("You guess: ", guess)

secret_word = ["apple", "strawberry", "cherry", "grape", "banana"]
if guess in secret_word[0]:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again")