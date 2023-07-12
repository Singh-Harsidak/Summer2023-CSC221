from gasp import *

begin_graphics()


def drawFace(x,y,size):
    Circle((x,y), size*2)



    Circle((x-(size//4),y+size//4), size//4)
    Circle((x+15,y), size//4)

    Line((x,y+10),(x-10,y-10))

    Line((x-10,y-10),(x+10,y-10))

    Arc((x,y), 30, 225, 315)


    Arc((x-40,y), 10, 90,270)
    Arc((x+40,y), 10, -90, 100)

drawFace(300,20,40)
update_when('key_pressed') 
end_graphics()
