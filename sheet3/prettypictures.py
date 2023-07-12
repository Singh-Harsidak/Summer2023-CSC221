from gasp import *

begin_graphics()


def drawFace(x,y):
    Circle((x,y),40, color="yellow", filled=True)



    Circle((x-15,y), 5, color="black", filled=True)
    Circle((x+15,y), 5, color="black", filled=True)

    Line((x,y+10),(x-10,y-10))

    Line((x-10,y-10),(x+10,y-10))

    Arc((x,y), 30, 225, 315, color="red", filled=True)


    Arc((x-40,y), 10, 90,270)
    Arc((x+40,y), 10, -90, 100)

drawFace(300,200)
update_when('key_pressed') 
end_graphics()
