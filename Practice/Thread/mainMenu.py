from LinkedList import Linked_list
from validation import Validation as v
from classContext import Context
from strategyIterator import StrategyIterator
from strategyFile import StrategyReadFile
from Observer import Observer
from Logger import Logger
from Event import Event
import copy
import threading


def main():
    """
    Main function.
    """
    Observer.attach('add', Logger.log)
    Observer.attach('delete', Logger.log)
    Observer.attach('deleteInRange', Logger.log)
    Observer.attach('taskMethod', Logger.log)

    linked_list1 = Linked_list()
    linked_list2 = Linked_list()
    options = '1 - first list \n2 - second list\n3 - list method\n4 - print lists\n5 - exit\n'
    while True:
        try:
            print(options)
            choice = v.intValidateInRange('Enter choice ', 1, 5)
            if choice == 1: linked_list1 = generateList(linked_list1, 'l1')
            elif choice == 2: linked_list2 = generateList(linked_list2, 'l2')
            elif choice == 3: linked_list1, linked_list2 = listMethod(linked_list1, linked_list2)
            elif choice == 4: print('list 1 - {}\nlist 2 - {}\n'.format(linked_list1, linked_list2))
            elif choice == 5: break
        except Exception as e:
                print('Error ', '--'*15, '  ',e)

def generateList(linked_list: Linked_list, lname = 'l'):
    options = ' 1 - Strategy 1\n 2 - Strategy 2\n 3 - generate data\n 4 - print list\n 5 - exit\n'
    context = Context(StrategyIterator)
    while True:  
        print(options)
        choice = v.intValidateInRange('Enter choice ', 1, 5)
        if choice == 1: context.strategy = StrategyIterator()  
        elif choice == 2: context.strategy = StrategyReadFile()
        elif choice == 3: linked_list = generateMenu(linked_list, context, lname)
        elif choice == 4: print(linked_list)
        elif choice == 5: return linked_list

def generateMenu(linked_list: Linked_list, context, lname = 'l'):
    position = v.intValidateInRange('Enter position ', 0, len(linked_list))
    linked_list = context.do_some_business_logic(linked_list, position, lname)
    return linked_list

def listMethod(linked_list1: Linked_list, linked_list2: Linked_list):
    options = '  1 - remove at\n  2 - remove in range\n  3 - task method\n  4 - print lists\n  5 - exit\n'
    thread1 = threading.Thread()
    thread2 = threading.Thread()
    while True:
        try:
            print(options)
            choice = v.intValidateInRange('Enter choice ', 1, 5)
            if choice == 1: 
                position = v.enterInteger('Enter position: ')
                thread1 = threading.Thread(target=deleteAtMenu, args=(linked_list1, position, 'l1', ))
                thread2 = threading.Thread(target=deleteAtMenu, args=(linked_list2, position, 'l2', ))
                
            elif choice == 2:
                l, r = v.int_validate_range()
                thread1 = threading.Thread(target=deleteInRangeMenu, args=(linked_list1, l, r, 'l1', ))
                thread2 = threading.Thread(target=deleteInRangeMenu, args=(linked_list2, l, r, 'l2', ))
                thread1.start()
                thread2.start() 
            elif choice == 3:
                thread1 = threading.Thread(target=listMethodMenu, args=(linked_list1, 'l1', ))
                thread2 = threading.Thread(target=listMethodMenu, args=(linked_list2, 'l2', ))
                thread1.start()
                thread2.start() 
            elif choice == 4:
                print('list 1 - {}\nlist 2 - {}\n'.format(linked_list1, linked_list2))
            elif choice == 5:
                return linked_list1, linked_list2
        
        except Exception as e:
            print('Error ', '--'*15, '  ',e)
        thread1.start()
        thread2.start() 
        thread1.join()
        thread2.join()

def deleteAtMenu(linked_list: Linked_list, position: int, lname: str):
    print('Thread {}  : starting'.format(lname[1]))
    beforeList = copy.deepcopy(linked_list)
    linked_list.remove_at(position)
    Event.do_some('delete', [beforeList, position, linked_list, lname])
    print('Thread {}  : finishing'.format(lname[1]))
    return linked_list

def deleteInRangeMenu(linked_list: Linked_list, l: int, r: int, lname: str):
    print('Thread {}  : starting'.format(lname[1]))
    beforeList = copy.deepcopy(linked_list)
    linked_list.remove_in_range(l, r)
    Event.do_some('deleteInRange', [beforeList, [l, r], linked_list, lname])
    print('Thread {}  : finishing'.format(lname[1]))
    return linked_list

def listMethodMenu(linked_list: Linked_list, lname: str):
    print('Thread {}  : starting'.format(lname[1]))
    beforeList = copy.deepcopy(linked_list)
    l, r = linked_list.min_max(linked_list)
    j = 1
    if r < l:
        temp = l
        l = r
        r = temp

    for i in range((r - l)//2):
        temp = linked_list.get_at(l+j)
        linked_list.set_at(l + j, linked_list.get_at(r - j))
        linked_list.set_at(r - j, temp)
        j += 1
    Event.do_some('taskMethod', [beforeList, [l, r], linked_list, lname])
    print('Thread {}  : finishing'.format(lname[1]))
    return linked_list


if __name__ == '__main__':
    main()
    








