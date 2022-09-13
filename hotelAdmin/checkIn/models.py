from django.db import models

# Create your models here.

class GuestList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Guest(models.Model):
    guestlist = models.ForeignKey(GuestList, on_delete=models.CASCADE)
    guest = models.CharField(max_length=200)
    checkedIn = models.BooleanField()
    def __str__(self):
        return self.guest
