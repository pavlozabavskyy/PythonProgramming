from validation import Validation as v
from LinkedList import Linked_list
from classStrategy import Strategy
from classSmith import Smith



class StrategyIterator(Strategy):

    def do_algorithm(self, l: Linked_list, position: int):
        j = 0
        n = v.enterInteger("Enter n: ")
        itSm = iter(Smith())
        for i in range(n):
            data = next(itSm)
            l.insert(position+j, data)
            j += 1

        return l
        


