from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST['text']
    word_counts = len(text.split())
    return render(request, 'counter.html', {'counts':  word_counts})