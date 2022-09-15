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
    # defaults = models.FloatField(default=-999999999.999999999)
    defaults = models.DecimalField(max_digits=20, decimal_places=2, default=1000.00)
    timestamp = models.DateTimeField('Transaction timestamp ')


    def __str__(self):
        return self.balance_text

    class Meta:
        verbose_name_plural = 'Balance'

'''
class AbstractBalance(models.Model):
    # create balance_set using foreignkey
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance_text = models.CharField(max_length=200)
    defaults = models.FloatField(default=-999999999.999999999)

    class Meta:
        abstract = True

class Balance(AbstractBalance):
    def __str__(self):
        return self.balance_text

    def save(self):
        history = super(Balance, self).save()
        print(history)
        BalanceHistory.objects.create(
            history = history,
            balance_text = history.balance_text,
            defaults = history.defaults,
        )
    class Meta:
        verbose_name_plural = 'Balance'

class BalanceHistory(AbstractBalance):
    history = models.ForeignKey(Balance, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['pk']
'''

class Income(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    revenue_expense = models.CharField(max_length=200)
    product = models.FloatField(default=-1000.00)

    def __str__(self):
        return self.revenue_expense
    class Meta:
        verbose_name_plural = 'Income'









# end
