from django.db import models
from django.utils import timezone
from django.urls import reverse
from timezone_field import TimeZoneField

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
    time_zone = TimeZoneField(default='UTC')


    def __str__(self):
        return 'Client #{0} - {1}'.format(self.pk, self.name)
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def appt_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.timing <= now



class Appointment(models.Model):
    clientlist = models.ForeignKey(ClientList, on_delete=models.CASCADE)
    memo = models.CharField(max_length=200, blank=True)
    has_appt = models.BooleanField(default=True)
    schedule_id = models.CharField(max_length=100, blank=True, editable=False)
    timestamp = models.DateTimeField('You made appt at ', auto_now_add=True)

    def __str__(self):
        # self.appointment_set.get(pk)
        return 'Appointment #{0} - {1}'.format(self.pk, self.memo)

    def save(self, *args, **kwargs):
        if self.schedule_id:
            self.cancel()

        # override the default
        super(Appointment, self).save(*arg, **kwargs)

    def cancel(self):
        # redis
        pass







# end
