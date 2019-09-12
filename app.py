import random


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    if letters_guessed == secret_word:
        secret_word = True
    else:
        secret_word = False
        pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    display = ''

    for letter in secret_word:
        if letter in letters_guessed:
            display += letter
        else:
            display += "_"
    return display


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    if guess in secret_word:
        print(f"{guess} is correct!")
        return True
    else:
        print(f"{guess} is incorrect! Try again!")
        return False
    pass


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    life = 7
    running = True
    while running == True:
        print(f"You have {life} guesses remaining")
        print(secret_word)
        print(get_guessed_word(secret_word, letters_guessed))
        guess = input("Guess a letter: ")
        letters_guessed.append(guess)
        if is_guess_in_word(guess, secret_word) is False:
            life -= 1
        if life == 0:
            print(f'Sorry, you lose. Your word was: {secret_word}')
            break


def test():
    get_guessed_word(secret_word, 'a')


# test()
secret_word = load_word()
spaceman(secret_word)
