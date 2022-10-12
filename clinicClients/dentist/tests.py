from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import ClientList, Appointment

# Create your tests here.

class ClientListModelTests(TestCase):
    def test_appt_recently_with_future_appt(self):
        # future appt -> validate
        time = timezone.now() + datetime.timedelta(days=3)
        future_appt = ClientList(appt_date=time)
        print(time, future_appt)

        self.assertIs(future_appt.appt_recently(), True)

    def test_appt_recently_with_old_appt(self):
        # past over one day (one day and one second) -> invalidate
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_appt = appt(appt_date=time)
        self.assertIs(old_appt.appt_rencently(), False)

    def test_appt_recently_with_recent_sch(self):
        # past less than one day - goes back in time -> invalidate
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_appt = appt(appt_date=time)
        self.assertIs(recent_appt.appt_recently(), False)

def create_client(client_name, days):
    time = timezone.now() + datetime.timedelta(days=days)
    print('time', time)
    return ClientList.objects.create(client_name=ClientList.name, days=time)


# tell a story of admin input and user exp on each state of change
class AppointmentIndexViewTests(TestCase):
    def test_no_appt(self):
        response = self.client.get(reverse('task:index'))
        self.assertEqual(response, status_code, 200)
        self.assertContains(response, 'No task are available.')
        # verify the list is empty
        self.assertQuerysetEqual(response.context['latest_appt_list'], [])
    def test_past_appt(self):
        appt = create_appt(appt_text = 'Past appt.', days=-38)
        response = self.client.get(reverse('task:index'))
        self.assertQuerySetEqual(response.context['latest_appt_list'], [appt],)
    def test_future_appt(self):
        create_appt(appt_text='Future appt', days=30)
        response = self.client.get(reverse('task:index'))
        # database reset after each test method
        self.assertContains(response, 'No task are available.')
        self.assertQuerysetEqual(response.context['latest_appt_list'], [])
    def test_future_appt_and_past_appt(self):
        appt=create_appt(appt_text='Past appt.', days=-30)
        create_appt(appt_text='Future appt.', days=30)
        response=self.client.get(reverse('task:index'))
        self.assertQuerysetEqual(response.context['latest_appt_list'], [appt],)
    def test_two_past_appts(self):
        appt1 = create_appt(appt_text='Past appt 1.', days=-30)
        appt2 = create_appt(appt_text='Past appt 2.', days=-5)
        response = self.client.get(reverse('task:index'))
        self.assertQuerysetEqual(response.context['latest_appt_list'], [appt2, appt1],)

class ClientListDetailViewTests(TestCase):
    def test_future_appt(self):
        future_appt = create_appt(appt_text='Future appt.', days=5)
        url = reverse('task:detail', args=(future_appt.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_past_question(self):
        past_appt = create_appt(appt_text='Past appt', days=-5)
        url = reverse('task:detail', args=(past_appt.id,))
        response = self.client.get(url)
        self.assertContains(resonse.past_appt.appt_text)













# end
