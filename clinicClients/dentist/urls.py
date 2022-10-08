from django.urls import path
from . import views

# app_name = 'clinicClients'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.index, name='index'),
    path('<int:id>/del', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]
