import random

# Predefined list of words for the game
word_list = ['python', 'hangman', 'programming', 'developer', 'technology', 'computer']

# Function to select a random word from the word_list
def get_random_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

# Hangman game function
def hangman():
    word = get_random_word()  # Get a random word
    guessed_letters = []  # List to store guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect = 6  # Maximum number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("You have to guess the word, one letter at a time.")
    print("You can make up to", max_incorrect, "incorrect guesses.")

    # Main game loop
    while incorrect_guesses < max_incorrect:
        current_display = display_word(word, guessed_letters)
        print("\nWord:", current_display)
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Get player's guess
        guess = input("Enter a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            incorrect_guesses += 1
            print("Incorrect guess!")

        # Check if the player has guessed the word
        if set(word) == set(guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

# Run the Hangman game
if __name__ == "__main__":
    hangman()