import re
from datetime import time


class Validation:

    @staticmethod
    def checkType(typeE):
        def actual_decorator(func):
            def func_wrapper(_self, val):
                if not isinstance(val, typeE):
                    raise ValueError("The value must be a {} for {} to work".format(str(typeE), func.__name__))
                func(_self, val)
            return func_wrapper
        return actual_decorator


    @staticmethod
    def checkSymbol(func):
        def func_wrapper(_self, val):
            symb = re.search(r'[0-9,+,${}!@#%^&*()-=_№:.;/<>\|?]', val)
            if symb is not None:
                raise Exception("The value should not contain symbol for function {} to work".format(func.__name__))
            func(_self, val)
        return func_wrapper

    @staticmethod
    def fileNameValidate(func):
        def func_wrapper(_self, val): 
            if not val.endswith('.json'):
                raise ValueError("The value must be json format for function {} to work".format(func.__name__))
            func(_self, val)
        return func_wrapper


    @staticmethod
    def checkNoOf(func):
        def func_wrapper(_self, val):
            if val < 0 or val > 4:
                raise Exception("The value must be 0-4 for function {} to work".format(func.__name__))
            func(_self, val)
        return func_wrapper


    @staticmethod
    def timeValidate(func):
        def func_wrapper(_self, val):
            try:
                if isinstance(val, str):
                    [hh, mm, ss] = val.split('-')
                    val = time(int(hh), int(mm), int(ss))
            except Exception:
                raise Exception("The value must be Time formar for function {} to work".format(func.__name__))
            func(_self, val)
        return func_wrapper

    @staticmethod
    def timeEndValidate(startTime):
        def actual_decorator(func):
            def func_wrapper(_self, val):
                if st > val:
                    raise ValueError("The {} must be < {} for function {} to work".format(Startdate, val, func.__name__))
                func(_self, val)
            return func_wrapper
        return actual_decorator


    def intInRangeDecor(func):
        def func_wrapper(value, message, l, r):
            while True:
                try:
                    data = int(input(message))
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

