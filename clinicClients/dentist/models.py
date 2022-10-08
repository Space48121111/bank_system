from django.db import models

# Create your models here.

class ClientList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Client(models.Model):
    Clientlist = models.ForeignKey(ClientList, on_delete=models.CASCADE)
    memo = models.CharField(max_length=200, blank=True)
    has_appointment = models.BooleanField(null=True)
    def __str__(self):
        return self.memo
