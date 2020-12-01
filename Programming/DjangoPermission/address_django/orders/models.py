from django.db import models
from django.contrib.auth.models import User


class Orders(models.Model):
    """
    Orders model.
    """
    user = models.ForeignKey(User, verbose_name='User ', 
                                on_delete=models.CASCADE)


    date = models.DateTimeField(verbose_name=('date'))

    item_id = models.PositiveIntegerField()


    """
    user_id
    item_id
    amount
    date
    """