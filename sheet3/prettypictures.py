from gasp import *

begin_graphics()

Circle((300,200),40)

for x in 285,315:
    Circle((x,210), 5)

Line((300,210),(290,190))

Line((290,190),(310,190))

Arc((300, 200), 30, 225, 315)



update_when('key_pressed') 
end_graphics()
