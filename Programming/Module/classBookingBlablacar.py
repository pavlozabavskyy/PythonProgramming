from decorator import Validation as v 
import json

class BlablacarBooking:

    def __init__(self, DriverName = 'name', NoOfPeople = 1, StartTime = '10-22-33', EndTime = '11-22-33', StartPlace = 'placea', EndPlace = 'placeb'):
        self.DriverName = DriverName
        self.NoOfPeople = NoOfPeople
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.StartPlace = StartPlace
        self.EndPlace = EndPlace


    def __str__(self):
        result = '\n!_______________________!'
        for i in self.getProperty():
            result += '\n'+ str(i) + ' - '+ str(getattr(self, str(i)))
        result += '\n!_______________________!\n'
        return result

    def __repr__(self):
        return self.__str__()

    def getProperty(self):
        return [name for name, value in vars(BlablacarBooking).items() if isinstance(value, property)]

    def jsonFormat(self):
        data = {}
        for i in self.getProperty():
            data[i.replace('_BlablacarBooking__', '')] = getattr(self, i)
        return json.dumps(data, indent = 8)


    @property
    def DriverName(self):
        return self._DriverName


    @DriverName.setter
    @v.checkType(str)
    @v.checkSymbol
    def DriverName(self, value):
        self._DriverName = value

    @property
    def NoOfPeople(self):
        return self._NoOfPeople

    @NoOfPeople.setter
    @v.checkType(int)
    @v.checkNoOf
    def NoOfPeople(self, value):
        self._NoOfPeople = value

    @property
    def StartTime(self):
        return str(self._StartTime)

    def getStartTime(self):
        return self._StartTime

    

    @StartTime.setter
    @v.timeValidate
    def StartTime(self, value):
        self._StartTime = value

    @property
    def EndTime(self):
        return str(self._EndTime)

    def getEndTime(self):
        return self._EndTime

    @EndTime.setter
    @v.timeValidate
    #@v.timeEndValidate(self.getStartTime)
    def EndTime(self, value):
        self._EndTime = value

    @property
    def StartPlace(self):
        return self._StartPlace

    @StartPlace.setter
    @v.checkType(str)
    @v.checkSymbol
    def StartPlace(self, value):
        self._StartPlace = value

    @property
    def EndPlace(self):
        return self._EndPlace

    @EndPlace.setter
    @v.checkType(str)
    @v.checkSymbol
    def EndPlace(self, value):
        self._EndPlace = value