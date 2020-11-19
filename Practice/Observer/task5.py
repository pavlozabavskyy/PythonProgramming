from LinkedList import Linked_list
from validation import Validation as v
from classContext import Context
from strategyIterator import StrategyIterator
from strategyFile import StrategyReadFile
from Observer import Observer
from Logger import Logger
from Event import Event
import copy


def main():
    options = '1 - Strategy 1\n2 - Strategy 2\n3 - generate data\n4 - remove at\n5 - remove in range\n6 - list method\n7 - print list\n8 - exit\n'
    linked_list = Linked_list()
    context = Context(StrategyIterator)

    Observer.attach('add', Logger.log)
    Observer.attach('delete', Logger.log)
    Observer.attach('deleteInRange', Logger.log)
    Observer.attach('taskMethod', Logger.log)

    while True:
        try:
            print(options)
            choice = v.intValidateInRange('Enter choice ', 1, 8)

            if choice == 1: context.strategy = StrategyIterator()  
            elif choice == 2: context.strategy = StrategyReadFile()
            elif choice == 3: linked_list = generateMenu(linked_list, context)
            elif choice == 4: linked_list = deleteAtMenu(linked_list)
            elif choice == 5: linked_list = deleteInRangeMenu(linked_list)       
            elif choice == 6: linked_list = listMethodMenu(linked_list)
            elif choice == 7: print(linked_list)
            elif choice == 8: break

        except Exception as e:
            print('Error ', '--'*15, '  ',e)


def generateMenu(linked_list: Linked_list, context):
    position = v.intValidateInRange('Enter position ', 0, len(linked_list))
    linked_list = context.do_some_business_logic(linked_list, position)
    return linked_list

def deleteAtMenu(linked_list: Linked_list):
    beforeList = copy.deepcopy(linked_list)
    position = v.intValidateInRange('Enter position', 0, len(linked_list)-1)
    linked_list.remove_at(position)
    Event.do_some('delete', [beforeList, position, linked_list])
    return linked_list

def deleteInRangeMenu(linked_list: Linked_list):
    beforeList = copy.deepcopy(linked_list)
    print(f"From 0 to {len(linked_list) - 1}")
    l, r = v.int_validate_range()
    linked_list.remove_in_range(l, r)
    Event.do_some('deleteInRange', [beforeList, [l, r], linked_list])
    return linked_list

def listMethodMenu(linked_list: Linked_list):
    beforeList = copy.deepcopy(linked_list)
    l, r = linked_list.min_max(linked_list)
    j = 1
    if r < l:
        temp = l
        l = r
        r = temp
        
    print(f'left index - {l}, \nright index - {r}')
    for i in range((r - l)//2):
        temp = linked_list.get_at(l+j)
        linked_list.set_at(l + j, linked_list.get_at(r - j))
        linked_list.set_at(r - j, temp)
        j += 1
    Event.do_some('taskMethod', [beforeList, [l, r], linked_list])
    return linked_list



if __name__ == '__main__':
    main()

    








