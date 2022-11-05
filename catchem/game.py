from sense_hat import SenseHat
from player import Player 
import time
import random
from berry import Berry

sense = SenseHat()

class Game:

    def __init__(self):
        self.score = 0
        self.game_over = False
        self.speed = .5
        self.berry = Berry(0,7,sense)
        self.player = Player(56, 63, sense)
        
    def start(self):
        sense.show_message("Catchem!", text_colour = (255,0,0), scroll_speed = 0.05)

    def play(self):
        self.start()
        #self.player.display(0)

        while not self.game_over:
            self.player.display(0)
            self.berry.drop()
            for event in sense.stick.get_events(): 
                if event.action == "pressed" and event.direction == "left":
                    self.player.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    self.player.move_right()

    #def make_berries(self):
        #b1 = Berry()
        #b1.name= "raspberry1"
       # b1.color = colors.d
       # b1.points = 10

        #b2 = Berry()
        #b2.name= "raspberry2"
        #b2.color = colors.d
        #b2.points = 10, 

        #b3 = Berry()
       # b3.name= "raspberry3"
        #b3.color = colors.d
        #b3.points = 10, 

        #b4 = Berry()
        #b4.name= "raspberry4"
        #b4.color = colors.d
        #b4.points = 10
        
        #berries = random.Berries(0,4)
        #berries.se
        

        
        
        #self.position(0,0)

        #if self.position:
            #return drop(self)
            #return display(self)
            #self.berries(display)

    #def new_berry(self):
        #return random.berries

    #for self.
        #self.berry.display(0)



    



