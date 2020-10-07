import validation as valid

class Address:
    __postal_code_lenght = 5

    def __init__(self, address_line = 'address_line', postal_code = 10000, country = 'country', city = 'city', fax_number = 100000, phone_number = 100000):
        self.address_line = address_line
        self.postal_code = postal_code
        self.country = country
        self.city = city
        self.fax_number = fax_number
        self.phone_number = phone_number


    def __str__(self):
        return f'\n!-----------------------!\nID- {self.ID}, \naddress line - {self.address_line} street, \npostal code - {self.postal_code}, \ncountry - {self.country}, \ncity - {self.city}, \nfax number - {self.fax_number}, \nphone number - {self.phone_number} \n!-----------------------!\n'

    def __repr__(self):
        return f'\n!-----------------------!\nID- {self.ID}, \naddress line - {self.address_line} street, \npostal code - {self.postal_code}, \ncountry - {self.country}, \ncity - {self.city}, \nfax number - {self.fax_number}, \nphone number - {self.phone_number} \n!-----------------------!\n'


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

    @property
    def strAddressWithoutId(self):
        return f'{self.address_line} {self.postal_code} {self.country} {self.city} {self.fax_number} {self.phone_number}\n'

    @property
    def strAddressWithId(self):
        return f'{self.ID} {self.strAddressWithoutId}'




    @address_line.setter
    def address_line(self, value):
        '''Set address_line'''
        self._address_line = value

    @postal_code.setter
    def postal_code(self, value):
        '''Set postal_code. checking lenght'''
        while True:
            result = valid.Validation.lenghtValue(value, self.__postal_code_lenght)
            if not result:
                self._postal_code = '00000'
                print(f'object with postal code: {value}')
                break
            result = valid.Validation.integerType(value)
            if not result:
                self._postal_code = '00000'
                print(f'object with postal code: {value}')
                break
            else:
                self._postal_code = value
                break

    @country.setter
    def country(self, value):
        '''Set country'''
        check = valid.Validation.isalphaValid(value)
        if not check:
            self._country = 'country'
        else:
            self._country = value

    @city.setter
    def city(self, value):
        '''Set city'''
        check = valid.Validation.isalphaValid(value)
        if not check:
            self._city = 'city'
        else:
            self._city = value

    @fax_number.setter
    def fax_number(self, value):
        '''Set fax_number'''
        check = valid.Validation.isdigitValid(str(value))
        if not check:
            self._fax_number = "0"
        else:
            self._fax_number = str(value)

    @phone_number.setter
    def phone_number(self, value):
        '''Set phone number'''
        check = valid.Validation.isdigitValid(value)
        if not check:
            self._phone_number = "0"
        else:
            self._phone_number = value
