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
    path('login/', views.login_view, name='login'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='myapp/login.html')),
    path('<int:pk>/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('', ClientListView.as_view(), name='ls'),

    # path('<int:id>/', views.index, name='index'),
    # path('logout/', AppointmentDetailView.as_view(), name='detail'),

    # path('create/', views.create, name='create'),
    path('create/', AppointmentCreateView.as_view(), name='create'),

    path('<int:pk>/', AppointmentUpdateView.as_view(), name='update'),

    # path('<int:id>/del', views.delete, name='delete'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='del'),

]
