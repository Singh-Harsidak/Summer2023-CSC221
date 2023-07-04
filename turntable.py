import random
counter = 0
for i in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = "What is {} into {}?".format(x,y)
    ans = int(input(z))
    if ans == (x*y):
        counter +=1

print("Your final score is", counter)

if counter>5:
    print("Good job!")
else:
    print("Try again!")

