from django.shortcuts import render
from .forms import CityForm
from django.http import HttpResponse


def archive(request):
    form = CityForm
    return render(request, 'weather/main.html', {'form': form})
