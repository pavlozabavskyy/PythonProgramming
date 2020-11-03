from classAddress import Address as CA
from classCollection import CollectionAddress as CC
from classCollectionCaretaker import CollectionCaretaker
from decorator import *

def main():
    options = '1 - insert collection from file\n2 - print collection\n3 - sort\n4 - search\n5 - delete obj\n6 - add new obj\n7 - edit obj\n8 - show history\n9 - undo\n10 - redo\n11 - exit\n'
    collect = CC()
    caretaker = CollectionCaretaker(collect)
    while True:
        try:
            print(options)
            choice = enterIntInRange(0, 'Enter choice : ', 0, 11)

            if choice == 1:
                menu1(caretaker, collect)

            elif choice == 2:
                print(collect)

            elif choice == 3:
                menu3(caretaker, collect)

            elif choice == 4:
                menu4(collect)

            elif choice == 5:
                menu5(caretaker, collect)

            elif choice == 6:
                menu6(caretaker, collect)

            elif choice == 7:
                menu7(caretaker, collect)

            elif choice == 8:
                menu8(caretaker)

            elif choice == 9:
                menu9(caretaker, collect)
            
            elif choice == 10:
                menu10(caretaker, collect)
                
            elif choice == 11:
                break

        except Exception as e:
            print('Error ', '--'*20, '  ',e)

def menu1(caretaker, collect):
    caretaker.backup()
    collect.readJsonFile('data.json')
    collect.writeJsonFile("output.json")

def menu3(caretaker, collect):
    attr = enterStr('0', 'Enter attribute: ')
    caretaker.backup()
    collect.sort(attr)
    collect.writeJsonFile("output.json")

def menu4(collect):
    value = enterStr('0', "Enter search elem - ")
    collect.search(value)

def menu5(caretaker, collect):
    index = enterIntInRange(0, f'Enter index from 0 to {len(collect) - 1}: ', 0, len(collect) -1)
    caretaker.backup()
    collect.deleteElem(index)
    collect.writeJsonFile("output.json")

def menu6(caretaker, collect):
    caretaker.backup()
    collect.addNewAddress()
    collect.writeJsonFile("output.json")

def menu7(caretaker, collect):
    caretaker.backup()
    collect.editAddress()
    collect.writeJsonFile("output.json")

def menu8(caretaker):
    caretaker.show_history()

def menu9(caretaker, collect):
    caretaker.undo()
    collect.writeJsonFile("output.json")

def menu10(caretaker, collect):
    caretaker.redo()
    collect.writeJsonFile("output.json")

"""if __name__ == '__main__':
    main()"""
