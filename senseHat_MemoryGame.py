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

extra_meaning = ['sugar','milk','tea','coffee','water','I','love','one','two','three','four','five']
extra_pronunciation = ['ng5','sei3','ji6','jat1','siu2','do1','luk6','tong4','bui1','ngo5','oi3']
game_meaning_list = []
game_pronunciation_list =[]
points_counter = 0
row_counter = 0
max_rows = 0
points_aim = 0

# The following function loads a character, its meaning, and pronunciation from the CSV file.

def load_character(row_number):
    
    global char_meaning
    global char_pronounce
    global max_rows
    with open('cantonese_characters.txt') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        max_rows = len(rows)
        print(rows)
        hold_list = rows[row_number]
        temp_display_char = hold_list
        print(temp_display_char)
        display_char = []
        char_pronounce = temp_display_char.pop(65)
        char_meaning = temp_display_char.pop(64)
        for item in temp_display_char:
            if item == 'a':
                display_char.append(a)
            if item =='b':
                display_char.append(b)
        #char_meaning = hold_list[64]
        #char_pronounce = hold_list[65]
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
    global points_counter
    global row_counter
    
    
    for x in range(0, 5):
        load_character(row_counter)
        create_pronunciation_list()
        for i in game_pronunciation_list:
            sense.show_message(i)
        sense.show_message("Pick!", scroll_speed=0.05)
        event_occured = False
        while event_occured == False:
            
            for event in sense.stick.get_events():
                if event.action == "pressed":
                    if pronunciation_outcome(event.direction) == True:
                        sense.show_message("Right", text_colour=(g), back_colour=(u), scroll_speed=0.05)
                        points_counter ++ 1
                        row_counter ++ 1
                        event_occured = True
                    else:
                        sense.show_message("Wrong", text_colour=(r), back_colour=(u), scroll_speed=0.05)
                        row_counter = ++ 1
                        event_occured = True

def meaning_game():
    global points_counter
    minigame_over = False
    while minigame_over == False:
        load_character()
        create_meaning_list()
        for i in game_meaning_list:
            sense.show_message(i)
        sense.show_message("Pick!", scroll_speed=0.05)
        event = sense.stick.wait_for_event()
        for event in sense.stick.get_events():
            if event.action == "pressed":
                
                if meaning_outcome(event.direction) == True:
                    sense.show_message("Right",text_colour=(g), back_colour=(u), scroll_speed=0.05)
                    minigame_over = True
                else:
                    sense.show_message("Wrong", text_colour=(r), back_colour=(u), scroll_speed=0.05)

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
        
        
def game_rules():
    sense.show_message("Cantonese Memory Game! To select answers use the joystick: Left,Up, Down, Right correspond to the order in which the choices are shown.Now pick a mode: Left for Pronunciation. Right for Meaning.", scroll_speed=0.05)


game_over = False
game_rules()

while game_over == False:
    points_counter
    for event in sense.stick.get_events():
        
        if event.action == "pressed":
            
            #Check Direction
            
            if event.direction == "left":
                sense.show_message("Pronunciation practice!", scroll_speed=0.05)
                pronunciation_game()
            if event.direction == "right":
                sense.show_message("Meaning practice!", scroll_speed=0.05)
                meaning_game()
                
            
            sense.clear()
        


