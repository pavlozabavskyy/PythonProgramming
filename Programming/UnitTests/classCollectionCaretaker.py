from classCollection import CollectionAddress
from classCollectionMemento import CollectionMemento
from decorator import *

class CollectionCaretaker:

    def __init__(self, collect):
        self._collect = collect
        self._mementos = []
        self._current = 0
        self._maxlen = 5
        self._checkUndo = False

    def backup(self):
        self._mementos.append(self._collect.save())
        if not self._checkUndo:
            self._current += 1
        if len(self._mementos) == (self._maxlen + 1):
            self._mementos.pop(0)
            self._current -= 1

    def __isEmpty(self):
        if not len(self._mementos):
            raise Exception('empty memento')

    def undo(self):
        self.__isEmpty()

        if self._current == 0:
            raise Exception('Current = 0')
        else:
            self._current -= 1
            memento = self._mementos[self._current]
            try:
                self._collect.restore(memento)
            except Exception as e:
                print(e)
            self._checkUndo = True

    def redo(self):
        self.__isEmpty()

        if self._current >= (len(self._mementos)-1):
            raise Exception('last caretaker')        
        else:
            self._current += 1
            memento = self._mementos[self._current]
            try:
                self._collect.restore(memento)
            except Exception as e:
                print(e)
        
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

   

