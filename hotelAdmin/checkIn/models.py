from django.db import models

# Create your models here.

class GuestList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Guest(models.Model):
    guestlist = models.ForeignKey(GuestList, on_delete=models.CASCADE)
    memo = models.TextField(blank=True)
    checkedIn = models.BooleanField(null=True)
    made_on = models.DateField(default='2023-01-01')
    def __str__(self):
        return self.memo
