from classAddress import Address as CA
from classCollectionMemento import CollectionMemento
from decorator import *
import copy
import json

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

    def __str__(self):
        return str(self.__arr)

    def __getitem__(self, index):
        return self.__arr[index]

    def __eq__(self, other):
        j = 0
        check = True
        if len(self.__arr) != len(other):
            check = False
        for i in range(len(self.__arr)):
            if self.__arr[i] != other[i]:
                check == False 
        return check

    def save(self):
        newCollect = copy.deepcopy(self.__arr)
        return CollectionMemento(newCollect)

    def restore(self, memento: CollectionMemento):
        try:
            self.__arr = memento.get_collect
        except Exception as e:
            print(e)

    def at(self, index):
        return self.__arr[index]

    def deleteElem(self, i):
        del self.__arr[i]

    def insert(self, obj):
        self.__arr.append(obj)

    def addNewAddress(self, arrSTR, arrINT):
        try:
            nA = CA()
            attributes = nA.getAttr()
            #attributes.remove("ID")
            for i in attributes:
                if isinstance(getattr(nA, i), int):
                    #valInt = enterInt(0, f'Enter {i} : ')
                    setattr(nA, str(i), arrINT[0])
                    arrINT.pop(0)       # якщо б ми мали декілька int значень , ми б присвоїли їх тут
                else:
                    #valStr = enterStr('0', f'Enter {i}: ')
                    setattr(nA, str(i), arrSTR[0])
                    arrSTR.pop(0)
            self.__arr.append(nA)
        except Exception as e:
            raise e

    def search(self, value):
        #print(f'search value : {value} \n')
        items = []
        for i in self.__arr:
            if i.strAddress().lower().find(str(value.lower())) != -1 :
                items.append(i)
        if not len(items):
            raise AttributeError('No search item')
            return

        return items   
        
    def sort(self, attr = 'address_line'):
        try:
            if isinstance(getattr(self.__arr[0], attr), int):
                self.__arr.sort(key = lambda x: getattr(x, attr))
            else:
                self.__arr.sort(key = lambda x: getattr(x, attr).lower())
        except AttributeError:
            raise AttributeError(f'\'Address\' object has no attribute {attr}')

    def bubbleSort(self, attr = 'address_line'):
        try:
            for i in range(len(self.__arr) - 1):
                for j in range(0, (len(self.__arr) - 1 - i)):
                    if isinstance(getattr(self.__arr[0], attr), int):
                        if getattr(self.__arr[j], attr) > getattr(self.__arr[j + 1], attr):
                            self.__arr[j], self.__arr[j+1] = self.__arr[j + 1], self.__arr[j]
                    else:
                        if getattr(self.__arr[j], attr).lower() > getattr(self.__arr[j + 1], attr).lower():
                            self.__arr[j], self.__arr[j+1] = self.__arr[j + 1], self.__arr[j]  
        except AttributeError:
            raise AttributeError(f'\'Address\' object has no attribute {attr}')   

    def editAddress(self, index, attr, value):
        try:
            #attr = enterStr('0', 'Enter attribute: ')
            #index = enterIntInRange(0, 'Enter index : ', 0, len(collect))
            if isinstance(getattr(self.__arr[index], attr), int):
                #valInt = enterInt(0, f'Enter {attr} : ')
                setattr(self.__arr[index], attr, value)
            else:
                #valStr = enterStr('0', f'Enter {attr}: ')
                setattr(self.__arr[index], attr, value)

        except Exception as e:
            raise e

    @fileNameValidate
    def readJsonFile(self, fileName):
        self.__arr = []
        with open(fileName) as file:
            jsonList = json.load(file)
        newObj = CA()        
        attr = newObj.getAttr()
        #attr.remove('ID')
        
        for i in jsonList:
            try:
                newObj = CA()   
                for j in attr:
                    if isinstance(getattr(newObj, j), int):
                        setattr(newObj, j, int(i.get(str(j))))
                    else:
                        setattr(newObj, j, str(i.get(str(j))))
            except Exception as e:
                print('Error ', e)
                continue
            self.__arr.append(newObj)

    @fileNameValidate
    def writeJsonFile(self, fileName):
        with open(fileName, mode='w') as file:
            file.write('[')
            for i in self.__arr:
                file.write(i.jsonFormat())
                if i != self.__arr[len(self) - 1]:
                    file.write(', ')
            file.write(']')