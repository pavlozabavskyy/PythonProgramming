from classAddress import Address as CA
from classCollection import CollectionAddress as CC
from decorator import *


def main2():
    options = '1 - insert collection from file\n2 - print collection\n3 - sort\n4 - search\n5 - delete obj\n6 - add new obj\n7 - edit obj\n8 - exit\n'
    collect = CC()
    while True:
        try:
            print(options)
            choice = enterIntInRange(0, 'Enter choice : ', 0, 9)

            if choice == 1:
                arr = CC.readFile()
                collect.fromStrAddress(arr)

            elif choice == 2:
                print(collect)

            elif choice == 3:
                attr = enterStr('0', 'Enter attribute: ')
                collect.sort(attr)
                collect.writeFile("output.txt", "r+")

            elif choice == 4:
                value = enterStr('0', "Enter search elem - ")
                collect.search(value)

            elif choice == 5:
                index = enterIntInRange(0, 'Enter index : ', 0, len(collect))
                collect.deleteElem(index)
                collect.writeFile("output.txt", "r+")

            elif choice == 6:
                collect.addNewAddress()
                collect.writeFile("output.txt", "r+")

            elif choice == 7:
                collect.editAddress()
                collect.writeFile("output.txt", "r+")

            elif choice == 8:
                break

        except Exception as e:
            print('Error ', '--'*20, '  ',e)

main2()
