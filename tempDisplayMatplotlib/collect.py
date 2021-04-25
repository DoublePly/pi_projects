from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


for x in range(20):
    sleep(2)
    myfile = open('weather.txt', 'a')
    myfile.write(str(sense.get_temperature()))
    myfile.write('\n')
    myfile.close()

    

    