from django.urls import path
from . import views
from .views import (
    ClientListView,
    AppointmentDetailView,
    AppointmentCreateView,
    AppointmentUpdateView,
    AppointmentDeleteView,
)
from django.contrib.auth import views as auth_views

# app_name = 'clinicClients'
urlpatterns = [
    # path('<int:pk>/login/', views.login_view, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Registration/login.html')),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('user/', views.get_user, name='user'),

    # clientlist_list.html
    path('', ClientListView.as_view(), name='ls'),
    # clientlist_form.html
    path('<int:pk>/', AppointmentDetailView.as_view(), name='detail'),

    # clientlist_form.html
    path('create/', AppointmentCreateView.as_view(), name='create'),
    path('<int:pk>/update/', AppointmentUpdateView.as_view(), name='update'),
    path('<int:pk>/del/', AppointmentDeleteView.as_view(), name='del'),

    # path('', views.home, name='home'),
    # path('<int:id>/', views.index, name='index'),
    # path('create/', views.create, name='create'),
    # path('<int:id>/del', views.delete, name='delete'),

]
