import random
from sense_hat import SenseHat
from time import sleep
from Berry import berries
sense = SenseHat()
class Berry:
    def __init__(self, color, speed, value)
    self.position(0,7)
    self.color = color
    self.speed = speed
    self.value = value

    def drop(self):
        if self.position <=55:
            self.position += 8 
        sleep(self.speed)
        self.display()

    

    def display(self):
        
        x = self.position%8
        y = self.position // 8
        sense.set_pixel(x, y, self.color)

        sense.set_pixel (x, y-1, (0,0,0))
        sense.set_pixel(x, y, self.color)



        
