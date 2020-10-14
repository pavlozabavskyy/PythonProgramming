from classAddress import Address as CA
from decorator import *

class CollectionAddress():
    __arr = []

    def __init__(self):
        self.__arr = []

    def __repr__(self):
        return str(self.__arr)

    def __iter__(self):
        return iter(self.__arr)

    def __len__(self):
        return len(self.__arr)

    def at(self, index):
        return self.__arr[index]

    def deleteElem(self, i):
        del self.__arr[i]

    def insert(self, obj):
        self.__arr.append(obj)

    def fromStrAddress(self, a):
        nA = CA()
        try:
            attributes = nA.getAttr()
            attributes.remove("ID")
            for i in a:
                nA = CA()
                k = 0
                for j in attributes:
                    if isinstance(getattr(nA, j), int):
                        setattr(nA, str(j), int(i[k]))
                    else:
                        setattr(nA, str(j), str(i[k]))
                    k += 1

                self.__arr.append(nA)

        except Exception as e:
            raise e


    def addNewAddress(self):
        nA = CA()    # new Address obj
        try:
            attributes = nA.getAttr()
            attributes.remove("ID")
            for i in attributes:
                if isinstance(getattr(nA, i), int):
                    valInt = enterInt(0, f'Enter {i} : ')
                    setattr(nA, str(i), valInt)
                else:
                    valStr = enterStr('0', f'Enter {i}: ')
                    setattr(nA, str(i), valStr)
            self.__arr.append(nA)
        except Exception as e:
            raise e

    def search(self, value):
        print(f'search value : {value} \n')
        check = True
        for i in self.__arr:
            if i.strAddressWithId().lower().find(str(value.lower())) != -1 :
                check = False
                print(i)
        if check:
            print('no search elem ')

    def writeFile(self, fileName = 'output.txt', flag = 'r+'):
        try:
            fw = open(fileName, flag)
            fw.write(str(self.__arr))
            fw.close()
        except IOError:
            raise 'Error: can\'t find file or read data'


    def sort(self, attr = 'address_line'):
        try:
            if isinstance(getattr(self.__arr[0], attr), int):
                self.__arr.sort(key = lambda x: getattr(x, attr))
            else:
                self.__arr.sort(key = lambda x: getattr(x, attr).lower())
        except AttributeError:
            raise AttributeError(f'\'Address\' object has no attribute {attr}')

    def editAddress(self):
        try:
            attr = enterStr('0', 'Enter attribute: ')
            index = enterIntInRange(0, 'Enter index : ', 0, len(collect))
            if isinstance(getattr(self.__arr[index], attr), int):
                valInt = enterInt(0, f'Enter {attr} : ')
                setattr(self.__arr[index], attr, valInt)
            else:
                valStr = enterStr('0', f'Enter {attr}: ')
                setattr(self.__arr[index], attr, valStr)

        except Exception as e:
            raise e

    @staticmethod
    def readFile(fileName = "data.txt"):
        try:
            open(fileName)
            with open(fileName) as f:
                arrOfStr = [line.split() for line in f]
            f.close()
            return arrOfStr
        except Exception as e:
            raise e
