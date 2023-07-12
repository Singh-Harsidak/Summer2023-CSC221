from random import randint
x = randint(1, 1000)     
print("I've thought of a number between 1 and 1000")
guess = int(input("Make a guess: "))
if(guess==x):
    print("You guessed correct!")
else:
    print("Sorry, wrong guess")