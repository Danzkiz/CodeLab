
import random


def roll_die(sides: int):
    x = random.randint(1, sides)
    print("Alea iacta est, d"+str(sides)+": "+str(x))
    return x


def roll_dice(x, y):
    first = roll_die(x)
    second = roll_die(y)
    return first+second


print("How many dice should I roll?")
dice_number = int(input())

list = []
for i in range(dice_number):
    print("What die is number "+str(i+1)+"?")
    list.append(int(input()))
y=0
for i in list:
    x = roll_die(i)
    y += x
    #print("Die d"+str(i)+" got a: "+str(x))


print("total is: "+str(y))

#for i in range(dice_number):
#    print("Which die should I roll?")
#    sides = int(input())
#    roll_die(sides)
