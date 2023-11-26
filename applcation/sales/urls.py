from django.urls import path
from .views import hello_world

app_name = 'sales'

urlpatterns = [
    path('hello/', hello_world, name='upload'),
]