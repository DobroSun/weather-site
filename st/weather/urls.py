from django.urls import path

from . import views

urlpatterns = [
            path('', views.archive, name='archive'),
            path('<str:city>/<str:country>/results/', views.results, name='results'),]