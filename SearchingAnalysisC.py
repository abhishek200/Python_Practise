# Analyse Search Algorithms
# Date: Dec 6, 2021

def sequentialSearch(theList, item):
    #**** to be changed:
    # counts the iterations of the while loop and returns this value
    found = False
    count = 0
    index = 0
    while index < len(theList) and not found:
        count = count + 1
        if theList[index] == item:
            found = True
            print("Found at Index: " + str(index))
        index = index + 1    
    return count                    

def binarySearch(theList, item):
    #**** to be changed:
    # counts the iterations of the while loop and returns this value
    startIndex = 0
    endIndex = len(theList)- 1
    found = False
    count = 0
    while startIndex <= endIndex and not found:
        count = count + 1
        middleIndex = (startIndex + endIndex)//2
        if item == theList[middleIndex]:    # item found at middleIndex
            found = True
            print("Found at Index: " + str(middleIndex))
        elif item > theList[middleIndex]:   # item is in the upper half of theList
            startIndex = middleIndex + 1
        else:                               # item is in the lower half of theList
            endIndex = middleIndex - 1  
    return count     


# program for testing the search algorithms
dataSet = [-201, -191, -181, -171, -161, -111, -105, -74, -30, -17, -12, -1, 4, 5, 13, 26, 37, 42, 62, 96, 100, 110, 120,130]

# Step a
print("\nSuccessful sequential search - all elements of the data set")    
totalComparisons = 0
#**** to be completed:
#     list traversal on the dataSet list:
#     for each item: perform a sequential search and
#                    display (print) the item's value
#                                    and the number of comparisons,
#                    count the total number of comparisons
for data in dataSet:
    comparision = sequentialSearch(dataSet, data)
    print(data)
    print("No. of Comparisions required: " + str(comparision))
    totalComparisons = totalComparisons + comparision
print("Average number of comparisons: "+str(totalComparisons/len(dataSet)))


# Step b    
print("\nUn-successful sequential search")
target = 196                 # target not in the dataSet
comparisons = 0 
#**** to be changed: perform a sequential search for target
comparision = sequentialSearch(dataSet, target)
print ("target " + str(target), "\t comparisons used " + str(comparisons))


# Step c
print("\nSuccessful binary search - all elements of the data set")
totalComparisons = 0
#     for each item: perform a sequential search and
#                    display (print) the item's value
#                                    and the number of comparisons,
#                    count the total number of comparisons
for data in dataSet:
    comparision = binarySearch(dataSet,data)
    print(data)
    print("No. of Comparisions required: " + str(comparision))
    totalComparisons = totalComparisons + comparision
print("Average number of comparisons: "+str(totalComparisons/len(dataSet)))


# Step d
print("\nUn-successful binary search")
target = 196                 # target not in the dataSet
comparisons = 0 
#**** to be changed: perform a binary search for target
comparision = binarySearch(dataSet,target)
print ("target " + str(target), "\t comparisons used " + str(comparisons))

