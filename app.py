import random

secret_list = []
user_list = []


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

    # Creates a hidden list to compare to user's list.
    for letter in secret_word:
        if letter == letters_guessed:
            user_list.append(letter)
            secret_list.append(letter)
            print(letter)

        else:
            print("_")

    return


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
        is_guess_in_word == True
    else:
        print(f"{guess} is incorrect! Try again!")
        is_guess_in_word == False
    pass


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    running = True
    while running:
        print(secret_word)
        guess = input("Guess a letter for our Spaceman")
        get_guessed_word(secret_word, guess)
        is_guess_in_word(guess, secret_word)
    # TODO: show the player information about the game according to the project spec

    # TODO: Ask the player to guess one letter per round and check that it is only one letter

    # TODO: check if the game has been won or lost


def test():
    guess = "e"
    secret_word = load_word()
    print(secret_word)
    get_guessed_word(secret_word, guess)
    is_guess_in_word(guess, secret_word)


# test()
spaceman(load_word())
