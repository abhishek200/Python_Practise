# Date: November 2, 2021


# Problem 2:
# Program to perform sequencial search
# returns index if match is found
# returns -1 if match is not found
def sequentialSearch(theList, target):
    index = 0
    while index < len(theList):
        if theList[index] == target:
            return index
        else: 
            index = index + 1
    return -1


# Problem 3:
# Program to perform binary search
# returns index if match is found
# returns -1 if match is not found
def binaryAdvancedSearch(theList, target):
    startIndex = 0
    endIndex = len(theList) - 1
    while startIndex <= endIndex:
        middleIndex = (startIndex + endIndex)//2
        if target == theList[middleIndex]:
            return middleIndex
        elif target > theList[middleIndex]:
            startIndex = middleIndex + 1
        else:
            endIndex = middleIndex - 1
    return -1

# testing program for problem1
L1 = [0,3,4,9,10,15,18,19,20]

i = binaryAdvancedSearch(L1, 10)
print("Search Result for the problem 3 is: ")
print(i)

