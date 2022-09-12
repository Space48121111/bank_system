from django.urls import path
from . import views

app_name = 'checkIn'
urlpatterns = [
    path('', views.index, name='index'),
]
