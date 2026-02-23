import random
import hangman_words
import hangman_art
# from hangman_words import word_list
# from hangman_art import stages, logo

lives = 6

print(hangman_art.logo)

stages = hangman_art.stages

random_word = random.choice(hangman_words.word_list) # returns an element from the list, in a string format
# for blank in random_word:
#     print("_", end=" ")
# temporarily printed, nothing stored to be updated later

# to store and update, have to use variable
blanks = ""

for position in random_word:
    blanks += "_"
print(blanks)

correct_letter = []

game_over = False
while not game_over:
    print(f"{lives}/6 lives left")
    user_guess = input("\nGuess a letter: ").lower()

    if user_guess in correct_letter:
        print(f"You already guessed {user_guess}")

    fill_blank = "" # so we can update and show what is filled and what is not filled
    for i in random_word: # since it's a string i can take each letter
        if user_guess == i:
            fill_blank += i
            # print(user_guess, end="")
            correct_letter.append(i)
        elif i in correct_letter:
            fill_blank += i
        else:
            fill_blank += "_"
            # print("_", end="") # better to use variable first and then check for clean code later
    print(fill_blank)

    if i not in random_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")

    if user_guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True

            print(f"\nGame Over. The correct word is {random_word}")

    if "_" not in fill_blank:
        game_over = True
        print("You win!")

    print(hangman_art.stages[lives])