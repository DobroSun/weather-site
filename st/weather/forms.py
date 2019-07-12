from .models import City
from django import forms



class CityForm(forms.ModelForm):

    class Meta():
        model = City
        fields = ('name', 'country',)
