from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import TweetForm
from .models import Tweet

def welcome_view(request, *args, **kwargs ):
    return render(request, 'tweets/home.html')

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    #print('Ajax is ', request.headers.get('X-Requested-With'))
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse(obj.serialize(), status=201) # create items
        if next_url and url_has_allowed_host_and_scheme(next_url, '127.0.0.1'):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context = {'form':form})



def tweet_list_view(request, *args, **kwargs):
    qset = Tweet.objects.all()
    data = {
        'isUser': False,
        "response": [x.serialize() for x in qset]
    }

    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs ):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "404 Not fount"
        status = 404
    
    return JsonResponse(data=data, status=status)