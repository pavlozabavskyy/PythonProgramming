
class Validation():

    @staticmethod
    def enterStr(message):
        while True:
            try:
                user_str = str(input(message))
                return user_str
            except ValueError:
                print('You must enter an str')

    @staticmethod
    def enterInteger(message):
        while True:
            try:
                user_int = int(input(message))
                return user_int
            except ValueError:
                print('You must enter an integer')

    @staticmethod
    def intValidateInRange(message, l, r):
        while True:
            try:
                data = Validation.enterInteger(message+f'from {l} to {r} : ')
                if data < l:
                    raise Exception('data < left border ')
                elif data > r:
                    raise Exception('data > right border ')
                else:
                    return data
                    break
            except Exception as e:
                print(e)

    @staticmethod
    def int_validate_range():
        while True:
            try:
                l = Validation.enterInteger('Enter l : ')
                r = Validation.enterInteger('Enter r : ')
                if l > r:
                    raise Exception('l > r')
                else: 
                    return l, r
            except Exception as e:
                print(e)
