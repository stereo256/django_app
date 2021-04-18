from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    data = Friend.objects.all().values()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)