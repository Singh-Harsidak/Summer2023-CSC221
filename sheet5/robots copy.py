from gasp import *
from random import randint
from time import sleep

class Player:
    pass

class Robot:
    pass

finished = False 
numbots = 10
robots = []  
junk = []  # Create an empty list to store junk (dead robots)

player_x = randint(0, 63)
player_y = randint(0, 47)

def collided(thing1, list_of_things):
    for thing2 in list_of_things:
        if thing1.x == thing2.x and thing1.y == thing2.y:
            return True
    return False

def safely_place_player():
    global player

    player = Player()
    player.x = randint(0, 63)
    player.y = randint(0, 47)

    while collided(player, robots + junk):  
        player.x = randint(0, 63)
        player.y = randint(0, 47)

    player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

def robot_crashed(the_bot):
    for a_bot in robots:
        if a_bot == the_bot:    # we have reached our self in the list
            return False
        if a_bot.x == the_bot.x and a_bot.y == the_bot.y:  # a crash
            return a_bot
    return False

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
    else:
        player_x = player_x +0 
        player_y = player_y +0

    player_x, player_y = player.x, player.y
    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))

def place_robots():
    global robots

    robots = []

    while len(robots) < numbots:
        robot = Robot()
        robot.x = randint(0, 63)
        robot.y = randint(0, 47)
        if not collided(robot, robots):
            robot.shape = Box((10 * robot.x, 10 * robot.y), 10, 10)
            robots.append(robot)

def move_robots():
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

def check_collisions():
    global finished, robots, junk, score, score_text

    # Handle player crashes into robot
    if collided(player, robots + junk):
        finished = True
        Text("You've been caught!",(320, 240), size=36)
        sleep(3)
        return

    # Handle robot crashes
    surviving_robots = []
    for robot in robots:
        # Check if the robot has hit a piece of junk and discard it
        if collided(robot, junk):
            continue

        # Check if the robot has crashed with another robot
        jbot = robot_crashed(robot)

        if not jbot:
            # Append the robot to surviving_robots
            surviving_robots.append(robot)
        else:
            # Remove the robot shape from the screen
            remove_from_screen(robot.shape)

            if jbot in robots:
                # Remove the other crashed robot shape from the screen
                remove_from_screen(jbot.shape)
                # Change the other crashed robot into junk and append it to the junk list
                jbot.shape = Box((10 * jbot.x, 10 * jbot.y), 10, 10, filled=True, color=color.YELLOW)
                junk.append(jbot)

                # Change the current robot into junk and append it to the junk list
                robot.shape = Box((10 * robot.x, 10 * robot.y), 10, 10, filled=True, color=color.YELLOW)
                junk.append(robot)

                # Increment the score by 2 for each robot that becomes junk
                score += 2
                remove_from_screen(score_text)
                score_text = Text(f"Score: {score}", (50, 450), size=10)

    # Update the robots list with the surviving robots
    robots = surviving_robots

    # Check if robots is empty (if not robots)
    if not robots:
        finished = True
        Text("You win!", (320, 240), size=36)
        sleep(3)
        return

begin_graphics(640,480)
place_robots()
safely_place_player()

score = 0
score_text = Text("Score: 0", (50, 450), size=10)
while not finished:
    move_player()
    move_robots()
    check_collisions()

end_graphics()
