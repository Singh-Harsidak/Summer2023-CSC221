from gasp import *

begin_graphics()

Circle((100,200),40)


for x in 85,115:
    Circle((x,210), 5)

Line((100,210),(90,190))

Line((90,190),(110,190))

Arc((100, 200), 30, 225, 315)


for x in range(75,100,5):
    Arc((x,215), 30, -225, -315)

Arc((60,200), 10, 90,270)
Arc((140,200), 10, -90, 100)


update_when('key_pressed') 
end_graphics()
