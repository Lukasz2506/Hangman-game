#100 Days of code course, Angela Yu
#Student: Łukasz Świątek Brzeziński
# own workshop included
# Hangman Game



logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

import random
from word_list import word_list

stages = ['''
 +---+
 |   |
 O   |
     |
     |
     |
 =========''' ,
'''          
 +---+
 |   |
 O   |
 |   |
     |
     |
 =========''' ,
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
 =========''' ,
 '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
 =========''',
 '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
 =========''' ,         
'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
 ========='''   
]


chosen_word = random.choice(word_list)
#print("Psss, the guess word is %s"%(chosen_word))


display = []



for letter in chosen_word:
    display.append("_")

print(display)


print("\n")

end_of_game = False
is_letter = 0
stage_no = 0

while not end_of_game:

    guess = input("Choose the letter from the word: ").lower()
    if guess in display:
        print("you already choose this letter. Try again :)")


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            is_letter += 1
    print(display)
    
    if is_letter == 0:
        print(f"\nThere is no letter \"{guess}\" in this word. you lose one life.")
        print(stages[stage_no])
        stage_no += 1
    
    if "_" not in display:
        end_of_game = True
        print("You win!!!")
    elif stage_no == 6:
        print("You lose!!!, Game Over!!!")
        end_of_game = True
    is_letter = 0


#-------------------------------SECOND WAY to make for loop--------------------------
##n = 0
##for letter in chosen_word:
##    if letter == guess:
##        print("RIGHT")
##        #display.insert(chosen_word.index(letter),letter)
##        display[n] = letter
##    else:
##        print("WRONG")
##    n += 1
##n = 0
#print(display)



