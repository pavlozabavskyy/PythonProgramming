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
                readFromFileMenu(caretaker, collect)

            elif choice == 2:
                print(collect)

            elif choice == 3:
                sortMenu(caretaker, collect)

            elif choice == 4:
                searchMenu(collect)

            elif choice == 5:
                deleteMenu(caretaker, collect)

            elif choice == 6:
                newObjMenu(caretaker, collect)

            elif choice == 7:
                editObjMenu(caretaker, collect)

            elif choice == 8:
                mementoHistoryMenu(caretaker)

            elif choice == 9:
                undoMenu(caretaker, collect)
            
            elif choice == 10:
                redoMenu(caretaker, collect)
                
            elif choice == 11:
                break

        except Exception as e:
            print('Error ', '--'*20, '  ',e)

def readFromFileMenu(caretaker, collect):
    caretaker.backup()
    collect.readJsonFile('data.json')
    collect.writeJsonFile("output.json")

def sortMenu(caretaker, collect):
    attr = enterStr('0', 'Enter attribute: ')
    caretaker.backup()
    collect.sort(attr)
    collect.writeJsonFile("output.json")

def searchMenu(collect):
    value = enterStr('0', "Enter search elem - ")
    collect.search(value)

def deleteMenu(caretaker, collect):
    index = enterIntInRange(0, f'Enter index from 0 to {len(collect) - 1}: ', 0, len(collect) -1)
    caretaker.backup()
    collect.deleteElem(index)
    collect.writeJsonFile("output.json")

def newObjMenu(caretaker, collect):
    caretaker.backup()
    collect.addNewAddress()
    collect.writeJsonFile("output.json")

def editObjMenu(caretaker, collect):
    caretaker.backup()
    collect.editAddress()
    collect.writeJsonFile("output.json")

def mementoHistoryMenu(caretaker):
    caretaker.show_history()

def undoMenu(caretaker, collect):
    caretaker.undo()
    collect.writeJsonFile("output.json")

def redoMenu(caretaker, collect):
    caretaker.redo()
    collect.writeJsonFile("output.json")

if __name__ == '__main__':
    main()
