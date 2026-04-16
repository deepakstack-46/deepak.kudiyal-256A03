from django.test import TestCase, Client

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import Group
from accounts.models import User
from positions.models import Position

class PositionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_group, _ = Group.objects.get_or_create(name='Administrator')
        self.member_group, _ = Group.objects.get_or_create(name='Member')

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

    def test_position_list_admin(self):
        self.client.login(username='admin@test.com', password='Test1234')
        response = self.client.get(reverse('position_list'))
        self.assertEqual(response.status_code, 200)


    def test_position_create(self):
        self.client.login(username='admin@test.com', password='Test1234')
        response = self.client.post(reverse('position_create'), {
            'position_name': 'Greeter'
        })
        self.assertEqual(response.status_code, 302)


    def test_position_delete(self):
        self.client.login(username='admin@test.com', password='Test1234')
        response = self.client.post(reverse('position_delete', args=[self.position.pk]))
        self.assertEqual(response.status_code, 302)