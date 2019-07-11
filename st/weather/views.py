from django.shortcuts import render
from django.http import HttpResponse


def archive(request):
    return render(request, 'weather/main.html', {})
