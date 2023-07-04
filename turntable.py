import random
counter = 0
for i in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    ans = int(input("What is", str(x), "into", str(y)))
    if ans == (x*y):
        counter +=1

        
