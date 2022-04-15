from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from meetings.models import Meeting

def welcome(request):
    return render(request,"website/welcome.html",
        {"num_meetings": Meeting.objects.count()})

def date(request):
    return HttpResponse('This page was served at ' + str(datetime.now()))

def about(request):
    return HttpResponse('试着写个Django Project')