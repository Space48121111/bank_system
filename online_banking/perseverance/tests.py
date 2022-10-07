from django.test import TestCase

# Create your tests here.

from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Room

# Create your tests here.
'''
class RoomModelTests(TestCase):
    def test_was_published_recently_with_future_room(self):
        # for testing the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_room = Room(pub_date=time)

        self.assertIs(future_room.was_published_recently(), False)

    def test_was_published_recently_with_old_room(self):
        # over one day (one day and one second)
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_room = Room(pub_date=time)
        self.assertIs(old_room.was_published_rencently(), False)

    def test_was_published_recently_with_recent_question(self):
        # less than one day - goes back in time
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_room = Room(pub_date=time)
        self.assertIs(recent_room.was_published_recently(), True)

def create_room(room_text, days):
    time = timezone.now() + datetime.timedelta(days=days):
    return Room.objects.create(room_text=room.text, pub_date=time)

# tell a story of admin input and user exp on each state of change
class RoomIndexViewTests(TestCase):
    def test_no_room(self):
        response = self.client.get(reverse('task:index'))
        self.assertEqual(response, status_code, 200)
        self.assertContains(response, 'No task are available.')
        # verify the list is empty
        self.assertQuerysetEqual(response.context['latest_room_list'], [])
    def test_past_room(self):
        room = create_room(room_text = 'Past room.', days=-38)
        response = self.client.get(reverse('task:index'))
        self.assertQuerySetEqual(response.context['latest_room_list'], [room],)
    def test_future_room(self):
        create_room(room_text='Future room', days=30)
        response = self.client.get(reverse('task:index'))
        # database reset after each test method
        self.assertContains(response, 'No task are available.')
        self.assertQuerysetEqual(response.context['latest_room_list'], [])
    def test_future_room_and_past_room(self):
        room=create_room(room_text='Past room.', days=-30)
        create_room(room_text='Future room.', days=30)
        response=self.client.get(reverse('task:index'))
        self.assertQuerysetEqual(response.context['latest_room_list'], [room],)
    def test_two_past_rooms(self):
        room1 = create_room(room_text='Past room 1.', days=-30)
        room2 = create_room(room_text='Past room 2.', days=-5)
        response = self.client.get(reverse('task:index'))
        self.assertQuerysetEqual(response.context['latest_room_list'], [room2, room1],)

class RoomDetailViewTests(TestCase):
    def test_future_room(self):
        future_room = create_room(room_text='Future room.', days=5)
        url = reverse('task:detail', args=(future_room.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_past_question(self):
        past_room = create_room(room_text='Past room', days=-5)
        url = reverse('task:detail', args=(past_room.id,))
        response = self.client.get(url)
        self.assertContains(resonse.past_room.room_text)
'''












# end
