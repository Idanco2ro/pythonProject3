from clear import clear
import random
from hangman_words import word_list
from hangman_ASCII_ART import stages
from hangman_ASCII_ART import logo
from clear import clear

print(logo)

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

lives = 6
# letter = guess.isalpha()

# Create blanks
display = []
for _ in range(word_lenght):
    display += "_"
end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ").lower()
    clear()
    # if user entered a letter they have already guessed, print the letter and let them know
    if guess in display:
        print(f"You already guessed {guess}")

        # to make sure that user input just letters
    letter = guess.isalpha()

    # Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
