# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for char in secretWord:
        result += '_ ' if char not in lettersGuessed else char
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    available_letters = ''
    for char in abc:
        if char not in lettersGuessed:
            available_letters += char
    return available_letters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    bodyParts = 8
    mistakesMade = 0
    delimiter = '-----------'

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long'.format(str(len(secretWord))))
    print(delimiter)

    while mistakesMade < bodyParts:
        print('You have {} guesses left'.format(str(bodyParts - mistakesMade)))
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        guess = input('Please guess a letter: ').lower()

        if guess not in secretWord and guess not in lettersGuessed:
            mistakesMade += 1
            lettersGuessed += [guess]
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print('Oops! That letter is not in my word: ', guessedWord)
        else:
            if guess in lettersGuessed:
                guessedWord = getGuessedWord(secretWord, lettersGuessed)
                print('Oops! You’ve already guessed that letter: ', guessedWord)
            else:
                lettersGuessed += [guess]
                guessedWord = getGuessedWord(secretWord, lettersGuessed)
                print('Good guess: ', guessedWord)
                if isWordGuessed(secretWord, lettersGuessed):
                    print(delimiter)
                    print('Congratulations, you won!')
                    return None
        print('------------')
    print('Sorry, you ran out of guesses. The word was else.: {}'.format(secretWord))
    return None


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
