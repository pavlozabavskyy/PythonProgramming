from classCollection import CollectionAddress
from classCollectionMemento import CollectionMemento
from decorator import *

class CollectionCaretaker:

    def __init__(self, collect: CollectionAddress):
        self._collect = collect
        self._mementos = []
        self._lenght = 0

    def backup(self):
        print('\nCaretaker: saving collection...')
        self._mementos.append(self._collect.save())
        self._lenght += 1
        if self._lenght == 6:
            self._mementos.pop(0)
            self._lenght -=1


    def undo(self):
        if not len(self._mementos):
            print('Empty')
            return

        memento = self._mementos.pop()

        try:
            self._collect.restore(memento)
            self._lenght -= 1
        except Exception as e:
            self.undo()
            print(e)


    def redo(self):
        index = enterIntInRange(0, f'Enter index from 0 to {self._lenght}: ', 0, self._lenght)
        for i in range(self._lenght - index-1):
            self._mementos.pop(index)
        self.undo()
        

    def show_history(self):
        print('\n\n!','_'*30 ,'history','_'*30, '!', "\nCaretaker: Here's the list of mementos:")
        j = 0
        for memento in self._mementos:
            print(j, ' -- memento', '-'*40, '\n')
            print(memento.name)
            j+=1
        print('!','_'*30 ,'history','_'*30, '!\n\n')



    @property
    def collect(self):
        return self._collect

   

