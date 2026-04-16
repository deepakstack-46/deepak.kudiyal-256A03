from django.test import TestCase, Client

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import Group
from accounts.models import User

class AccountTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.member_group = Group.objects.create(name='Member')
        self.admin_group = Group.objects.create(name='Administrator')
        self.volunteer_group = Group.objects.create(name='Volunteer')

        self.member = User.objects.create_user(
            username='test@test.com',
            email='test@test.com',
            password='Test1234',
            first_name='Test',
            last_name='User',
            phone='1234567890'
        )
        self.member.groups.add(self.member_group)

    def test_register_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_valid_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'test@test.com',
            'password': 'Test1234'
        })
        self.assertEqual(response.status_code, 302)



    def test_register_new_user(self):
        response = self.client.post(reverse('register'), {
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@test.com',
            'phone': '9876543210',
            'role': 'Member',
            'password1': 'Test1234',
            'password2': 'Test1234'
        })
        
        self.assertEqual(response.status_code, 302)