import random
from sense_hat import SenseHat
from time import sleep
#from berry import Berry
sense = SenseHat()


class Berry:
    def __init__(self, color, speed, value):
        self.color = color
        self.speed = .5
        self.position = random.randint(0,7)
        self.value = value
        self.pos_X = random.randint(0,7)
        self.pos_Y = 0

    def drop(self): 
        #if self.posy == 0 and self.posx == 0:
        sleep(self.speed)
        if self.pos_Y >= 0 and self.pos_Y < 7:
            self.pos_Y += 1
        self.display() 

    def display(self):
        x = self.pos_X
        y = self.pos_Y
        sense.set_pixel(x, (y-1), (0,7,0))
        sense.set_pixel(x, y, (200, 155, 255))
        print("berry moved")
             

        #if self.position <=55:
            #self.position += 8 
        #sleep(self.speed)
        #self.display()

    

    #def display(self):
        
       # x = self.position%8
        #y = self.position // 8
       # sense.set_pixel(x, y, self.color)

       # sense.set_pixel (x, y-1, (0,0,0))
        #sense.set_pixel(x, y, self.color)



        
