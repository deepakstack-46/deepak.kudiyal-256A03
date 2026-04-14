from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from accounts.models import User
from positions.models import Position
from events.models import Event, EventRegistration
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle (self, *args, **kwargs):
        self.stdout.write('Clearing existing data....')
        EventRegistration.objects.all().delete()
        Event.objects.all().delete()
        Position.objects.all().delete()
        User.objects.all().delete()
        Group.objects.all().delete()

        self.stdout.write('Creating Groups...')
        admin_group, _ = Group.objects.get_or_create(name='Administrator')
        member_group, _ = Group.objects.get_or_create(name='Member')
        volunteer_group, _= Group.objects.get_or_create(name='Volunteer')

        self.stdout.write('Creating Position...')
        positions = ['Security', 'Greeter', 'Cook', 'Swamper', 'Setup', 'Tear Down', 'Server']
        for p in positions:
            Position.objects.create(position_name=p)

        self.stdout.write('Creating users...')
        admin = User.objects.create_superuser(
            username='admin@admin.com',
            email='admin@admin.com',
            password='Pa55worD',
            first_name='Admin',
            last_name='User'
        )
        admin.groups.add(admin_group)

        member1 = User.objects.create_user(
            username='a@b.ca',
            email='a@b.ca',
            password='Pa55worD',
            first_name='Member',
            last_name='One',
            phone='1234567890'
        )
        member1.groups.add(member_group)

        member2 = User.objects.create_user(
            username='b@b.ca',
            email='b@b.ca',
            password='Pa55worD',
            first_name='Member',
            last_name='Two',
            phone='1234567890'
            )
        member2.groups.add(member_group)

        vol1 = User.objects.create_user(
            username='vol1@b.ca',
            email='vol1@b.ca',
            password='Pa55worD',
            first_name='Volunteer',
            last_name='One',
            phone='1234567890'
        )
        vol1.groups.add(volunteer_group)

        vol2 = User.objects.create_user(
            username='vol2@b.ca',
            email='vol2@b.ca',
            password='Pa55worD',
            first_name='Volunteer',
            last_name='Two',
            phone='1234567890'
        )
        vol2.groups.add(volunteer_group)
        
        self.stdout.write('Creating events....')
        today = timezone.now().date()

        Event.objects.create(
            name='Past Event',
            description='This event has already happened.',
            date_start=today - timedelta(days=5),
            date_end=today - timedelta(days=3),
            time_start='09:00',
            time_end='17:00'

        )

        Event.objects.create(
            name='Current Event',
            description='This event is happening now.',
            date_start=today - timedelta(days=1),
            date_end=today + timedelta(days=1),
            time_start='09:00',
            time_end='17:00'
        )

        Event.objects.create(
            name='Today Event',
            description='This event starts later today.',
            date_start=today,
            date_end=today,
            time_start='18:00',
            time_end='22:00'
        )

        Event.objects.create(
            name='Future Event 1',
            description='This event is coming up soon.',
            date_start=today + timedelta(days=3),
            date_end=today + timedelta(days=4),
            time_start='09:00',
            time_end='17:00'
        )

        Event.objects.create(
            name='Future Event 2',
            description='This event is also coming up soon.',
            date_start=today + timedelta(days=5),
            date_end=today + timedelta(days=6),
            time_start='09:00',
            time_end='17:00'
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
