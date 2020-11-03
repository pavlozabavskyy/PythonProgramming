import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self, l = None):
        self.__lenght = 0
        self.__head = None
        if l is not None:
            for i in l:
                self.append(i)

    def __len__(self):
        return self.__lenght

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        current, l_str = self.__head, '[ '
        while current is not None:
            l_str += f'{str(current.data)}, '
            current = current.next
        l_str += ']'
        return l_str


    def __out_of_range(self, index):
        if index >= self.__lenght:
            raise IndexError('Out of range')


    def __list_is_empty(self):
        if self.__lenght == 0:
            raise Exception('List is empty')
    
    
    def append(self, value):
        if self.__head == None:
            self.__head = Node(value)
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
        self.__lenght += 1


    def insert(self, index, value):
        if index == 0:
            new_node = Node(value)
            temp = self.__head
            self.__head = new_node
            new_node.next = temp
            self.__lenght += 1
            return
        elif index == self.__lenght:
            self.append(value)
            return
        else:
            self.__out_of_range(index)
            i, current, prev = 0, self.__head, None
            while current != None:
                if i == index:
                    new_node = Node(value)
                    prev.next = new_node
                    new_node.next = current
                    self.__lenght += 1
                    return
                prev = current
                current = current.next
                i += 1


    def remove_at(self, index):
        self.__list_is_empty()
        self.__out_of_range(index)
        if index == 0:
            temp = self.__head
            self.__head = self.__head.next
            temp.next = None
            self.__lenght -= 1
            return
        else:
            i, current, prev = 0, self.__head, None
            while current != None:
                if i == index:
                    prev.next = current.next
                    current.next = None
                    self.__lenght -= 1
                    return
                prev = current
                current = current.next
                i += 1

    def remove_in_range(self, l, r):
        for i in range(r-l+1):
            self.remove_at(l)


    def average(self):
        sum = 0 
        for i in self:
            sum += i
        return sum / self.__lenght

    def __at(self, index):
        self.__list_is_empty()
        self.__out_of_range(index)
        current = self.__head
        for i in range(index):
            current = current.next
        return current

    def get_at(self, index):
        current = self.__at(index)
        return current.data

    def set_at(self, index, value):
        current = self.__at(index)
        current.data = value

    @staticmethod
    def min_max(l):
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

