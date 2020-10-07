import classAdress as CA
import validation as valid
import classCollection as CC



def newObjAddress():
    address_line = valid.Validation.enterStr('enter address_line ')
    postal_code = valid.Validation.enterInteger('enter postal_code ')
    country = valid.Validation.enterStr('enter country ')
    city = valid.Validation.enterStr('enter city ')
    fax_number = valid.Validation.enterStr('enter fax_number ')
    phone_number = valid.Validation.enterStr('enter phone_number ')

    ad = CA.Address(address_line, postal_code, country, city, fax_number, phone_number)
    #address = f'{address_line} {postal_code} {country} {city} {fax_number} {phone_number}'
    writeFile(ad.strAddressWithoutId, "data.txt", "a")

    return ad


def writeFile(strObj, fileName = "data.txt", flag = "r+"):
    fw = valid.Validation.openFile(fileName, flag)
    fw.write(strObj)
    fw.close()

def readFile(fileName = "data.txt"):
    with open(fileName) as f:
        arrOfStr = [line.split() for line in f]

    f.close()
    return arrOfStr

def fromStrAddress(arr):
    collect = CC.Collection()
    for i in arr:
        address_line = i[0]
        postal_code = int(i[1])
        country = i[2]
        city = i[3]
        fax_number = i[4]
        phone_number = i[5]
        address = CA.Address(address_line, postal_code, country, city, fax_number, phone_number)
        collect.insert(address)

    return collect

def reWriteFile(arr, fileName = "data.txt", flag = "r+"):
    for i in arr:
        writeFile(i.strAddressWithoutId)


def options(arr):
    for i in arr:
        print(i)

    choice = valid.Validation.validIntLimit('Your choice - ', 0, len(arr))
    return choice

def sortCollection(collect):
    sortChArr = ['sort key:','1 - ID', '2 - address_line', '3 - postal_code', '4 - country', '5 - city', '6 - fax_number', '7 - phone_number']
    choice = options(sortChArr)
    if choice == 1:
        collect.sort(lambda x: x.ID)
        return collect
    elif choice == 2:
        collect.sort(lambda x: x.address_line)
        return collect
    elif choice == 3:
        collect.sort(lambda x: x.postal_code)
        return collect
    elif choice == 4:
        collect.sort(lambda x: x.country)
        return collect
    elif choice == 5:
        collect.sort(lambda x: x.city)
        return collect
    elif choice == 6:
        collect.sort(lambda x: x.fax_number)
        return collect
    else:
        collect.sort(lambda x: x.phone_number)
        return collect


def editObjCollection(collect):
    index = valid.Validation.validIntLimit('enter index - ', 0, len(collect))
    ChArr = [' ', '1 - address_line', '2 - postal_code', '3 - country', '4 - city', '5 - fax_number', '6 - phone_number']
    choice = options(ChArr)

    if choice == 1:
        collect.at(index).address_line = valid.Validation.enterStr('enter address_line ')
    elif choice == 2:
        collect.at(index).postal_code = valid.Validation.enterInteger('enter postal_code ')
    elif choice == 3:
        collect.at(index).country = valid.Validation.enterStr('enter country ')
    elif choice == 4:
        collect.at(index).city = valid.Validation.enterStr('enter city ')
    elif choice == 5:
        collect.at(index).fax_number = valid.Validation.enterStr('enter fax_number ')
    elif choice == 6:
        collect.at(index).phone_number = valid.Validation.enterStr('enter phone_number ')

    return collect

def main():
    optionChArr = ['1 - insert collection from file' ,'2 - print collection', '3 - sort', '4 - search', '5 - delete obj', '6 - add new obj', '7 - edit obj', '8 - exit']
    collect = CC.Collection()
    searchInd = []
    while True:
        choice = options(optionChArr)

        if choice == 1:
            arr = readFile()
            collect = fromStrAddress(arr)

        elif choice == 2:
            print(collect)
            collect.at(2).fax_number = "213123"
            print(collect.at(2))

        elif choice == 3:
            collect = sortCollection(collect)
            reWriteFile(collect)

        elif choice == 4:
            collect = sortCollection(collect)
            reWriteFile(collect)

        elif choice == 5:
            choi = valid.Validation.validIntLimit('enter index - ', 0, len(collect))
            collect.deleteElem(choi)
            reWriteFile(collect)

        elif choice == 6:
            newAddress = newObjAddress()
            collect.insert(newAddress)

        elif choice == 7:
            collect = editObjCollection(collect)
            reWriteFile(collect)

        elif choice == 8:
            break


main()
