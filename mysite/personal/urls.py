from django.conf.urls import re_path
from django.urls import path
from django.urls import include
from django.views.generic import ListView, DetailView
from personal.models import User
from . import views

urlpatterns = [
    re_path(r'^RecentUsers$',ListView.as_view(queryset=User.objects.all().order_by("-DateJoined")[:10],
                                              template_name="personal/RecentUsers.html"))
    re_path(r'^Settings$', views.settings, name='settings'),
    re_path(r'^signup$', views.signup, name="signup"),
    re_path(r'^', views.index, name='index'),
]
