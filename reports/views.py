from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from accounts.models import User
from events.models import Event, EventRegistration

# Create your views here.
@login_required
def user_list(request):
    if not request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')
    users = User.objects.all().order_by('last_name', 'first_name')
    return render(request, 'reports/user_list.html', {'users': users})

@login_required
def event_upcoming(request):
    today = timezone.now().date()
    events = Event.objects.filter(date_start__gte=today).order_by('date_start')
    return render(request, 'reports/event_upcoming.html', {'events': events})

@login_required
def event_all(request):
    if not request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')
    events = Event.objects.all().order_by('date_start')
    return render(request, 'reports/event_all.html', {'events': events})

@login_required
def event_registered(request):
    if request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'Administrators do not register for events.')
        return redirect('home')
    registrations = EventRegistration.objects.filter(user=request.user).order_by('event__date_start')
    return render(request, 'reports/event_registered.html', {'registrations': registrations})

@login_required
def event_registrants(request):
    if not request.user.groups.filter(name='Administrator').exists() and not request.user.groups.filter(name='Member').exists():
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')
    today = timezone.now().date()
    filter_type = request.GET.get('filter', 'upcoming')
    if filter_type == 'current':
        events = Event.objects.filter(date_start__lte=today, date_end__gte=today).order_by('date_start')
    else:
        events = Event.objects.filter(date_start__gte=today).order_by('date_start')
    return render(request, 'reports/event_registrants.html', {
        'events': events,
        'filter_type': filter_type
    })