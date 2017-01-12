import random
#desktop\main\school2017\caps\projects
random = random.randrange(1, 100)

print("I'm thinking of a number between 1 and 100...")
#print(random)

answer = int(input(">"))
correct = False

while correct == False:
    if answer == random:
        print("You got it!")
        break
    elif answer < random:
        print("A little low")
        answer = int(input(">"))
    elif answer > random:
        print("A bit too high")
        answer = int(input(">"))

#No exception handling yet. Yes this is currently extrememly easy
#to break.
