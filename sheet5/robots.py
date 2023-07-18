from gasp import *          # So that you can draw things
from random import randint
from time import sleep
begin_graphics()            # Create a graphics window
finished = False
player_x = random.randint(0,63)
player_y = random.randint(0,47)
robot_x = random.randint(0,63)
robot_y = random.randint(0,47)

def place_player():
    global player_shape
    player_shape = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)


def move_player():
    global player_x, player_y
    key = update_when('key_pressed')
    if key == '1':
        if player_x >0:
            player_x -=1 
        if player_y >0:
            player_y -=1
    elif key == '2' and player_y>0:
        player_y -=1 
    elif key == '3':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1
    elif key == '4' and player_x>0:
        player_x -=1

    elif key == '6' and player_x < 63:
        player_x += 1
    
    elif key == '7':
        if player_x >0 :
            player_x -= 1
        if player_y < 47:
            player_y += 1
    
    elif key == '8' and player_y < 47:
        player_y += 1
    
    elif key == '9':
        if player_x < 63:
            player_x += 1
        if player_y < 47:
            player_y += 1

    
    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))

def place_robot():
    global robot_shape
    robot_shape = Box((10 * robot_x + 3, 10 * robot_y + 3), 10,10)

def move_robot():
    global robot_x, robot_y, player_x, player_y
    if robot_x < player_x:
        robot_x += 1
    elif robot_x > player_x:
        robot_x -= 1

    if robot_y < player_y:
        robot_y += 1
    elif robot_y > player_y:
        robot_y -= 1

    move_to(robot_shape, (10 * robot_x + 3, 10 * robot_y + 3))

def check_collision():
    global finished
    if player_x == robot_x and player_y == robot_y:
        finished = True
        message = Text("You've been caught!", (200, 200), size=30)
        sleep(3)  
        remove_from_screen(message)

place_robot()
place_player()

while not finished:
    move_player()
    move_robot()
    check_collision()

end_graphics()              # Finished!