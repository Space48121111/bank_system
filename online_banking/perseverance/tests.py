from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Customer, Balance

# Create your tests here.

class customerModelTests(TestCase):
    def test_was_published_recently_with_future_customer(self):
        # for testing the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_customer = customer(pub_date=time)

        self.assertIs(future_customer.was_published_recently(), False)

    def test_was_published_recently_with_old_customer(self):
        # over one day (one day and one second)
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_customer = customer(pub_date=time)
        self.assertIs(old_customer.was_published_rencently(), False)

    def test_was_published_recently_with_recent_question(self):
        # less than one day - goes back in time
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_customer = customer(pub_date=time)
        self.assertIs(recent_customer.was_published_recently(), True)

def create_customer(customer_text, days):
    time = timezone.now() + datetime.timedelta(days=days):
    return customer.objects.create(customer_text=customer.text, pub_date=time)

# tell a story of admin input and user exp on each state of change
class customerIndexViewTests(TestCase):
    def test_no_customer(self):
        response = self.client.get(reverse('task:index'))
        self.assertEqual(response, status_code, 200)
        self.assertContains(response, 'No task are available.')
        # verify the list is empty
        self.assertQuerysetEqual(response.context['latest_customer_list'], [])
    def test_past_customer(self):
        customer = create_customer(customer_text = 'Past customer.', days=-38)
        response = self.client.get(reverse('task:index'))
        self.assertQuerySetEqual(response.context['latest_customer_list'], [customer],)
    def test_future_customer(self):
        create_customer(customer_text='Future customer', days=30)
        response = self.client.get(reverse('task:index'))
        # database reset after each test method
        self.assertContains(response, 'No task are available.')
        self.assertQuerysetEqual(response.context['latest_customer_list'], [])
    def test_future_customer_and_past_customer(self):
        customer=create_customer(customer_text='Past customer.', days=-30)
        create_customer(customer_text='Future customer.', days=30)
        response=self.client.get(reverse('task:index'))
        self.assertQuerysetEqual(response.context['latest_customer_list'], [customer],)
    def test_two_past_customers(self):
        customer1 = create_customer(customer_text='Past customer 1.', days=-30)
        customer2 = create_customer(customer_text='Past customer 2.', days=-5)
        response = self.client.get(reverse('task:index'))
        self.assertQuerysetEqual(response.context['latest_customer_list'], [customer2, customer1],)

class customerDetailViewTests(TestCase):
    def test_future_customer(self):
        future_customer = create_customer(customer_text='Future customer.', days=5)
        url = reverse('task:detail', args=(future_customer.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_past_question(self):
        past_customer = create_customer(customer_text='Past customer', days=-5)
        url = reverse('task:detail', args=(past_customer.id,))
        response = self.client.get(url)
        self.assertContains(resonse.past_customer.customer_text)













# end
