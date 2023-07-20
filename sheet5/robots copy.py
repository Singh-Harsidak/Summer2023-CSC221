from gasp import *
from random import randint
from time import sleep

class Player:
    pass

class Robot:
    pass

begin_graphics()
finished = False 
numbots = 10
robots = []  # Create an empty list to store the robots

player_x = random.randint(0, 63)
player_y = random.randint(0, 47)

def collided():
    global player_x, player_y, robots

    for robot in robots:
        if player_x == robot.x and player_y == robot.y:
            return True

    return False

def safely_place_player():
    global player
    player = Player()
    player.x = random.randint(0, 63)
    player.y = random.randint(0, 47)

    while collided():
        player.x = random.randint(0, 63)
        player.y = random.randint(0, 47)

    player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

def move_player():
    global player, player_x, player_y

    while True:
        key = update_when('key_pressed')

        if key == '5':
            remove_from_screen(player.shape)
            safely_place_player()

        else:
            break

    if key == '1':
        if player.x > 0:
            player.x -= 1
        if player.y > 0:
            player.y -= 1
    elif key == '2' and player.y > 0:
        player.y -= 1
    elif key == '3':
        if player.x < 63:
            player.x += 1
        if player.y > 0:
            player.y -= 1
    elif key == '4' and player.x > 0:
        player.x -= 1
    elif key == '6' and player.x < 63:
        player.x += 1
    elif key == '7':
        if player.x > 0:
            player.x -= 1
        if player.y < 47:
            player.y += 1
    elif key == '8' and player.y < 47:
        player.y += 1
    elif key == '9':
        if player.x < 63:
            player.x += 1
        if player.y < 47:
            player.y += 1

    player_x, player_y = player.x, player.y
    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))

def place_robots():
    global robots

    for i in range(numbots):
        robot = Robot()  # Create a new Robot instance
        robot.x = random.randint(0, 63)
        robot.y = random.randint(0, 47)
        robot.shape = Box((10 * robot.x + 3, 10 * robot.y + 3), 10, 10)

        robots.append(robot)  # Add the robot to the list

def move_robot():
    global robots

    for robot in robots:
        if robot.x < player.x:
            robot.x += 1
        elif robot.x > player.x:
            robot.x -= 1

        if robot.y < player.y:
            robot.y += 1
        elif robot.y > player.y:
            robot.y -= 1

        move_to(robot.shape, (10 * robot.x + 3, 10 * robot.y + 3))

def check_collision():
    global finished

    for robot in robots:
        if robot.x == player.x and robot.y == player.y:
            finished = True
            message = Text("You've been caught!", (200, 200), size=30)
            sleep(3)
            remove_from_screen(message)

place_robots()
safely_place_player()

while not finished:
    move_player()
    move_robot()
    check_collision()

end_graphics()
