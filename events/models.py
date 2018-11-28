from django.db import models
from django.utils import timezone

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class Followers(models.Model):
    # User a is followed by user b
    class Meta:
        unique_together = (('user_a', 'user_b'),)
    user_a = models.ForeignKey(Users, models.CASCADE, related_name='is_followed')
    user_b = models.ForeignKey(Users, models.CASCADE, related_name='follows')
    def __str__(self):
        return self.user_a.first_name + " <- " + self.user_b.first_name

class MeetUps(models.Model):
    user_creator = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='events_created')
    created_date = timezone.now()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    mu_date = models.DateTimeField('event date')
    def __str__(self):
        return self.name

class Attendees(models.Model):
    # The user is going to this event.
    class Meta:
        unique_together = (('meetup_going', 'user_going'))
    meetup_going = models.ForeignKey(MeetUps, on_delete=models.CASCADE, related_name='attendees')
    user_going = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='going_to')
    def __str__(self):
        return self.meetup_going.name + " <- " + self.user_going.first_name