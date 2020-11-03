from decorator import *
import json

class Address:
    def __init__(self, address_line = 'addressline', postal_code = 10000, country = 'country', city = 'city', fax_number = '+380979088267', phone_number = '+380979088267'):
        self.address_line = address_line
        self.postal_code = postal_code
        self.country = country
        self.city = city
        self.fax_number = fax_number
        self.phone_number = phone_number

    def __str__(self):
        result = '\n!-------------------------!'
        for i in self.getAttr():
            result += '\n'+ str(i)+ ' - ' + str(getattr(self, str(i)))
        result += '\n!-------------------------!'
        return result

    def __repr__(self):
        return self.__str__()

    def jsonFormat(self):
        data = {}
        attr = self.getAttr()
        attr.remove('ID')
        for i in attr:
            data[i.replace('_Address__', '')] = getattr(self, i)
        return json.dumps(data, indent = 8)

    @property
    def address_line(self):
        return self._address_line

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def country(self):
        return self._country

    @property
    def city(self):
        return self._city

    @property
    def fax_number(self):
        return self._fax_number

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def ID(self):
        return id(self)

    def getAttr(self):
        return [name for name, value in vars(Address).items() if isinstance(value, property)]

    def strAddressWithoutId(self):
        result = ''
        for i in self.getAttr():
            result += str(getattr(self, str(i))) + ' '
        return result

    def strAddressWithId(self):
        return f'{self.ID} {self.strAddressWithoutId}'

    @address_line.setter
    @check_str
    @check_symbol
    def address_line(self, value):
        '''Set address_line. type, symbol'''
        self._address_line = value

    @postal_code.setter
    @check_int
    @check_lenght_Value(lenght = 5)
    def postal_code(self, value):
        '''Set postal_code. lenght, type'''
        self._postal_code = value

    @country.setter
    @check_str
    @check_symbol
    def country(self, value):
        '''Set country. type, symbol'''
        self._country = value

    @city.setter
    @check_str
    @check_symbol
    def city(self, value):
        '''Set city. type, symbol'''
        self._city = value

    @fax_number.setter
    @check_str
    @check_phone_number
    def fax_number(self, value):
        '''Set fax_number. type, symbol and +380'''
        self._fax_number = value

    @phone_number.setter
    @check_str
    @check_phone_number
    def phone_number(self, value):
        '''Set phone number. type, symbol and +380'''
        self._phone_number = value
