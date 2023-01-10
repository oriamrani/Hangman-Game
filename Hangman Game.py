# Import fore from colorama so I can print in different colors.
from colorama import Fore

# A dictionary that consists of the 7 states of the hangman.
HANGMAN_PHOTOS = {
    1: "    x-------x",
    2: """    x-------x
    |
    |
    |
    |
    |""",
    3: """    x-------x
    |       |
    |       0
    |
    |
    |""",
    4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
    5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
    6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""",
}

def opening_screen():
    """This function prints the opening screen of the game in yellow"""
    HANGMAN_ASCII_ART = """Welcome to the 
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/       \n game! """

    MAX_TRIES = 6
    print(Fore.YELLOW + HANGMAN_ASCII_ART + "\n" + "\n" + Fore.RESET + "For your knowledge, the maximum number of failed attempts available for you is: "
          + str(MAX_TRIES) + "\n")


def print_hangman(num_of_tries):
    """This function returns the hangman state according to the number of failed attempts.
    :param num_of_tries: The number of failed attempts
    :type num_of_tries: int
    :return: The suitable image of the hangman (from the dictionary - HANGMAN_PHOTOS)
    :rtype: print
    """
    return HANGMAN_PHOTOS[num_of_tries]


def length_of_guessed_word(secret_word):
    """This function returns number of underlines as per as the length of the secret word.
    :param secret_word: The word should be guessed by the gamer.
    :type secret_word: string
    :return: Number of underlines
    :rtype: string (print)
    """
    return len(secret_word) * "_ "


def check_valid_input(letter_guessed, old_letters_guessed):
    """This function checks if the string which inserted by the gamer is valid, according to 3 criteria:
     1.Its length = 1,  2. It's a letter,  3. It wasn't guessed before.
    :param letter_guessed: One guessed string to be checked
    :param old_letters_guessed: A list that consists of the letters already been guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: A boolean value if the string is valid or not
    :rtype: boolean
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
            and not letter_guessed.lower() in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """This function checks the validation of the user’s input.
    If it’s valid - it adds it to the "old_letters_guessed" list and returns True.
    Otherwise, returns a message of 'X', a sorted list of the letters been guessed, and False.
    :param letter_guessed: One guessed string to be checked
    :param old_letters_guessed: A list that consists of the letters that already been guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: A boolean value (and other print - according to the situation)
    :rtype: boolean (and print)
    """
    separator = " -> "
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        x = sorted(old_letters_guessed, key=str.lower)
        print(separator.join(x))
        print("Please, insert a valid char!")
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    """This function returns a string consists of underlines and letters (in the right place at the string),
    so the gamer can know how much he advanced and which are the letters left to be guessed.
    :param secret_word: The word should be guessed by the gamer
    :param old_letters_guessed: A list that consists of the letters already been guessed
    :type secret_word: string
    :type old_letters_guessed: list
    :return: The letters been guessed alongside underlines - where the gamer didn't guess yet
    :rtype: string (print)
    """
    output = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            output = output + letter + ' '
        else:
            output = output + "_ "
    return output[:-1]


def check_win(secret_word, old_letters_guessed):
    """This function checks whether the gamer succeeded and guessed all needed letters.
    It returns True -  if all the letters in the secret word are in the list of the
    letters the gamer already has guessed, which means that the gamer won.
    :param secret_word: The word should be guessed by the gamer.
    :param old_letters_guessed: A list that consists of the letters already been guessed.
    :type secret_word: string
    :type old_letters_guessed: list
    :return: A boolean value if all the letters composing the secret word been guessed.
    :rtype: boolean
    """
    num = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            num = num + 1
    if num == len(secret_word):
        return True
    else:
        return False


def choose_word(file_path, index):
    """This function takes a path to a text file and retrieve the word that placed in the given index.
    :param file_path: path to the text file
    :param index: The index of the desirable word
    :type file_path: string
    :type index: int
    :return: The word in the desirable index
    :rtype: string
    """
    with open(file_path, 'r') as words:
        word_list = words.read().split(' ')
    i = (index - 1) % len(word_list)
    return word_list[i]


def main():
    #1 - Opening screen
    opening_screen()

    #2 - Choosing a word to guess
    path = input("Enter a path of file for taking a word: " + "\n")
    index = int(input("Enter an index: "))
    secret_word = choose_word(path, index)

    #3 - Displaying the initial state of the hangman
    print("\n" + "Your starting position is: " + "\n" + print_hangman(1) + "\n")

    #4 - Displaying the secret word as: "____"
    print("The letters you should guess are hiding here:  " + length_of_guessed_word(secret_word) + "\n")

    #5 - Asking the gamer to insert one char and try guess the secret word
    print("Now let's beat it!")
    old_letters_guessed = []
    MAX_TRIES = 6
    num_of_tries = 0

    #As long as num_of_tries haven't reached to MAX_TRIES (6 failed attempts), do the while loop
    while num_of_tries < MAX_TRIES:
        letter_guessed = input("\n" + "Guess a letter: ")
        #Checking validation of input
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            #if the input is in the secret word - it will be shown as part of the word next to another underlines
            if letter_guessed.lower() in secret_word:
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                #printing the state of hangman and letters that already been guessed, after failed attempt
                print("\n" + ":(" + "\n" + print_hangman(num_of_tries + 2))
                print("\n" + show_hidden_word(secret_word, old_letters_guessed))
                num_of_tries = num_of_tries + 1

        # checking winning the game or losing it.
        if check_win(secret_word, old_letters_guessed):
            print("\n" + Fore.BLUE + "WIN" + Fore.RESET)
            break

        if num_of_tries == MAX_TRIES:
            print("\n" + Fore.RED + "LOSE" + Fore.RESET)

if __name__ == "__main__":
    main()