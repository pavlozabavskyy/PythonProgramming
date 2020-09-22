import random


def average(arr):
    return sum(arr) / len(arr)


def maxElemAverage(arr):
    s, i, maximum, j, index = average(arr), 0, arr[0], 0, 0

    while maximum > s:
        i += 1
        maximum = arr[i]

    for obj in arr:
        if obj > maximum and obj <= s:
            maximum = obj
            index = j
        j += 1

    print "Maximum number - ", maximum, " , with index -- ", index
    return index


def minElemAverage(arr):
    s, i, minimum, j, index = average(arr), 0, arr[0], 0, 0

    while minimum < s:
        i += 1
        minimum = arr[i]

    for obj in arr:
        if obj < minimum and obj >= s:
            minimum = obj
            index = j
        j += 1

    print "Average - ", s, ", minimum number - ", minimum, " , with index -- ", index
    return index


def sortElem(arr):
    newArray = []

    l, r = minElemAverage(arr), maxElemAverage(arr)

    if r < l:
        temp = l
        l = r
        r = temp

    for i in range(l + 1, r):
        newArray.append(arr[i])

    print "Elements in between (with reverse sort) - ", newArray

    newArray.sort(reverse=True)

    j = 0
    for i in range(l + 1, r):
        arr[i] = newArray[j]
        j += 1

    print "Result : ", arr
    return arr


def binarySearch(arr, number):
    arr.sort()
    idSearch, numOfOper = [], 0
    low , high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        numOfOper += 1

        print numOfOper, " middle index - ", mid

        if number < arr[mid]:
            high = mid - 1
        elif number > arr[mid]:
            low = mid + 1
        elif number == arr[mid]:
            idSearch.append(mid)
            break
    else:
        print "No number"

    if idSearch[0] != len(arr) - 1:
        i = 1
        while number == arr[idSearch[0] + i]:
            idSearch.append(idSearch[0] + i)
            i += 1

    if idSearch[0] != 0:
        i = 1
        while number == arr[idSearch[0] - i]:
            idSearch.append(idSearch[0] - i)
            i += 1

    idSearch.sort()

    print "ID : ", idSearch
    print "Number of operations - ", numOfOper


def printOptions():
    print "\n Choose : \n '1' - create a new array  \n '2' -  create random array \n '3' - see present array"
    print " '4' - go to the task  \n '5' - practice task \n '6' - exit menu "

    while True:
        try:
            choice = int(input("Your choice - "))
            if choice < 1 or choice > 6:
                raise Exception("Incorrect input")
            else:
                return choice
        except Exception as e:
            print e


def main():
    arr = []
    arrSize = 0
    while True:
        choice = printOptions()

        if choice == 1:
            try:
                arrSize = int(input("Enter the size of a new array - "))
                if arrSize < 0:
                    raise Exception("Incorrect input")
                else:
                    arr = []
                    for i in range(0, arrSize):
                        arr.append(int(input("Enter element : ")))
            except Exception as e:
                print e

        elif choice == 2:
            try:
                arrSize = int(input("Enter the size of a new array - "))
                loEnd = int(input("Enter the lower end of random numbers - "))
                hiEnd = int(input("Enter the higher end of random numbers - "))
                if arrSize < 0 or hiEnd < loEnd:
                    raise Exception("Incorrect input")
                else:
                    for i in range(0, arrSize):
                        arr.append(random.randint(loEnd, hiEnd))
            except Exception as e:
                print e

        elif choice == 3:
            try:
                if len(arr) == 0:
                    raise Exception("No array ")
                else:
                    print "Your array : ", arr
            except Exception as e:
                print e

        elif choice == 4:
            try:
                if len(arr) == 0:
                    raise Exception("No array ")
                else:
                    sortElem(arr)
            except Exception as e:
                print e

        elif choice == 5:
            try:
                if len(arr) == 0:
                    raise Exception("No array ")
                else:
                    newArray = sortElem(arr)
                    searchNumber = int(input("Enter search number - "))

                    binarySearch(newArray, searchNumber)

            except Exception as e:
                print e

        else:
            break


main()
