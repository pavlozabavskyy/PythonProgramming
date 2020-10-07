import classCollection as CA

class Collection():
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

    def search(self, value):
        #trueSearchArrInd = []
        #j = 0
        check = True
        for i in self.__arr:
            if i.strAddressWithId.find(str(value)) != -1 :
                #trueSearchArrInd.append(j)
                check = False
                print(i)
            #j++

        if not check:
            print('no search elem ')
        #return trueSearchArrInd()




    def sort(self, func):
        self.__arr.sort(key = func)
