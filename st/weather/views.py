from django.shortcuts import render
from django.http import HttpResponse


def weather(request):
    return render(request, 'weather.html', {})
