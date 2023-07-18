from gasp import *          # So that you can draw things
from random import randint
begin_graphics()            # Create a graphics window
finished = False
player_x = random.randint(0,63)
player_y = random.randint(0,47)
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


place_player()

while not finished:
    move_player()

end_graphics()              # Finished!