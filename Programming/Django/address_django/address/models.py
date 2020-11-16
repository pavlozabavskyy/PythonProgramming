from django.db import models
from django.core.validators import RegexValidator

class Address(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,15}$', 
                                message="Phone number must be entered in the format: '+123456789012'.")
    
    postal_regex = RegexValidator(regex=r'^\d{5}$', 
                                message='Postal code must be contains exactly 5 digits')

    symbol_digits_regex = RegexValidator(regex=r'', 
                                message='Dont use symbol')              #      fix it =( !!!


    address_line = models.CharField(validators=[symbol_digits_regex], max_length=50)    # fix validation  (=
    postal_code = models.CharField(validators=[postal_regex], max_length=5)
    country = models.CharField(validators=[symbol_digits_regex], max_length=50)
    city = models.CharField(validators=[symbol_digits_regex], max_length=50)
    fax_number = models.CharField(validators=[phone_regex], max_length=13)
    phone_number = models.CharField(validators=[phone_regex], max_length=13)