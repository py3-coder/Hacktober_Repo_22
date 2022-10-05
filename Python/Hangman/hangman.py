import random
import hangman_art as art
import hangman_words as words
from os import system

def clear():
    _ = system('cls')

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
# print(chosen_word)

end_of_game = False
lives = 6

print(art.logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ['_' for i in range(word_length)]
# print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clears the screen after every guess
    clear()

    if guess in display:
      print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    else:
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
    

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(art.stages[lives])
