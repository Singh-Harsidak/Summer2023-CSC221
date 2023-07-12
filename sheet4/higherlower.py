from random import randint
x = randint(1, 1000)     
print("I've thought of a number between 1 and 1000")
estimates = 0 
while True:
    guess = int(input("Make a guess: "))
    if(guess>x):
        print("That's too high!")
        estimates +=1
    
    elif(guess<x):
        print("That's too low")
        estimates +=1

    else:
        end = f"Correct! You guessed {estimates} times"
        print(end)
        break 