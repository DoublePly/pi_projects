from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()


b = (0,0,0)
r = (255,0,0)
o = (255,153,51)
y = (255,255,51)



currentTemp = 0

display = [ b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b,
    ]
columnOne =   [0,8,16,24,32,40,48,56]
columnTwo =   [1,9,17,25,33,41,49,57]
columnThree = [2,10,18,26,34,42,50,58]
columnFour =  [3,11,19,27,35,43,51,59]
columnFive =  [4,12,20,28,36,44,52,60]
columnSix =   [5,13,21,29,37,45,53,61]
columnSeven = [6,14,22,30,38,46,54,62]
columnEight = [7,15,23,31,39,47,55,63]
 
sense.set_pixels(display)


def getTemp():
    global currentTemp
    currentTemp = int(sense.get_temperature_from_humidity())


    
def alterDisplay():
    global display
    global columnOne
    global columnTwo
    global columnThree
    global columnFour
    global columnFive
    global columnSix
    global columnSeven
    global columnEight
    
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
    


while True:
    time.sleep(0.2)
    getTemp()
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
    alterDisplay()
    
    
        
    
    