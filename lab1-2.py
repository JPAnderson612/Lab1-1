import string

camelize = ""
print("Enter a sequence of characters\n and I will try to camelize it")

toCamel = input(">")

#.split() I found online here: https://docs.python.org/3/library/stdtypes.html#str.split
#.capitalze() and .lower() I found online here: https://www.dotnetperls.com/lower-python
words = toCamel.split(" ")
#This loop goes through each word in the list and capitalzes the first letter of each one
#The first letter in the list is an exception and is forced lower with every run of the loop (perhaps a bit redundant)
for x in range(0, len(words)):
    words[x] = words[x].capitalize()
    words[0] = words[0].lower()
    camelize = camelize + words[x]
print(camelize)
