from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from validation import Validation as v
from LinkedList import Linked_list


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy


    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy


    def do_some_business_logic(self, l: Linked_list, position: int) -> None:
        result = self._strategy.do_algorithm(l, position)
        return result


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self):
        pass



class Strategy1(Strategy):
    def __primeDiv(self, n):
        i, a = 2, n
        div = []
        while i < a:
            if a % i == 0:
                div.append(i)
                a /= i
            else:
                i += 1
        div.append(a)
        return div

    def __sumD(self, n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit
            n = n // 10
        return sum

    def __isSmith(self, n):
        div = self.__primeDiv(n)
        sumOfNum = 0
        for i in div:
            if len(div) > 1:
                sumOfNum += self.__sumD(i)

        return sumOfNum == self.__sumD(n)

    
    def __init__(self, index = 4):
        self.num = index

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        current = num + 1
        while self.__isSmith(current) == False:
            current += 1
        self.num = current
        return num

    def do_algorithm(self, l: Linked_list, position: int):
        j = 0
        n = v.enterInteger("Enter n: ")
        for i in range(n):
                l.insert(position+j, next(self))
                j += 1

        return l
        





class Strategy2(Strategy):

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
        if len(l) == 0:
            l = temp
        else:
            for i in temp:
                l.insert(position+j, i)
                j += 1
        return l

