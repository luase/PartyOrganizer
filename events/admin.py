from django.contrib import admin
from .models import Users, Followers, MeetUps, Attendees
# Register your models here.

admin.site.register(Users)
admin.site.register(Followers)
admin.site.register(MeetUps)
admin.site.register(Attendees)