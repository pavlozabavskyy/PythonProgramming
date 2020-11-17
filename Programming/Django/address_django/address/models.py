from django.db import models
from django.core.validators import RegexValidator

from .validation import Validation


class Address(models.Model):
    address_line = models.CharField(validators=[Validation.symbolValidation], 
                                max_length=50)    

    postal_code = models.CharField(validators=[RegexValidator(regex=r'^\d{5}$', 
                                message='Postal code must be contains exactly 5 digits')], 
                                max_length=5)

    country = models.CharField(validators=[Validation.symbolValidation], 
                                max_length=50)

    city = models.CharField(validators=[Validation.symbolValidation], 
                                max_length=50)

    fax_number = models.CharField(validators=[Validation.numberValidation], 
                                max_length=13)

    phone_number = models.CharField(validators=[Validation.numberValidation], 
                                max_length=13)