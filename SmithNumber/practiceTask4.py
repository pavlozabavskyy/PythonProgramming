import iteratorSm as iter
import funcSm as func
import generatorSm as gen


def IntValid(message):
    while True:
        try:
            user_int = int(input(message))
            return user_int
        except ValueError:
            print('You must enter an integer')


def Optione(arr):
    for i in arr:
        print(i)

    while True:
        try:
            data = IntValid("Your choice - ")
            if data < 0:
                raise Exception('data < left border ')
            elif data > len(arr) + 1:
                raise Exception('data > right border ')
            else:
                return data
                break
        except Exception as e:
            print(e)




def main():
    selectMethod = ['1 - func ', '2 - iterator ', '3 - generator ', '4 - exit ']
    modeArr = ['1 - next ', '2 - exit ']
    while True:
        choice = Optione(selectMethod)
        if choice == 1:
            current = func.nextNum()
            print(current)
            m = Optione(modeArr)
            while m != 2:
                temp = current
                current = func.nextNum(temp)
                print(current)
                m = Optione(modeArr)


        elif choice == 2:
            itSm = iter.SmithIter()
            m = Optione(modeArr)
            while m != 2:
                print(next(itSm))
                m = Optione(modeArr)

        elif choice == 3:
            finish = IntValid("Enter ")
            g = gen.generate(300)
            for i in g:
                print(i)

        else:
            break

main()
