from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Users, MeetUps, Followers, Attendees

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'user_list'
    def get_queryset(self):
        return Users.objects.all()

class UserView(generic.DetailView):
    model = Users
    template_name = 'events/user.html'

class UserViewFollowers(generic.DetailView):
    model = Users
    template_name = 'events/user/followers.html'

class UserViewFollowing(generic.DetailView):
    model = Users
    template_name = 'events/user/following.html'

class MeetUpView(generic.DetailView):
    model = MeetUps
    template_name = 'events/meetup.html'



