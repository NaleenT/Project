import time

#Multiplies a number to the power of another number
#An if, elif and else statement,
#A while loop, 
X = 15
counter = X
if X == 20:
    Mul = X ** 2
    print("Here's the answer " + str(Mul))
elif X == 10:
    Sub = X - 4
    print("Here's the answer " + str(Sub))
else:
    while counter != 0:
        print("Here's the answer " + str(counter))
        counter -= 1
        time.sleep(.5)

#A for loop,
#A dictionary.
Count = 0
dictionary = {"Heater":"Fan", "AC":"Fan", "Window":"Manual"}
for Fan in dictionary:
    if dictionary[Fan] == "Fan":
        Count += 1
print("There are " + str(Count) + " fans")