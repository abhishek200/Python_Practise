
# Writes elements of a list into a File
# Author: Taranjeet Singh
# Date: 25 Nov 2021
def problem1(fileObject, sList):
    for item in sList:
        txt = item + "\n"
        fileObject.write(txt)

# Reads data from a file line by line and write it into another along with "name" and line number
# Author: Taranjeet Singh
# Date: 25 Nov 2021
def problem2(inFileObj, outFileObj):
    i = 0
    for line in inFileObj.readlines():
        i += 1
        txt = "name" + str(i) + line
        outFileObj.write(txt)

# Program to read from a file and adds the name ending with 'R' and 'N' into another file
# Author: Taranjeet Singh
# Date: 25 Nov 2021
def problem3 (inFileObj, outFileObj):
    for line in inFileObj.readlines():
        txt = line.strip()
        print(txt)
        if (txt[-1] == 'R' or txt[-1] == 'N'):
            outFileObj.write(txt)

# Testing Problem 1
# Opening myFavs.txt and myFavDrinks.txt
favAnimals = open("myFavs.txt", "w")
favDrinks = open("myFavDrinks.txt", "w")

Animals = ["Lion", "Tiger", "Cat", "Dog", "Bear"]
Drinks = ["Lemonade", "Lassi", "Smoothie", "Banana Shake"]

problem1(favAnimals, Animals)
problem1(favDrinks, Drinks)

# Closing the two files
favAnimals.close()
favDrinks.close()

# Testing Problem 2
# Opening boysNames.txt for input and namesWithLines.txt for output
bNames = open("boysNames.txt", "r")
namesWL = open("namesWithLines.txt", "w")

problem2(bNames, namesWL)

# closing the text files
namesWL.close()
bNames.close()

# TESTING for Problem3
# Opening the required files
namesWRN = open("namesWithRN.txt", "w")
inBName = open("boysNames.txt", "r")
problem3(inBName, namesWRN)

# closing the files
inBName.close()
namesWRN.close()