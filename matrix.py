import numpy as np

def matrixN(n):
    matrix = np.zeros( (n, n) )

    matrix[0][0:n]  = 1      #First row     == 1
    matrix[:,0]     = 1      #First column  == 1
    matrix[-1][0:n] = 1      #Last row      == 1
    matrix[:,-1]    = 1      #Last column   == 1

    print(matrix)

def validationInt(name):
    while True:
        try:
            n = int(input(name))
            break
        except ValueError:
            print('Incorrect input')
    return n


def Options():
    print("\n Choose: \n '1' - test \n '2' - exit ")

    while True:
        try:
            choice = validationInt("Your choise - ")
            if choice < 1 or choice > 2:
                raise Exception("Incorrect input")
            else:
                return choice
        except Exception as e:
            print(e)


def main():
    while True:
        choice = Options()

        if choice == 1:
            try:
                n = validationInt("Enter N: ")
                if n <= 0:
                    raise Exception("Incorrect N ")
                else:

                    matrixN(n)

            except Exception as e:
                print(e)

        elif choice == 2:
            break


main()
