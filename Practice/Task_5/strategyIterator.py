from validation import Validation as v
from LinkedList import Linked_list
from classStrategy import Strategy
from classSmith import Smith



class StrategyIterator(Strategy):

    def do_algorithm(self, l: Linked_list, position: int):
        j = 0
        n = v.enterInteger("Enter n: ")
        itSm = iter.SmithIter()
        for i in range(n):
            l.insert(position+j, next(itSm))
            j += 1

        return l
        




