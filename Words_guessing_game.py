# WORDS GUESSING GAME
# User will be guessing the letters of words and will have total 6 wrong attempts
# If user guesses the words within 6 wrong attempts - he wins, if not - loses
# Words will be selected randomly from the list 
# User will be able to play again, and the words from the list will not repeat

import random
from IPython.display import clear_output

# LIST OF THE WORDS
Words_list = ['Dictionary','Python','Computer','Internet','Society','Entertainment','Building','Europe',
              'Program','Function','Keyboard','Table','Newspaper','Hospital','Fence','Money','Youtube',
              'Instagram','Facebook','Mouse','Webcam','Movie','Orange','Rainbow','Bottle','Watermellon']

# Function for selecting random word from the list and then remove that word from the list
def random_word_func(list1):
    random_word = random.choice(list1)
    list1.pop(list1.index(random_word))
    return random_word

# Function to display available letters for guessing letters
def random_letters_func(rand_word, user_letter):
    new_word = ""
    duplicate = 0
    for letter in rand_word:
        if user_letter.lower() != letter.lower():
            new_word += letter 
        else: 
            duplicate += 1
            if duplicate > 1:
                new_word += letter
    return new_word

# Setting game_on status - True
game_on = True

# Starting actual gameplay
while game_on:
    
    #Picking random word from the list by calling function
    user_rand_word = random_word_func(Words_list)
    #Defining first variables for the gameplay
    guessing_word = ''
    random_letters = ''.join(random.sample(user_rand_word.lower(),len(user_rand_word)))
    attempts = 6
    guessed_letters = 0
    user_choice = ""
    #Iterting through all letters of the word
    for letter in user_rand_word:
        #While user input is not equal to letter of the word - run this program
        while user_choice.lower() != letter.lower():
            #breaking out of the while and for loops if used all guessing attempts
            if attempts == 0:
                break
            #asking for user imput and displaying the random letters and guessed word symbols
            clear_output()
            print(f'Guessing word: {guessing_word+(len(user_rand_word)-guessed_letters)*"*"} \
            \nAvailable letters: {random_letters} \nNumber of available wrong attempts: {attempts} \n')
            user_choice = input('Please guess the letter of the word \n')
            if user_choice.lower() != letter.lower():
                attempts -= 1
        #Else - when user input equals letter then running this program
        else:
            guessing_word += letter
            guessed_letters +=1
            random_letters=random_letters_func(random_letters, letter)
            clear_output()
            print(f'Guessing word: {guessing_word+(len(user_rand_word)-guessed_letters)*"*"} \
            \nAvailable letters: {random_letters} \nNumber of available wrong attempts: {attempts} \n')
    # if user used all attemps then print it to the user
    if attempts == 0:
        clear_output()
        print("Sorry, you used all atempts")
    # if user guessed the word then print it to the user
    elif user_rand_word == guessing_word:
        print('Congratulations! You had succesfully guessed the word! \n')   
    # asking user if want to reapeat the games, if no - break the while loop
    repeat_game = input('Do you want to play again? YES / NO \n')
    if repeat_game[0].lower() != 'y':
        game_on = False
    
