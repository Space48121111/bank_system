from django.urls import path
from . import views
from .views import (
    ClientListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
)


# app_name = 'clinicClients'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', ClientListView.as_view(), name='ls'),

    # path('create/', views.create, name='create'),
    path('create/', AppointmentCreateView.as_view(), name='create'),

    # path('<int:id>/', views.index, name='index'),
    path('<int:pk>/update/', AppointmentUpdateView.as_view(), name='update'),

    # path('<int:id>/del', views.delete, name='delete'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='del'),

]
