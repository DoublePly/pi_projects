from sense_hat import SenseHat
import csv
import time
import random

sense = SenseHat()
sense.clear()


a = (255,10,10)
b = (10,10,255)



char_meaning = None
char_pronounce = None
display_char =[]
extra_meaning = ['sugar','milk','tea','coffee','water','I','love','one','two','three','four','five']
extra_pronunciation = ['ng5','sei3','ji6','jat1','siu2','do1','luk6','tong4','bui1','ngo5','oi3']
game_meaning_list = []
game_pronunciation_list =[]

# The following function loads a character, its meaning, and pronunciation from the CSV file.

def load_character():
    global display_char
    global char_meaning
    global char_pronounce
    with open('cantonese_characters.txt') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_file:
            hold_list = row.split(",")
            for item in hold_list:
                if item == 'a':
                    item = display_char.append(a)
                if item == 'b':
                    item = display_char.append(b)
            char_meaning = hold_list[64]
            char_pronounce = hold_list[65]
            
            # Testing that the values have been read correctly.
            print (display_char)
            print (len(display_char))
            sense.set_pixels(display_char)
            time.sleep(3)
            sense.clear()
            print (char_meaning)

# The function that sets up the list of meanings to be used by the game.

def create_meaning_list():
    global game_meaning_list
    game_meaning_list.append(char_meaning)
    while len(game_meaning_list) < 4:
        holding_variable = random.choice(extra_meaning)
        if holding_variable != char_meaning:
            game_meaning_list.append(holding_variable)
    print (game_meaning_list)
    
# The function that sets up the list of pronunciations to be used by the game.
    
def create_pronunciation_list():
    global game_pronunciation_list
    game_pronunciation_list.append(char_pronounce)
    while len(game_pronunciation_list) < 4:
        holding_variable = random.choice(extra_pronunciation)
        if holding_variable != char_meaning:
            game_pronunciation_list.append(holding_variable)
    print (game_pronunciation_list)

load_character()  
create_meaning_list()
create_pronunciation_list()
            
