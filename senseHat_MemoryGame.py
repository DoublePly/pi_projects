from sense_hat import SenseHat
import csv
import time
import random

sense = SenseHat()
sense.clear()

#Variables for display colours

a = (255,10,10)
b = (10,10,255)
r = (255,0,0)
u = (0,0,0)
g = (0,255,0)



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
            print (display_char)
            print (len(display_char))
            sense.set_pixels(display_char)
            time.sleep(3)
            sense.clear()
            print (char_meaning)

# The function that sets up the list of meanings to be used by the game.

def create_meaning_list():
    global game_meaning_list
    #Populates the list with four values that aren't the answer
    while len(game_meaning_list) < 4:
        holding_variable = random.choice(extra_meaning)
        if holding_variable != char_meaning:
            game_meaning_list.append(holding_variable)
    #Changes one element at random to the answer
    game_meaning_list[random.randrange(4)] = char_meaning 
    print (game_meaning_list)
    
# The function that sets up the list of pronunciations to be used by the game.
    
def create_pronunciation_list():
    global game_pronunciation_list
    
    #Populates the list with four values that aren't the answer
    
    while len(game_pronunciation_list) < 4:
        holding_variable = random.choice(extra_pronunciation)
        if holding_variable != char_meaning:
            game_pronunciation_list.append(holding_variable)
            
    #Changes one element at random to the answer
            
    game_pronunciation_list[random.randrange(4)] = char_pronounce 
    print (game_pronunciation_list)
    
def pronunciation_game():
    load_character()
    create_pronunciation_list()
    
    for i in game_pronunciation_list:
        sense.show_message(i)
    sense.show_message("Pick the correct answer!")
    minigame_over = False
    while minigame_over == False:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if pronunciation_outcome(event.direction) == True:
                    sense.show_message("Right", text_colour=(g), back_colour=(u))
                    minigame_over = True
                else:
                    sense.show_message("Wrong", text_colour=(r), back_colour=(u))
    

def meaning_game():
    load_character()
    create_meaning_list()
    for i in game_meaning_list:
        sense.show_message(i)
    sense.show_message("Pick the correct answer!")
    minigame_over = False
    while minigame_over == False:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                
                if meaning_outcome(event.direction) == True:
                    sense.show_message("Right",text_colour=(g), back_colour=(u))
                    minigame_over = True
                else:
                    sense.show_message("Wrong", text_colour=(r), back_colour=(u))

def pronunciation_outcome(direction):
    
    #Get the index of the correct answer.
    
    index = game_pronunciation_list.index(char_pronounce)
    print(index)
    if index == input_Parser(direction):
        return True
    else:
        return False
    

def meaning_outcome(direction):
    
    #Get the index of the correct answer.
    
    index = game_meaning_list.index(char_meaning)
    print(index)
    if index == input_Parser(direction):
        return True
    else:
        return False
 
    
def input_Parser(input):
    if input == "left":
        return 0
        
    elif input == "up":
        return 1
        
    elif input == "right":
        return 2
        
    elif input == "down":
        return 3
        
game_over = False





while game_over == False:
    
    #sense.show_message("Pick a Game Mode")
    
    for event in sense.stick.get_events():
        if event.action == "pressed":
            
            #Check Direction
            
            if event.direction == "left":
                sense.show_message("Pronunciation practice!")
                pronunciation_game()
            if event.direction == "right":
                sense.show_message("Meaning practice!")
                meaning_game()
                
            
            sense.clear()
        

