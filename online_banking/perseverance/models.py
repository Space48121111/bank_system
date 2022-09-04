import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    customer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Doing business with us since ')

    def __str__(self):
        return self.customer_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Deposited recently',
    )
    def deposited_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.pub_date <= now

class Balance(models.Model):
    # create balance_set using foreignkey
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance_text = models.CharField(max_length=200)
    # defaults = models.DecimalField(max_digits=19,
    # decimal_places=9, default=-999999999.999999999)
    defaults = models.FloatField(default=-999999999.999999999)

    def __str__(self):
        return self.balance_text, self.defaults
    class Meta:
        verbose_name_plural = 'Balance'

# end
