import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7gg

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Cê tem', lives, 'vidas e já usou essas letras: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Palavra atual: ', ' '.join(word_list))

        user_letter = input('Fala uma letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nA letra,', user_letter, 'não ta na palavra.')

        elif user_letter in used_letters:
            print('\nJá foi. Vai outra.')

        else:
            print('\nIsso é uma letra inválida, querida.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Caiu fedendo. Passou longe. A palavra era: ', word)
    else:
        print('Razô ein! Acertou tudo', word, '!! ')


if __name__ == '__main__':
    hangman()