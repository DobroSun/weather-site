from django.shortcuts import render, redirect, reverse
from .forms import CityForm
from django.http import HttpResponse





def archive(request):
    form = CityForm
    exception = False


    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(type(form.cleaned_data))
            name = form.cleaned_data['name']
            country = form.cleaned_data['country']
            return redirect(reverse('results', kwargs={'city': name, 'country': country}))

    return render(request, 'weather/main.html', {'form': form, 'exception': exception})


def results(request, city, country):
    import requests
    s_city = city + "," + country
    http = "http://api.openweathermap.org/data/2.5/find"
    my_key = '1569e3dffe0719b6eaa0ea8b58723ca7'
    try:
        res = requests.get(http, params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': my_key})
        data = res.json()

        print(data['list'])
        dict_ = data['list'][0]

        return render(request, 'weather/forecast.html', {})
    except Exception as e:
        form = CityForm
        exception = True
        return render(request, 'weather/main.html', {'form': form, 'exception': exception})
