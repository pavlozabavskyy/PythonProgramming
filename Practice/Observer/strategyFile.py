from validation import Validation as v
from LinkedList import Linked_list
from classStrategy import Strategy
from Event import Event
import copy



class StrategyReadFile(Strategy):

    @staticmethod
    def __enter_file_name():
        file_name = v.enterStr('Enter file name:  ')
        return file_name

    @staticmethod
    def __readFile(fileName): 
        try:
            with open(fileName) as f:
                for line in f:
                    l = Linked_list([int(x) for x in line.split()])
            return l
        except Exception as e:
            raise e

    def do_algorithm(self, l: Linked_list, position: int):
        file_name = self.__enter_file_name()
        temp, j = self.__readFile(file_name), 0
        newList = copy.deepcopy(l)
        if len(l) == 0:
            l = temp
        else:
            for i in temp:
                l.insert(position+j, i)
                j += 1
        Event.do_some('add', [newList, position, l])
        return l

