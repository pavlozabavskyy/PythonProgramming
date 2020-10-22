import re
def check_int(func):
    def func_wrapper(self, x):
        if not isinstance(x, int):
            raise Exception("The value must be a number for function {} to work".format(func.__name__))
        res = func(self, x)
        return res
    return func_wrapper


def check_str(func):
    def func_wrapper(self, x):
        if not isinstance(x, str):
            raise Exception("The value must be a string for function {} to work".format(func.__name__))
        res = func(self, x)
        return res
    return func_wrapper


def check_symbol(func):
    def func_wrapper(self, x):
        symb = re.search(r'[0-9,+,${}!@#%^&*()-=_№:.;/<>\|?]', x)
        if symb is not None:
            raise Exception("The value should not contain symbol for function {} to work".format(func.__name__))
        res = func(self, x)
        return res
    return func_wrapper

def check_lenght_Value(lenght):
    def actual_decorator(func):
        def func_wrapper(self, x):
            if len(str(x)) != lenght:
                raise Exception("len(value) = lenght for function {} to work".format(func.__name__))
            res = func(self, x)
            return res

        return func_wrapper
    return actual_decorator


def check_phone_number(func):
    def func_wrapper(self, x):
        symb = re.search(r'[a-zA-Z$]', x)
        if symb is not None:
            raise Exception("The value should not contain [a-Z] for function {} to work".format(func.__name__))
        elif x[0:4] != '+380': 
            raise Exception("Start +380 for function {} to work".format(func.__name__))
        elif len(x) != 13:
            print(len(x))
            raise Exception("len(x) != 13  for function {} to work".format(func.__name__))
        res = func(self, x)
        return res
    return func_wrapper

def enterIntDecor(func):
    def func_wrapper(value, message):
        while True:
            try:
                user_int = int(input(message))
                return user_int
            except ValueError:
                print("You must enter an integer for function {} to work".format(func.__name__))
        res = func(value, message)
        return res
    return func_wrapper

@enterIntDecor
def enterInt(value, message = "Enter value : "):
    return value


def enterStrDecor(func):
    def func_wrapper(value, message):
        while True:
            try:
                user_int = str(input(message))
                return user_int
            except ValueError:
                print("You must enter an str for function {} to work".format(func.__name__))
        res = func(value, message)
        return res
    return func_wrapper

@enterStrDecor
def enterStr(value = "0", message = "Enter value : "):
    return value


def intInRangeDecor(func):
    def func_wrapper(value, message, l, r):
        while True:
            try:
                data = enterInt(value, message)
                if data < l:
                    raise Exception('data < left border ')
                elif data > r:
                    raise Exception('data > right border ')
                else:
                    return data
                    break
            except Exception as e:
                print(e)
        res = func(value, message, l, r)
        return res
    return func_wrapper

@intInRangeDecor
def enterIntInRange(value = 0, message = "Enter value : ", l = 0, r = 100):
    return value
