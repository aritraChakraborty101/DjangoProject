from django.urls import path
from . import views


app_name = 'cars'

#domain.com/cars/list
urlpatterns = [
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete'),
    path('add/', views.add, name='add'),
]