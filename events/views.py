from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Event, EventRegistration
from positions.models import Position

# Create your views here.
@login_required
def event_list(request):
    today = timezone.now().date()
    events = Event.objects.filter(date_end__gte=today).order_by('date_start')
    user_registrations = EventRegistration.objects.filter(user=request.user).values_list('event_id', flat=True)
    return render(request, 'events/event_list.html', {
        'events': events,
        'user_registrations': user_registrations

    })

@login_required
def event_create(request):
    if not request.user.groups.filter(name='Administrator').exists():
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
    return render(request, 'events/event_form.html')

@login_required
def event_update(request, pk):
    if not request.user.groups.filter(name='Administrator').exists() and not request.user.groups.filter(name='Member').exists():
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.date_start = request.POST.get('date_start')
        event.date_end = request.POST.get('date_end')
        event.time_start = request.POST.get('time_start')
        event.time_end = request.POST.get('time_end')
        event.save()
        messages.success(request, 'Event updated successfully.')
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'event': event})

@login_required
def event_delete(request, pk):
    if not request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'You are not authorized to view this page')
        return redirect('home')
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully')
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

@login_required
def event_register(request, pk):
    if request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'Administrator cannot register for events.') 
        return redirect('event_list')
    event = get_object_or_404(Event, pk=pk)
    positions = Position.objects.all().order_by('position_name')
    if request.method == 'POST':
        position_id = request.POST.get('position')
        position = get_object_or_404(Position, pk=position_id)
        if EventRegistration.objects.filter(user=request.user, event=event).exists():
            messages.error(request, 'You are already registered for this event.')
            return redirect('event_list')
        EventRegistration.objects.create(user=request.user, event=event, position=position)
        messages.success(request, 'You have successfully registered for this event.')
        return redirect('event_list')
    return render(request, 'events/event_register.html', {'event': event, 'positions': positions})

@login_required
def event_unregister(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        EventRegistration.objects.filter(user=request.user, event=event).delete()
        messages.success(request, 'You have successfully unregistered from this event.')
        return redirect('event_list')
    return render(request, 'events/event_confirm_unregister.html', {'event': event})   
