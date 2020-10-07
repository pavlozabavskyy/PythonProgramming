
class Validation():

    @staticmethod
    def enterStr(message):
        while True:
            try:
                user_int = str(input(message))
                return user_int
            except ValueError:
                print('You must enter an str')


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
    def enterInteger(message):
        while True:
            try:
                user_int = int(input(message))
                return user_int
            except ValueError:
                print('You must enter an integer')


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


    @staticmethod
    def openFile(name, flag):
        try:
            fileOpen = open(name, flag)
        except IOError:
            print('Error: can\'t find file or read data')
        else:
            return fileOpen
