#Create a program that figures out how long you have been alive in terms of years and months.

age = int(input("How old are you?"))
months = age * 30
days = age * 365
minutes = age * 525600
seconds = age * 31536000

print("You are " + str(months) + " months old")
print("You are " + str(days) + " days old")
print("You are " + str(minutes) + " minutes old")
print("You are " + str(seconds) + " seconds old")