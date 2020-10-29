from decorator import Validation as v
import json
from classBookingBlablacar import BlablacarBooking
from datetime import time

class MyCollection:

    def __init__(self):
        self.__arr = []

    def __str__(self):
        return str(self.__arr)

    def __iter__(self):
        return iter(self.__arr)

    def __len__(self):
        return len(self.__arr)


    def insert(self, obj: BlablacarBooking):  
        self.__arr.append(obj)


    def __checkHour(self, timeCheck, name):
        countPeople = 0
        for i in self.__arr:
            if i.getStartTime() <= timeCheck  and i.getEndTime() >= timeCheck:
                if i.DriverName == name:
                    raise Exception("Name error ")
                countPeople += i.NoOfPeople
        if countPeople >= 4:
            return False
        else: 
            return True


    def countOfTrips(self, name):
        count = 0
        for i in self.__arr:
            if i.DriverName == name:
                count += 1
        return count


    def __countOfTripsInHour(self, hour):
        count = 0
        for i in self.__arr:
            if i.getStartTime() == hour:
                count += 1
        return count



    def hourMoreTrips(self):
        maximum = 0
        for i in self.__arr:
            if maximum < self.__countOfTripsInHour(i.getStartTime()):
                maximum = self.__countOfTripsInHour(i.getStartTime())
                hour = i.getStartTime()

        print("Hour: {}".format(hour))



    def UserWithMoreTrips(self):
        maximum = 0
        name = ''
        for i in self.__arr:
            if maximum < self.countOfTrips(i.DriverName):
                maximum = self.countOfTrips(i.DriverName)
                name = i.DriverName
        with open('bestBla.json', mode='w') as file:
            file.write('[')
            for i in self.__arr:
                if i.DriverName == name:
                    file.write(i.jsonFormat())
                    if i != self.__arr[len(self) - 1]:
                        file.write(', ')
            file.write(']')


        print('Check bestBla.json file ')








    def addNewObj(self):
        newObj = BlablacarBooking()  
        try:
            attr = newObj.getProperty()
            for j in attr:
                if isinstance(getattr(newObj, j), int):
                    data = int(input('enter {} :'.format(j)))
                    setattr(newObj, j, int(data))
                else:
                    string = str(input("enter {} : ".format(j)))
                    if j.endswith('Time'):
                        [hh, mm, ss] = string.split('-')
                        val = time(int(hh), int(mm), int(ss))
                        if not self.__checkHour(val, newObj.DriverName):
                            raise Exception('Invalid time. more then 4 people')

                    setattr(newObj, j, str(string))

            self.__arr.append(newObj)

        except Exception as e:
            print(e)

    @v.fileNameValidate
    def readJsonFile(self, fileName):
        self.__arr = []
        with open(fileName) as file:
            jsonList = json.load(file)
        newObj = BlablacarBooking()        
        attr = newObj.getProperty()
        
        for i in jsonList:
            try:
                newObj = BlablacarBooking()   
                for j in attr:
                    if isinstance(getattr(newObj, j), int):
                        setattr(newObj, j, int(i.get(str(j))))
                    elif isinstance(getattr(newObj, j), float):
                        setattr(newObj, j, float(i.get(str(j))))
                    else:
                        setattr(newObj, j, str(i.get(str(j))))
            except Exception as e:
                print('Error ', e)
                continue
            self.__arr.append(newObj)


    @v.fileNameValidate
    def writeJsonFile(self, fileName):
        with open(fileName, mode='w') as file:
            file.write('[')
            for i in self.__arr:
                file.write(i.jsonFormat())
                if i != self.__arr[len(self) - 1]:
                    file.write(', ')
            file.write(']')
