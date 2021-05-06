from sense_hat import SenseHat
import csv
import time
import random

sense = SenseHat()
sense.clear()

# Variables for RGB values for LED display

a = (0,0,0)
b = (255,255,255)
r = (255,0,0)
g = (0,255,0)

# Variables for the game. The two "extra" lists are used to populate the remaining spots
# of the options from which the player will guess the right choice.

charMeaning = None
charPronounce = None
fileContents = []
extraMeaning = ['sugar','milk','tea','coffee','water','I','love','one','two','three','four','five']
extraPronunciation = ['ng5','sei3','ji6','jat1','siu2','do1','luk6','tong4','bui1','ngo5','oi3']
gameMeaningList = []
gamePronunciationList =[]
pointsCounter = 0
rowCounter = 0
maxRows = 0


# read_data will load the data needed to render the characters and
# pass their correct meaning/pronunciation to the right variables. It also determines
#how many rows are in the file to ensure that the game does not try to request more data than is there.

def read_data():

    global maxRows
    global fileContents
    try:
        with open('cantonese_characters.txt') as csv_file:
            csv_reader = csv.reader(csv_file)
            fileContents = list(csv_reader)
            maxRows = len(fileContents)
            
    except:
        sense.show_message("Issue reading from file. Make sure the file exists and restart the game.")
                
  
# load_character takes in two values: row_counter (which keeps track of the row the game is on), and file_contents
# (which is the contents of the read file saved to a list). row_counter is used as the index value to obtain the right row from
# the list. It then pops off the last two values of the list which should be the meaning/pronunciation. Then it converts the
# remaining String values to variable names (otherwise it won't display properly)

def load_character(rowCounter, fileContents):
    
    global charMeaning
    global charPronounce
    try:
        fileRow = fileContents[rowCounter]
        displayChar = []
        charPronounce = fileRow.pop(65)
        charMeaning = fileRow.pop(64)
        for item in fileRow:
            if item == 'a':
                displayChar.append(a)
            if item =='b':
                displayChar.append(b)
        sense.set_pixels(displayChar)
        time.sleep(3)
        sense.clear()
        
    except:
        sense.show_message("Check the contents of the supporting file. Data formatting may not be correct.")

# create_meaning_list generates a list of 4 elements. It initially populates it with four incorrect answers
# using extra_meaningand then overrides an element at a random index with the correct answer.

def create_meaning_list():
    global gameMeaningList
    global charMeaning
    gameMeaningList = []
    
    while len(gameMeaningList) < 4:
        holdingVariable = random.choice(extraMeaning)
        if holdingVariable != charMeaning and holdingVariable not in gameMeaningList:
            gameMeaningList.append(holdingVariable)
   
    gameMeaningList[random.randrange(4)] = charMeaning 
   
    
# create_pronunciation_list generates a list of 4 elements. It initially populates it with four incorrect answers
# using extra_pronunciation and then overrides an element at a random index with the correct answer.
    
def create_pronunciation_list():
    global gamePronunciationList
    global charPronounce
    
    gamePronunciationList = []
    while len(gamePronunciationList) < 4:
        holdingVariable = random.choice(extraPronunciation)
        if holdingVariable != charPronounce and holdingVariable not in gamePronunciationList:
            gamePronunciationList.append(holdingVariable)

            
    gamePronunciationList[random.randrange(4)] = charPronounce 
    

# pronunciation_game runs the pronunciation game mode where the player attempts to guess the correct
# pronunciations of loaded characters. After each attempt it will increment the row_counter to render
# the next character. Due to max_rows the game will stop when each character has been tested. 
    
def pronunciation_game():
    global pointsCounter
    global rowCounter
    read_data()
    for x in range(0, maxRows):
        load_character(rowCounter, fileContents)
        create_pronunciation_list()
        for i in gamePronunciationList:
            sense.show_message(i)
        sense.show_message("Pick!", scroll_speed=0.05)
        eventOccured = False
        while eventOccured == False:
           for event in sense.stick.get_events():
                if event.action == "pressed":
                    if pronunciation_outcome(event.direction) == True:
                        sense.show_message("Right", text_colour=(g), back_colour=(a), scroll_speed=0.05)
                        pointsCounter = pointsCounter + 1
                        rowCounter = rowCounter + 1
                        eventOccured = True
                    else:
                        sense.show_message("Wrong", text_colour=(r), back_colour=(a), scroll_speed=0.05)
                        rowCounter = rowCounter + 1
                        eventOccured = True
                        
                        
# meaning_game runs the pronunciation game mode where the player attempts to guess the correct
# meanings of loaded characters. After each attempt it will increment the row_counter to render
# the next character. Due to max_rows the game will stop when each character has been tested.
                        
def meaning_game():
    global pointsCounter
    global rowCounter
    read_data()
    for x in range(0, maxRows):
        load_character(rowCounter, fileContents)
        create_meaning_list()
        for i in gameMeaningList:
            sense.show_message(i)
        sense.show_message("Pick!", scroll_speed=0.05)
        eventOccured = False
        while eventOccured == False:
            for event in sense.stick.get_events():
                if event.action == "pressed":
                    if meaning_outcome(event.direction) == True:
                        sense.show_message("Right", text_colour=(g), back_colour=(a), scroll_speed=0.05)
                        pointsCounter = pointsCounter + 1
                        rowCounter = rowCounter + 1
                        eventOccured = True
                    else:
                        sense.show_message("Wrong", text_colour=(r), back_colour=(a), scroll_speed=0.05)
                        rowCounter = rowCounter + 1
                        eventOccured = True
                        
                        
# pronunciation_outcome takes a String value representing a direction and then uses that to verify that it
# represented the correct answer. It does this by calling a further function input_Parser.

def pronunciation_outcome(direction):
    
    index = gamePronunciationList.index(charPronounce)
    if index == input_Parser(direction):
        return True
    else:
        return False
    
# meaning_outcome takes a String value representing a direction and then uses that to verify that it
# represented the correct answer. It does this by calling a further function input_Parser.
    
def meaning_outcome(direction):
    
    index = gameMeaningList.index(charMeaning)
    if index == input_Parser(direction):
        return True
    else:
        return False
 
# input_Parser converts a String value representing direction into a numerical value and returns it. That value represents
# an index value of a list. 
    
def input_Parser(input):
    if input == "left":
        return 0
        
    elif input == "up":
        return 1
        
    elif input == "right":
        return 2
        
    elif input == "down":
        return 3
        



    

# Sets up a Boolean value that will keep the game running until the player has played one of the game modes.
    
gameOver = False
sense.show_message("Cantonese Memory Game! Now pick a mode: Left for Pronunciation. Right for Meaning.", scroll_speed=0.05)

while gameOver == False:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "left":
                sense.show_message("Pronunciation practice!", scroll_speed=0.05)
                pronunciation_game()
                sense.show_message("Your score: " + str(pointsCounter))
                gameOver = True
            if event.direction == "right":
                sense.show_message("Meaning practice!", scroll_speed=0.05)
                meaning_game()
                sense.show_message("Your score: " + str(pointsCounter))
                gameOver = True
            sense.clear()
