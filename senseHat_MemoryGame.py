from sense_hat import SenseHat
import csv
import time
import random

sense = SenseHat()
sense.clear()

#Variables for RGB values for LED display

a = (0,0,0)
b = (255,255,255)
r = (255,0,0)
g = (0,255,0)

#Variables for the game. The two "extra" lists are used to populate the remaining spots
#of the options from which the player will guess the right choice.

char_meaning = None
char_pronounce = None
file_contents = []
extra_meaning = ['sugar','milk','tea','coffee','water','I','love','one','two','three','four','five']
extra_pronunciation = ['ng5','sei3','ji6','jat1','siu2','do1','luk6','tong4','bui1','ngo5','oi3']
game_meaning_list = []
game_pronunciation_list =[]
points_counter = 0
row_counter = 0
max_rows = 0


#read_data will load the data needed to render the characters and
#pass their correct meaning/pronunciation to the right variables. It also determines
#how many rows are in the file to ensure that the game does not try to request more data than is there.

def read_data():

    global max_rows
    global file_contents
    try:
        with open('cantonese_characters.txt') as csv_file:
            csv_reader = csv.reader(csv_file)
            file_contents = list(csv_reader)
            max_rows = len(file_contents)
            
    except:
        sense.show_message("Issue reading from file. Make sure the file exists then restart the game.")
                
  
#load_character takes in two values: row_counter (which keeps track of the row the game is on), and file_contents
#(which is the contents of the read file saved to a list). row_counter is used as the index value to obtain the right row from
#the list. It then pops off the last two values of the list which should be the meaning/pronunciation. Then it converts the
#remaining String values to variable names (otherwise it won't display properly)

def load_character(row_counter, file_contents):
    
    global char_meaning
    global char_pronounce
    try:
        file_row = file_contents[row_counter]
        display_char = []
        char_pronounce = file_row.pop(65)
        char_meaning = file_row.pop(64)
        for item in file_row:
            if item == 'a':
                display_char.append(a)
            if item =='b':
                display_char.append(b)
        sense.set_pixels(display_char)
        time.sleep(3)
        sense.clear()
        
    except:
        sense.show_message("Check the contents of the supporting file. Data formatting may not be correct.")

#create_meaning_list generates a list of 4 elements. It initially populates it with four incorrect answers
#using extra_meaningand then overrides an element at a random index with the correct answer.

def create_meaning_list():
    global game_meaning_list
    global char_meaning
    game_meaning_list = []
    
    while len(game_meaning_list) < 4:
        holding_variable = random.choice(extra_meaning)
        if holding_variable != char_meaning and holding_variable not in game_meaning_list:
            game_meaning_list.append(holding_variable)
   
    game_meaning_list[random.randrange(4)] = char_meaning 
   
    
#create_pronunciation_list generates a list of 4 elements. It initially populates it with four incorrect answers
#using extra_pronunciation and then overrides an element at a random index with the correct answer.
    
def create_pronunciation_list():
    global game_pronunciation_list
    global char_pronounce
    
    game_pronunciation_list = []
    while len(game_pronunciation_list) < 4:
        holding_variable = random.choice(extra_pronunciation)
        if holding_variable != char_pronounce and holding_variable not in game_pronunciation_list:
            game_pronunciation_list.append(holding_variable)

            
    game_pronunciation_list[random.randrange(4)] = char_pronounce 
    

#pronunciation_game runs the pronunciation game mode where the player attempts to guess the correct
#pronunciations of loaded characters. After each attempt it will increment the row_counter to render
#the next character. Due to max_rows the game will stop when each character has been tested. 
    
def pronunciation_game():
    global points_counter
    global row_counter
    read_data()
    for x in range(0, max_rows):
        load_character(row_counter, file_contents)
        create_pronunciation_list()
        for i in game_pronunciation_list:
            sense.show_message(i)
        sense.show_message("Pick!", scroll_speed=0.05)
        event_occured = False
        while event_occured == False:
           for event in sense.stick.get_events():
                if event.action == "pressed":
                    if pronunciation_outcome(event.direction) == True:
                        sense.show_message("Right", text_colour=(g), back_colour=(a), scroll_speed=0.05)
                        points_counter = points_counter + 1
                        row_counter = row_counter + 1
                        event_occured = True
                    else:
                        sense.show_message("Wrong", text_colour=(r), back_colour=(a), scroll_speed=0.05)
                        row_counter = row_counter + 1
                        event_occured = True
                        
                        
#meaning_game runs the pronunciation game mode where the player attempts to guess the correct
#meanings of loaded characters. After each attempt it will increment the row_counter to render
#the next character. Due to max_rows the game will stop when each character has been tested.
                        
def meaning_game():
    global points_counter
    global row_counter
    read_data()
    for x in range(0, max_rows):
        load_character(row_counter, file_contents)
        create_meaning_list()
        for i in game_meaning_list:
            sense.show_message(i)
        sense.show_message("Pick!", scroll_speed=0.05)
        event_occured = False
        while event_occured == False:
            for event in sense.stick.get_events():
                if event.action == "pressed":
                    if meaning_outcome(event.direction) == True:
                        sense.show_message("Right", text_colour=(g), back_colour=(a), scroll_speed=0.05)
                        points_counter = points_counter + 1
                        row_counter = row_counter + 1
                        event_occured = True
                    else:
                        sense.show_message("Wrong", text_colour=(r), back_colour=(a), scroll_speed=0.05)
                        row_counter = row_counter + 1
                        event_occured = True
                        
                        
#pronunciation_outcome takes a String value representing a direction and then uses that to verify that it
#represented the correct answer. It does this by calling a further function input_Parser.

def pronunciation_outcome(direction):
    
    index = game_pronunciation_list.index(char_pronounce)
    if index == input_Parser(direction):
        return True
    else:
        return False
    
#meaning_outcome takes a String value representing a direction and then uses that to verify that it
#represented the correct answer. It does this by calling a further function input_Parser.
    
def meaning_outcome(direction):
    
    index = game_meaning_list.index(char_meaning)
    if index == input_Parser(direction):
        return True
    else:
        return False
 
#input_Parser converts a String value representing direction into a numerical value and returns it. That value represents
#an index value of a list. 
    
def input_Parser(input):
    if input == "left":
        return 0
        
    elif input == "up":
        return 1
        
    elif input == "right":
        return 2
        
    elif input == "down":
        return 3
        



    

#Sets up a Boolean value that will keep the game running until the player has played one of the game modes.Then starts the game.
    
game_over = False
sense.show_message("Cantonese Memory Game! Now pick a mode: Left for Pronunciation. Right for Meaning.", scroll_speed=0.05)

while game_over == False:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "left":
                sense.show_message("Pronunciation practice!", scroll_speed=0.05)
                pronunciation_game()
                sense.show_message("Your score: " + str(points_counter))
                game_over = True
            if event.direction == "right":
                sense.show_message("Meaning practice!", scroll_speed=0.05)
                meaning_game()
                sense.show_message("Your score: " + str(points_counter))
                game_over = True
            sense.clear()
