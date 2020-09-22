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

    print ("Maximum number - ", maximum, " , with index -- ", index)
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

    print ("Average - ", s, ", minimum number - ", minimum, " , with index -- ", index)
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

    print ("Elements in between (with reverse sort) - ", newArray)

    newArray.sort(reverse=True)

    j = 0
    for i in range(l + 1, r):
        arr[i] = newArray[j]
        j += 1

    print ("Result : ", arr)


def printOption():
    print ("\n Choose : \n '1' - create a new array  \n '2' -  create random array \n '3' - see present array")
    print (" '4' - go to the task \n '5' - exit menu ")

    while True:
        try:
            choice = int(input("Your choice - "))
            if choice < 1 or choice > 5:
                raise Exception("Incorrect input")
            else:
                return choice
        except Exception as e:
            print (e)


def main():
    arr = []
    arrSize = 0
    while True:
        choice = printOption()

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
                print (e)

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
                print (e)

        elif choice == 3:
            try:
                if len(arr) == 0:
                    raise Exception("No array ")
                else:
                    print ("Your array : ", arr)
            except Exception as e:
                print (e)

        elif choice == 4:
            try:
                if len(arr) == 0:
                    raise Exception("No array ")
                else:
                    sortElem(arr)
            except Exception as e:
                print (e)

        else:
            break


main()
