from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('events/upcoming/', views.event_upcoming, name='event_upcoming'),
    path('events/all/', views.event_all, name='event_all'),
    path('events/registered/', views.event_registered, name='event_registered'),
    path('events/registrants/', views.event_registrants, name='event_registrants'),
]