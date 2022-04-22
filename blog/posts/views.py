from django.shortcuts import render, get_object_or_404

from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    post = get_object_or_404(Posts, id=pk)
    return render(request, 'post.html', {'post':post})