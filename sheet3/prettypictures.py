from gasp import *

begin_graphics()

Circle((100,200),40)


for x in 85,115:
    Circle((x,210), 5)

Line((100,210),(90,190))

Line((90,190),(110,190))

Arc((100, 200), 30, 225, 315)



update_when('key_pressed') 
end_graphics()
