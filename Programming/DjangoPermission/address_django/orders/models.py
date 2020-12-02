from django.db import models
from django.contrib.auth.models import User
import address


class Orders(models.Model):
    """
    Orders model.
    """
    user = models.ForeignKey(User, verbose_name='User ', on_delete=models.CASCADE)

    item = models.ForeignKey('address.Address', verbose_name='address', on_delete=models.CASCADE)

    amount = models.PositiveIntegerField(default=1)

    date = models.DateTimeField(verbose_name=('date'), auto_now_add=True)
