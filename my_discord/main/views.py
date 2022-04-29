from django.shortcuts import render, redirect

from .models import Room
from .forms import RoomForm
# rooms = [
#     {'id': 1, 'name':"Lets's"},
#     {'id': 2, 'name':"Lets's do"},
#     {'id': 3, 'name':"Lets's do python"},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}

    return render(request, 'main/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'main/room.html', context)

def room_create(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'main/room_form.html', context)

def room_update(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(('home'))

    context = {'form': form}
    return render(request, 'main/room_form.html', context)

def room_delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'obj':room})