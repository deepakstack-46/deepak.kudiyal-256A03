from django.db import models
from accounts.models import User
from positions.models import Position
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    volunteers = models.ManyToManyField(User, through='EventRegistration', blank=True)
    position = models.ManyToManyField(Position, blank=True)

    def __str__(self):
        return self.name
    
class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


