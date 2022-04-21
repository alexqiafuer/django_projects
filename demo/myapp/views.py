from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature

def index(request):
    features = Feature.objects.all()

    return render(request, 'index.html', {'features':features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pswd = request.POST['password']
        pswd2 = request.POST['password2']
        if pswd == pswd2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=pswd)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            # user invalid
            messages.info(request, 'Please check your username and password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    text = request.POST['text']
    word_counts = len(text.split())
    return render(request, 'counter.html', {'counts':  word_counts})

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})