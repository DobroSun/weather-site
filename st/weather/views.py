from django.shortcuts import render
from django.http import HttpResponse


def weather(request):
    context = {}
    return render(request, 'weather.html', context)
