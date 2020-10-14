import re
class Validation():

    @staticmethod
    def strValidate(value, message = 'value'):
        if not isinstance(value, str):
            raise ValueError(f'{message}  must be str')
        return value

    @staticmethod
    def intValidate(value, message = 'value'):
        if not isinstance(value, int):
            raise ValueError(f'{message}  must be int')
        return value

    @staticmethod
    def lenghtValueValidate(value, lenght, message = 'value'):
        if len(str(value)) is not lenght:
            raise Exception(f'Invalid lenght of {message} ')
        return value


    @staticmethod
    def symbolValidate(value, message = 'value', dop = '+', digit = r'[0-9]'):
        value = Validation.strValidate(value, message)
        symb = re.search(r'[,${}!@#%^&*()-=_№:.;/<>\|?]'+ dop + digit, value)
        if symb is not None:
            raise ValueError(f'Bad str for {message},  --- symbol')  # IDEA: rename
        return value


    @staticmethod
    def numberValidate(value, message = 'value'):
        # +380
        value = Validation.strValidate(value, message)
        value = Validation.symbolValidate(value, message, r'[a-zA-Z]')

        if value[0:4] != '+380':
            raise Exception(f'Number error of {message}')
        return value

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
                data = Validation.enterInteger(message)
                if data < l:
                    raise Exception('data < left border ')
                elif data > r:
                    raise Exception('data > right border ')
                else:
                    return data
                    break
            except Exception as e:
                print(e)








"""



    @staticmethod
    def isdigitValid(value):
        try:
            if not value.isdigit():
                result = False
                raise Exception('it doesnt consist of number ')
            else:
                result = True
        except Exception as e:
            print(e)
        return result


    @staticmethod
    def isalphaValid(value):
        try:
            if not value.isalpha():
                result = False
                raise Exception('it doesnt consist of letour ')
            else:
                result = True
        except Exception as e:
            print(e)
        return result





    @staticmethod
    def lenghtValue(data, lenght):
        try:
            if len(str(data)) is not lenght:
                result = False
                raise Exception('Invalid lenght ')
            else:
                result = True
        except Exception as e:
            print(e)
        return result

    @staticmethod
    def validIntLimit(message, l, r):
        while True:
            try:
                data = Validation.enterInteger(message)
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
    def integerLimit(data, left, right):
        try:
            if left > right:
                result = True
                raise Exception('left > right ')
            elif data < left:
                result = False
                raise Exception('data < left border ')
            elif data > right:
                result = False
                raise Exception('data > right border ')
            else:
                result = True
        except Exception as e:
            print(e)
        return result

    @staticmethod
    def integerType(value):
        try:
            if not int(value):
                result = False
                raise Exception('not integer')
            else:
                result = True
        except Exception as e:
            print(e)
        return result



"""

@staticmethod
def openFile(name, flag):
    try:
        fileOpen = open(name, flag)
    except IOError:
        print('Error: can\'t find file or read data')
    else:
        return fileOpen
