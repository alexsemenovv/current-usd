from django.db import models


class ExchangeRate(models.Model):
    """Сущность:Курс обмена"""
    rate = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)
