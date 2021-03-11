from sense_hat import SenseHat
import random
import time

sense = SenseHat()

#Initializing colours for the dice displays

a = (0, 0, 0)
b = (0, 255, 0)

#Creating the individual displays for each side of the dice

one = [a,a,a,a,a,a,a,a,
       a,a,a,a,a,a,a,a,
       a,a,a,a,a,a,a,a,
       a,a,a,b,b,a,a,a,
       a,a,a,b,b,a,a,a,
       a,a,a,a,a,a,a,a,
       a,a,a,a,a,a,a,a,
       a,a,a,a,a,a,a,a,
       ]

two = [a,a,a,a,a,a,a,a,
       a,a,a,b,b,a,a,a,
       a,a,a,b,b,a,a,a,
       a,a,a,a,a,a,a,a,
       a,a,a,a,a,a,a,a,
       a,a,a,b,b,a,a,a,
       a,a,a,b,b,a,a,a,
       a,a,a,a,a,a,a,a,
       ]

three = [a,a,a,a,a,a,a,a,
         a,a,a,a,a,b,b,a,
         a,a,a,a,a,b,b,a,
         a,a,a,b,b,a,a,a,
         a,a,a,b,b,a,a,a,
         a,b,b,a,a,a,a,a,
         a,b,b,a,a,a,a,a,
         a,a,a,a,a,a,a,a,
       ]

four = [a,a,a,a,a,a,a,a,
        a,b,b,a,a,b,b,a,
        a,b,b,a,a,b,b,a,
        a,a,a,a,a,a,a,a,
        a,a,a,a,a,a,a,a,
        a,b,b,a,a,b,b,a,
        a,b,b,a,a,b,b,a,
        a,a,a,a,a,a,a,a,
       ]

five = [a,a,a,a,a,a,a,a,
        a,b,b,a,a,b,b,a,
        a,b,b,a,a,b,b,a,
        a,a,a,b,b,a,a,a,
        a,a,a,b,b,a,a,a,
        a,b,b,a,a,b,b,a,
        a,b,b,a,a,b,b,a,
        a,a,a,a,a,a,a,a,
       ]

six =  [a,b,b,a,a,b,b,a,
        a,b,b,a,a,b,b,a,
        a,a,a,a,a,a,a,a,
        a,b,b,a,a,b,b,a,
        a,b,b,a,a,b,b,a,
        a,a,a,a,a,a,a,a,
        a,b,b,a,a,b,b,a,
        a,b,b,a,a,b,b,a,
       ]

#Creating a list of dice displays with which they will be picked at random

dice_list = [one, two, three, four, five, six]

while True:
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
  
  #Use abs to get the absolute value
  
  x = abs(x)
  y = abs(y)
  z = abs(z)
  
  if x > 1.5 or y > 1.5 or z > 1.5:
    #set the dice display at random should the sense hat detect a certain level of movement. 
    
    sense.set_pixels(random.choice(dice_list))
    time.sleep(2)
  else:
    sense.clear()
