import random

rnd = random.randint(1,10)
count=0
print(rnd)
print("Guess a number")

while True:
    guess = int(input())
    if rnd == guess:
        print("Correct! The number was "+str(rnd))
        print("You used "+str(count)+"attempts")
        break
    else:
        print("WROOOOOONG!! guess again")
        count+=1