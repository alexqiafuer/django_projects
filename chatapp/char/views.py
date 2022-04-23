from django.shortcuts import render, redirect
from char.models  import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect(f"/{room}/?username={username}")
    else:
        new = Room.objects.create(name=room)
        new.save()
        return redirect(f"/{room}/?username={username}")