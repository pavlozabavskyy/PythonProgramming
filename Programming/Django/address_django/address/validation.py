from django.core.exceptions import ValidationError 
import re


class Validation:
    """ Class Validation """
    def numberValidation(value: str):
        """ Validation phone-fax number """
        if len(value) == 13 and value[0:4] == '+380' and value[4:].isdigit():
            return value
        else: 
            raise ValidationError("The lenght of value should be 13. Contain only digits. And start with '+380'. ")

    def symbolValidation(value: str):
        """ Validation str value """
        if re.search(r'[^A-Za-z .]', value) == None:
            return value
        else:
            raise ValidationError("Value must contain only letters ")
    
