from validation import Validation as v

class Address:

    def __init__(self, address_line = 'address_line', postal_code = 10000, country = 'country', city = 'city', fax_number = '+3800', phone_number = '+3800'):
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
    def address_line(self, value):
        '''Set address_line. type, symbol'''
        try:
            value = v.symbolValidate(value, 'Address line')
        except Exception as e:
            print(e)
            value = 'None'
        self._address_line = value


    @postal_code.setter
    def postal_code(self, value):
        '''Set postal_code. lenght, type'''
        try:
            value = v.intValidate(value, 'Postal code')
            value = v.lenghtValueValidate(value, 5, 'Postal code')
        except Exception as e:
            print(e)
            value = 0
        self._postal_code = value



    @country.setter
    def country(self, value):
        '''Set country. type, symbol'''
        try:
            value = v.symbolValidate(value, 'Country')
        except Exception as e:
            print(e)
            value = 'None'
        self._country = value


    @city.setter
    def city(self, value):
        '''Set city. type, symbol'''
        try:
            value = v.symbolValidate(value, 'City')
        except Exception as e:
            print(e)
            value = 'None'
        self._city = value


    @fax_number.setter
    def fax_number(self, value):
        '''Set fax_number. type, symbol and +380'''
        try:
            value = v.numberValidate(value, 'fax_number')
        except Exception as e:
            print(e)
            value = 'None'
        self._fax_number = value


    @phone_number.setter
    def phone_number(self, value):
        '''Set phone number. type, symbol and +380'''
        try:
            value = v.numberValidate(value, 'phone_number')
        except Exception as e:
            print(e)
            value = 'None'
        self._phone_number = value
