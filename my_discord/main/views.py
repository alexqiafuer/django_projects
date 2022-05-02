from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


from .models import Room, Topic, Message
from .forms import RoomForm, UserForm

def user_login(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "This user doesn't exist!")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password doesn't exist")

    context = {'page': page}
    return render(request, 'main/login_register.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    form = UserCreationForm()
    context = {'form':form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'main/login_register.html', context)

def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_news = user.message_set.all()
    topics = Topic.objects.all()
    context = {
        'user': user, 
        'rooms': rooms,
        'room_news': room_news,
        'topics': topics
    }

    return render(request, 'main/profile.html', context)

@login_required(login_url='login')
def user_update(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    context = {'form': form, 'user': user}
    
    return render(request, 'main/update_user.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_news = Message.objects.filter(Q(room__topic__name__icontains=q))


    context = {'rooms': rooms, 'topics': topics, 
               'room_count': room_count, 'room_news': room_news,
               }

    return render(request, 'main/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    rmessages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)


    context = {'room': room, 'rmessages': rmessages, 'participants':participants}

    return render(request, 'main/room.html', context)

@login_required(login_url='login')
def room_create(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host = request.user,
            topic= topic,
            name=request.POST.get('name'),
            description = request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics':topics}
    return render(request, 'main/room_form.html', context)

@login_required(login_url='login')
def room_update(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return render(request, 'main/login_register.html')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room }
    return render(request, 'main/room_form.html', context)

@login_required(login_url='login')
def room_delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'obj':room})

@login_required(login_url='login')
def message_delete(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return redirect('home')
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'obj':message})


