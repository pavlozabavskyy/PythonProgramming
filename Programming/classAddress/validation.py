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

        symb = re.search(r'[a-zA-Z$]', value)
        if symb is not None:
            raise Exception("The value should not contain [a-Z] for function {} to work".format(func.__name__))
        elif value[0:4] != '+380': 
            raise Exception("Start +380 for function {} to work".format(func.__name__))
        elif len(value) != 13:
            raise Exception("len(x) != 13 for function {} to work".format(func.__name__))
            
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
