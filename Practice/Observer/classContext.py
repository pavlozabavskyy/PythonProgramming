from __future__ import annotations
from classStrategy import Strategy
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