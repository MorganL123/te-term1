from sense_hat import SenseHat
sense = SenseHat()
pixel_list = sense.get_pixels()
from time import sleep


r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)
z = (50, 50, 50)

#rmon4 = [w, w, w, w, w, w, w, w,
         #w, w, d, d, w, d, w, w,             
        # w, d, d, d, d, d, d, w,
        # w, d, d, d, d, d, d, w,
        # w, d, d, d, d, d, d, w,
        # w, w, d, d, d, d, w, w,
        # w, w, w, d, d, w, w, w,
        # w, w, w, w, w, w, w, w]

rmon3 = [w, w, w, w, w, w, w, w,
         w, w, d, d, w, d, w, w,             
         w, d, d, d, d, d, d, w,
         w, d, d, d, d, d, d, w,
         w, d, d, d, d, d, d, w,
         w, w, d, d, d, d, w, w,
         w, w, w, d, d, w, w, w,
         w, w, w, w, w, w, w, w]

rmon4 = [w, w, w, w, w, w, w, w,
         r, r, d, d, w, w, w, w,             
         o, r, n, n, g, w, w, g,
         y, o, n, g, g, g, g, g,
         g, y, n, g, k, g, k, g,
         b, g, n, g, g, g, g, g,
         w, b, w, w, g, g, g, w,
         w, w, w, w, w, w, w, w]


sense.set_pixels(rmon4)
sleep(1)
sense.clear()

sense.set_pixels(rmon3)
sleep(1)


#drawing = ''
#drawing = input("What drawing would you like to see next?")
#if drawing == ['heart']:
    #sense.set_pixels(rmon3)
    #sleep(1)


		
		
		
		
		
		
		
		
		
		
		