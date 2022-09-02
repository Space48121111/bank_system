from django.urls import path

from . import views

app_name = 'perseverance'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/balance/', views.transaction, name='balance'),
    path('<int:pk>/account/', views.AccountView.as_view(), name='account'),
]
