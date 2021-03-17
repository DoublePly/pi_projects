from sense_hat import SenseHat
import csv

sense = SenseHat()
sense.clear()


a = (255,10,10)
b = (10,10,255)



char_meaning = []
char_pronounce = []

with open('cantonese_characters.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    display_char =[]
    for row in csv_file:
        hold_list = row.split(",")
        for item in hold_list:
            if item == 'a':
                item = display_char.append(a)
            if item == 'b':
                item = display_char.append(b)
            
        print (display_char)
        print (len(display_char))
        sense.set_pixels(display_char)
            
