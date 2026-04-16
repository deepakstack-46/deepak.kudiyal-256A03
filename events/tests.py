from django.test import TestCase,  Client

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import Group
from accounts.models import User
from events.models import Event, EventRegistration
from positions.models import Position
from django.utils import timezone
from datetime import timedelta

class EventTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_group = Group.objects.create(name='Administrator')
        self.member_group = Group.objects.create(name='Member')
        self.volunteer_group = Group.objects.create(name='Volunteer')

        self.admin = User.objects.create_user(
            username='admin@test.com',
            email='admin@test.com',
            password='Test1234',
            first_name='Admin',
            last_name='Test'
        )
        self.admin.groups.add(self.admin_group)

        self.member = User.objects.create_user(
            username='member@test.com',
            email='member@test.com',
            password='Test1234',
            first_name='Member',
            last_name='Test'
        )
        self.member.groups.add(self.member_group)

        self.position = Position.objects.create(position_name='Security')

        today = timezone.now().date()
        self.event = Event.objects.create(
            name='Test Event',
            description='Test Description',
            date_start=today + timedelta(days=1),
            date_end=today + timedelta(days=2),
            time_start='09:00',
            time_end='17:00'
        )



    def test_event_create_admin(self):
        self.client.login(username='admin@test.com', password='Test1234')
        today = timezone.now().date()
        response = self.client.post(reverse('event_create'), {
            'name': 'New Event',
            'description': 'New Description',
            'date_start': today + timedelta(days=1),
            'date_end': today + timedelta(days=2),
            'time_start': '09:00',
            'time_end': '17:00'
        })
        self.assertEqual(response.status_code, 302)

    def test_event_create_member_redirect(self):
        self.client.login(username='member@test.com', password='Test1234')
        response = self.client.get(reverse('event_create'))
        self.assertEqual(response.status_code, 302)

    def test_event_register(self):
        self.client.login(username='member@test.com', password='Test1234')
        response = self.client.post(reverse('event_register', args=[self.event.pk]), {
            'position': self.position.pk
        })
        self.assertEqual(response.status_code, 302)



    def test_event_delete_admin(self):
        self.client.login(username='admin@test.com', password='Test1234')
        response = self.client.post(reverse('event_delete', args=[self.event.pk]))
        self.assertEqual(response.status_code, 302)