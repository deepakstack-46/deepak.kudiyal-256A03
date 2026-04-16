from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Position
from  django.contrib import messages

# Create your views here.

@login_required
def position_list(request):
    if not request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')

    positions = Position.objects.all()
    return render(request, 'positions/position_list.html', {'positions': positions})

def position_create(request):
    if not request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')

    if request.method == 'POST':
        
        position_name = request.POST.get('position_name')
        
        if position_name:
            Position.objects.create(position_name=position_name)
            messages.success(request, 'Position created successfully.')

            
            return redirect('position_list')
    return render(request, 'positions/position_form.html')

@login_required
def position_update(request, pk):
    if not request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')

    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position_name = request.POST.get('position_name')
        messages.success(request, 'Position updated successfully.')


        if position_name:
            position.position_name = position_name
            position.save()
            
            return redirect('position_list')
    return render(request, 'positions/position_form.html', {'position': position})

@login_required
def position_delete(request, pk):
    if not request.user.groups.filter(name='Administrator').exists():
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')

    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        messages.success(request, 'Position deleted successfully.')
        return redirect('position_list')
    return render(request, 'positions/position_confirm_delete.html', {'position': position})