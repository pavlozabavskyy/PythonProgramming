from classAddress import Address as CA
from classCollection import CollectionAddress as CC
from classCollectionCaretaker import CollectionCaretaker
from decorator import *


def main2():
    options = '1 - insert collection from file\n2 - print collection\n3 - sort\n4 - search\n5 - delete obj\n6 - add new obj\n7 - edit obj\n8 - show history\n9 - undo\n10 - redo\n11 - exit\n'
    collect = CC()
    caretaker = CollectionCaretaker(collect)
    while True:
        try:
            print(options)
            choice = enterIntInRange(0, 'Enter choice : ', 0, 11)

            if choice == 1:
                arr = CC.readFile()
                caretaker.backup()
                collect.fromStrAddress(arr)

            elif choice == 2:
                print(collect)

            elif choice == 3:
                attr = enterStr('0', 'Enter attribute: ')
                caretaker.backup()
                collect.sort(attr)
                collect.writeFile("output.txt", "r+")

            elif choice == 4:
                value = enterStr('0', "Enter search elem - ")
                collect.search(value)

            elif choice == 5:
                index = enterIntInRange(0, f'Enter index from 0 to {len(collect) - 1}: ', 0, len(collect) -1)
                caretaker.backup()
                collect.deleteElem(index)
                collect.writeFile("output.txt", "r+")

            elif choice == 6:
                caretaker.backup()
                collect.addNewAddress()
                collect.writeFile("output.txt", "r+")

            elif choice == 7:
                caretaker.backup()
                collect.editAddress()
                collect.writeFile("output.txt", "r+")

            elif choice == 8:
                caretaker.show_history()

            elif choice == 9:
                caretaker.undo()
                collect.writeFile("output.txt", "r+")
            
            elif choice == 10:
                caretaker.redo()
                collect.writeFile("output.txt", "r+")
                
            elif choice == 11:
                break

        except Exception as e:
            print('Error ', '--'*20, '  ',e)

main2()
