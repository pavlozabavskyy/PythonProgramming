from classAddress import Address as CA
from validation import Validation as v
from classCollection import CollectionAddress as CC


def options(arr):
    for i in arr:
        print(i)

    choice = v.intValidateInRange('Your choice - ', 0, len(arr))
    return choice

def main2():
    optionChArr = ['1 - insert collection from file' ,'2 - print collection', '3 - sort', '4 - search', '5 - delete obj', '6 - add new obj', '7 - edit obj', '8 - exit']
    collect = CC()
    while True:
        try:
            choice = options(optionChArr)

            if choice == 1:
                arr = CC.readFile()
                collect.fromStrAddress(arr)

            elif choice == 2:
                print(collect)

            elif choice == 3:
                attr = v.enterStr('Enter attribute: ')
                collect.sort(attr)
                print(collect)
                collect.writeFile("output.txt", "r+")

            elif choice == 4:
                value = v.enterStr("Enter search elem - ")
                collect.search(value)

            elif choice == 5:
                index = v.intValidateInRange('enter index - ', 0, len(collect))
                collect.deleteElem(index)
                #CC.writeFile("output.txt", "r+")

            elif choice == 6:
                collect.addNewAddress()
                #CC.writeFile("output.txt", "r+")

            elif choice == 7:
                collect.editAddress()
                #CC.writeFile("output.txt", "r+")

            elif choice == 8:
                break

        except Exception as e:
            print('Error ', '--'*20, '  ',e)



main2()
