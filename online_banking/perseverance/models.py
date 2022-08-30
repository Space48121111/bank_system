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
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Balance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    defaults = models.IntegerField(default=-999,999,999)

    def __str__(self):
        return self.balance
    class Meta:
        verbose_name_plural = 'Balance'
