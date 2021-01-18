import random
import string
from words import word_list
print('Working!!!')

def choose_valid_word(word_list):
    word = random.choice(word_list)
    while ' ' in word or '-' in word:
        word = random.choice(word_list)
    return word.upper()
    
def hangman(word_list):
    word = choose_valid_word(word_list)
    alphabets = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters:", ' '.join(used_letters))
        print("You have", lives, "lives left.")
        print(' '.join([i + ' ' if i in used_letters else '- ' for i in word]))
        
        # print('- ' * len(word))
        player_letter = input('Guess a letter: ').upper()
        
        if player_letter in alphabets - used_letters:
            used_letters.add(player_letter)
            if player_letter in word_letters:
                word_letters.remove(player_letter)
            else:
                lives -= 1
                
        elif player_letter in used_letters:
            print("You've used this letter already\n")
        else:
            print("Please enter a valid character\n")
            
    if lives == 0:
        print("Sorry, You have no more lives (:, the word is", word + '.')
    else:       
        print('Wawoo! You guessed all the letters of the word!', word, ':)')
    
    
        
        



hangman(word_list)    

    