from django.shortcuts import render, redirect, reverse
from .forms import CityForm
from django.http import HttpResponse





def archive(request):
    form = CityForm
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(type(form.cleaned_data))
            name = form.cleaned_data['name']
            return redirect(reverse('results', kwargs={'city': name}))

    return render(request, 'weather/main.html', {'form': form})


def results(request, city):
    import requests
    s_city = city
    http = "http://api.openweathermap.org/data/2.5/find"
    my_key = '1569e3dffe0719b6eaa0ea8b58723ca7'

    res = requests.get(http, params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': my_key})
    data = res.json()

    print(data)

    city_id = data['list'][0]['id']

    print('city_id=', city_id)
    # except Exception as e:
    # print("Exception (find):", e)
    # pass


    return render(request, 'weather/forecast.html', {})