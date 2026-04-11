from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone\
from .models import Event, EventRegistration
from positions.models import Position

# Create your views here.
@login_required
def event_list(request):
    today = timezone.now().date()
    events = Event.objects.filter(date_end__gte=today).order_by('date_start')
    user_registrations = EventRegistration.objects.filter(user=request.user).values_list('event_id', flat=True)
    return render(request, 'events/events_list.html', {
        'events': events,
        'user_registration': user_registrations

    })

@login_required
def event_create(request):
    if not request.user.groups.filter(name='administrator').exists():
        messages.error(request, 'Yor are not authorized to view this page')
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_start = request.POST.get('date_start')
        date_end = request.POST.get('date_end')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        Event.objects.create(
            name=name,
            description=description,
            date_start=date_start,
            date_end=date_end,
            time_start=time_start,
            time_end=time_end 
        )
        messages.success(request, 'Event created successfully.')
        return redirect('event_list')
    return render(request, 'events/events_form.html')

@login_required
def event_delete(request, pk):
    if not request.user.groups.filter(name='Administrator').exists():
        
