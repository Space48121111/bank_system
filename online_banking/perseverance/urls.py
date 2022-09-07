from django.urls import path

from . import views

app_name = 'perseverance'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/tranx/', views.TransactionView.as_view(), name='tranx'),
    path('<int:customer_id>/transaction/', views.transaction, name='transaction'),
    path('<int:pk>/account/', views.AccountView.as_view(), name='account'),
]
