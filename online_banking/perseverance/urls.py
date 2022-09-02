from django.urls import path

from . import views

app_name = 'perseverance'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:customer_id>/transaction/', views.transaction, name='transaction'),
    path('<int:pk>/account/', views.AccountView.as_view(), name='account'),
]
