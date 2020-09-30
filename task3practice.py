import random as rn


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def empty(self):
        return self.head == None

    def printList(self):
        while True:
            try:
                if self.head == None:
                    raise Exception("List is empty")
                else:
                    current = self.head
                    while(current):
                        print(current.data, " ")
                        current = current.next
                    return
            except Exception as e:
                print (e)
                return

    def top(self):
        while True:
            try:
                if self.head == None:
                    raise Exception("List is empty")
                else:
                    current = self.head
                    while current.next is not None:
                        current = current.next

                    return current.data
            except Exception as e:
                print (e)
                return

    def pop(self):
        while True:
            try:
                if self.head == None:
                    raise Exception("List is empty")
                else:
                    current = self.head
                    while current.next.next is not None:
                        current = current.next

                    current.next = None
                    return
            except Exception as e:
                print (e)
                return

    def size(self):
        if self.head == None:
            return 0
        else:
            current = self.head
            count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def at(self, n):
        while True:
            try:
                intT = isinstance(n, int)
                if self.head == None:
                    raise Exception("List is empty")
                elif not intT:
                    raise Exception("n is not 'int' ")
                elif n > self.size():
                    raise Exception(" n > size ")
                else:
                    current = self.head
                    for i in range(n):
                        current = current.next
                    return current.data

            except Exception as e:
                print (e)
                return
    def atRo(self, n, o):
        while True:
            try:
                intT = isinstance(n, int)
                if self.head == None:
                    raise Exception("List is empty")
                elif not intT:
                    raise Exception("n is not 'int' ")
                elif n > self.size():
                    raise Exception(" n > size ")
                else:
                    current = self.head
                    for i in range(n):
                        current = current.next
                    current.data = o
                    return

            except Exception as e:
                print (e)
                return

    def sumOfElem(self):
        while True:
            try:
                if self.head == None:
                    raise Exception("List is empty")
                else:
                    current = self.head
                    sum = 0
                    while(current):
                        sum += current.data
                        current = current.next
                    return sum

            except Exception as e:
                print (e)
                return



def average(list):
    return list.sumOfElem() / list.size()


def maxElemAverage(list):
    s, i, maximum, index = average(list), 0, list.at(0), 0

    while maximum > s:
        i += 1
        maximum = list.at(i)

    for i in range(list.size()):
        if list.at(i) > maximum and list.at(i) <= s:
            maximum = list.at(i)
            index = i

    print ("Maximum number - ", maximum, " , with index -- ", index)
    return index


def minElemAverage(list):
    s, i, minimum, index = average(list), 0, list.at(0), 0

    while minimum < s:
        i += 1
        minimum = list.at(i)

    for i in range(list.size()):
        if list.at(i) < minimum and list.at(i) >= s:
            minimum = list.at(i)
            index = i


    print ("Average - ", s, ", minimum number - ", minimum, " , with index -- ", index)
    return index


def progTask(list):
    l, r, j = minElemAverage(list), maxElemAverage(list), 0

    if r < l:
        temp = l
        l = r
        r = temp

    for i in range((r-l)//2):
        temp = list.at(l+j)
        list.atRo((l + j), list.at(r - j))
        list.atRo((r - j), temp)
        j += 1

    print ("Result : ", )

    return list


def validationInt(name):
    while True:
        try:
            n = int(input(name))
            break
        except ValueError:
            print('Incorrect input')
    return n

def printOptions():
    print ("\n Choose : \n '1' - create a new array  \n '2' -  create random array \n '3' - see present array")
    print (" '4' - go to the task  \n '5' - exit menu ")

    while True:
        try:
            choice = int(input("Your choice - "))
            if choice < 1 or choice > 6:
                raise Exception("Incorrect input")
            else:
                return choice
        except Exception as e:
            print (e)




def main():
    list = LinkedList()
    arrSize = 0
    while True:
        choice = printOptions()

        if choice == 1:
            try:
                arrSize = validationInt("Enter the size of a new array - ")
                if arrSize < 0:
                    raise Exception("Incorrect input")
                else:
                    list = LinkedList()
                    for i in range(0, arrSize):
                        list.insert(validationInt("Enter element : "))
            except Exception as e:
                print (e)

        elif choice == 2:
            try:
                arrSize = validationInt("Enter the size of a new array - ")
                loEnd = validationInt("Enter the lower end of random numbers - ")
                hiEnd = validationInt("Enter the higher end of random numbers - ")
                list = LinkedList()
                if arrSize < 0 or hiEnd < loEnd:
                    raise Exception("Incorrect input")
                else:
                    for i in range(0, arrSize):
                        list.insert(rn.randint(loEnd, hiEnd))
            except Exception as e:
                print (e)

        elif choice == 3:
            try:
                if list.size() == 0:
                    raise Exception("No array ")
                else:
                    print ("Your array : ",)
                    list.printList()
            except Exception as e:
                print (e)

        elif choice == 4:
            try:
                if list.size() == 0:
                    raise Exception("No array ")
                else:
                    result = progTask(list)
                    print(result.printList())
            except Exception as e:
                print (e)

        else:
            break

main()
