from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return HttpResponse("Hello World")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    TODO-> Change to REST API VIEW i.e. GIVE BACK JSON RESPONSE
    """
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except (Tweet.DoesNotExist, NameError):
        raise Http404

    return HttpResponse(f"<h1>Tweet {tweet_id} - {obj.content} </h1>")
