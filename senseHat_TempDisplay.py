from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

# Sets up the variables used to display colours to the LED Matrix. Each variable is a tuple representing an RGB value. So Black, Red, Orange, and Yellow in 
# that order.

b = (0,0,0)
r = (255,0,0)
o = (255,153,51)
y = (255,255,51)

# Sets up the variable that will be used to store the temperature readings. 

currentTemp = 0

# Sets up the first display on the LED Matrix. Which in this case is a full Black background.

display = [ b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
    ]
# These variables are lists of values that represent the indexes of each position in a typical 64 element list used to set the 8x8 LED Matrix. They've been
# ordered into columns from left to right so as to correctly alter the display and adjust it as the temperature reading gets updated.

columnOne =   [0,8,16,24,32,40,48,56]
columnTwo =   [1,9,17,25,33,41,49,57]
columnThree = [2,10,18,26,34,42,50,58]
columnFour =  [3,11,19,27,35,43,51,59]
columnFive =  [4,12,20,28,36,44,52,60]
columnSix =   [5,13,21,29,37,45,53,61]
columnSeven = [6,14,22,30,38,46,54,62]
columnEight = [7,15,23,31,39,47,55,63]
 
            
# Sets up the initial display for the LED Matrix.
            
sense.set_pixels(display)

# A function to obtain the current temperature and convert the returned float value into an int value.

def get_Temp():
    global currentTemp
    currentTemp = int(sense.get_temperature_from_humidity())

# A function made to alter the display. Basically it uses the values stored in the column variables to iterate over the display
# list column by column, moving each current colour value over to the left by one (to give the appearance of a constant running line
# on the LED display. The first column is wiped completely as they've hit the edge of the screen.)
    
def alter_Display():
    global display
    
    displayCopy = display
    for item in columnOne:
        displayCopy[item] = b
    for item in columnTwo:
        if displayCopy[item] != b:
            i = displayCopy[item]
            displayCopy[item] = b
            displayCopy[item - 1] = i
    for item in columnThree:
        if displayCopy[item] != b:
            i = displayCopy[item]
            displayCopy[item] = b
            displayCopy[item - 1] = i
    for item in columnFour:
        if displayCopy[item] != b:
            i = displayCopy[item]
            displayCopy[item] = b
            displayCopy[item - 1] = i
    for item in columnFive:
        if displayCopy[item] != b:
            i = displayCopy[item]
            displayCopy[item] = b
            displayCopy[item - 1] = i
    for item in columnSix:
        if displayCopy[item] != b:
            i = displayCopy[item]
            displayCopy[item] = b
            displayCopy[item - 1] = i
    for item in columnSeven:
        if displayCopy[item] != b:
            i = displayCopy[item]
            displayCopy[item] = b
            displayCopy[item - 1] = i
    for item in columnEight:
        if displayCopy[item] != b:
            i = displayCopy[item]
            displayCopy[item] = b
            displayCopy[item - 1] = i
            
    display = displayCopy
    
# This iterates continuously, calling the two other functions. If the temperature is in a certain range it will add that colour to a specific position
# in the last column of the LED Matrix. After which it pauses very briefly before doing it all over again.

while True:
    time.sleep(0.2)
    get_Temp()
    if currentTemp < 5:
        display[55] = y
    elif currentTemp > 5 and currentTemp < 10:
        display[47] = y
    elif currentTemp > 10 and currentTemp < 15:
        display[39] = o
    elif currentTemp > 15 and currentTemp < 20:
        display[31] = o
    elif currentTemp > 20 and currentTemp < 25:
        display[23] = r
    elif currentTemp > 25:
        display[15] = r
    sense.set_pixels(display)
    alter_Display()
    
    
        
    
    
