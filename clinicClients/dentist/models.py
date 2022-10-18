from django.db import models
from django.utils import timezone
from django.urls import reverse
from timezone_field import TimeZoneField
import datetime

# Create your models here.

class ClientList(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20, default='000-000-000')
    email = models.EmailField(max_length=200, default='example@gmail.com')
    # '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
    # default='Oct. 10, 2022, 10:00 a.m.
    # YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format
    appt_date = models.DateField(default='2023-01-01')
    timing = models.TimeField('Your appt time is ', default='10:00')
    time_zone = TimeZoneField(default='Europe/Helsinki')

    schedule_id = models.CharField(max_length=100, blank=True, editable=False)
    # default='2023-10-25 14:30:59'
    timestamp = models.DateTimeField('You made appt at ', auto_now_add=True)

    def __str__(self):
        return 'Client #{0} - {1}'.format(self.pk, self.name)
    # def get_absolute_url(self):
    #     return reverse('detail', args=[str(self.id)])
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def appt_recently(self):
        now = timezone.now()
        print('now', type(now), now)
        print('self.appt_date', self.appt_date)
        return now <= self.appt_date <= now + datetime.timedelta(days=5)

    def save(self, *args, **kwargs):
        if self.schedule_id:
            self.cancel()

        # override the default
        super(ClientList, self).save(*args, **kwargs)

    def cancel(self):
        # redis
        pass


class Account(models.Model):
    clientlist = models.ForeignKey(ClientList, on_delete=models.CASCADE)
    password = models.CharField(max_length=200, blank=True)
    has_appt = models.BooleanField(default=True)

    def __str__(self):
        # self.appointment_set.get(pk)
        return 'Appointment #{0} - {1}'.format(self.pk, self.memo)








# end
