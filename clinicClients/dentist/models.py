from django.db import models
from django.utils import timezone

# Create your models here.

class ClientList(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20, default='000-000-000')
    # '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
    # YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format
    # timing = models.DateTimeField('Your appt time is ', default='2022-10-25 10:00')
    timing = models.DateTimeField('Your appt time is ', auto_now_add=True)


    def __str__(self):
        return 'Client #{0} - {1}'.format(self.pk, self.name)

    def appt_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.timing <= now


class Appointment(models.Model):
    clientlist = models.ForeignKey(ClientList, on_delete=models.CASCADE)
    memo = models.CharField(max_length=200, blank=True)
    has_appt = models.BooleanField(null=True)

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
