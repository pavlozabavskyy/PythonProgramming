from LinkedList import Linked_list
from pattern_strategy import *
from validation import Validation as v
import sys



def main():
    options = '1 - Strategy 1\n2 - Strategy 2\n3 - generate data\n4 - remove at\n5 - remove in range\n6 - list method\n7 - print list\n8 - exit\n'
    linked_list = Linked_list()
    context = Context(Strategy1)
    while True:
        try:
            print(options)
            choice = v.intValidateInRange('Enter choice ', 0, 8)

            if choice == 1:
                context.strategy = Strategy1()  

            elif choice == 2:
                context.strategy = Strategy2()
                
            elif choice == 3:
                position = v.intValidateInRange('Enter position ', 0, len(linked_list))
                linked_list = context.do_some_business_logic(linked_list, position)

            elif choice == 4:
                position = v.intValidateInRange('Enter position', 0, len(linked_list)-1)
                linked_list.remove_at(position)

            elif choice == 5:
                print(f"From 0 to {len(linked_list) - 1}")
                l, r = v.int_validate_range()
                linked_list.remove_in_range(l, r)
                    
            elif choice == 6:
                linked_list = menu6(linked_list)

            elif choice == 7:
                print(linked_list)

            elif choice == 8:
                break

        except Exception as e:
            print('Error ', '--'*15, '  ',e)





def min_max(l: Linked_list):
    s, maximum, minim, j = l.average(), -sys.maxsize, sys.maxsize, 0
    
    for i in l:
        if i > maximum and i <= s:
            maximum = i 
            indexMax = j
        if i < minim and i >= s:
            minim = i 
            indexMin = j
        j += 1
    print(f'max elem - {maximum}, \nmin elem - {minim}, \naverage  - {s}\n')

    return indexMin, indexMax


def menu6(linked_list: Linked_list):
    l, r = min_max(linked_list)
    j = 0

    if r < l:
        temp = l
        l = r
        r = temp
    if r - l == 1:
        size = 1
    else:
        size = (r-l)//2
        
    print(f'left index - {l}, \nright index - {r}')

    for i in range(size):
        temp = linked_list.get_at(l+j)
        linked_list.set_at(l + j, linked_list.get_at(r - j))
        linked_list.set_at(r - j, temp)
        j += 1

    return linked_list

    


main()


    








