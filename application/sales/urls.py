from django.urls import path
from .views import hello_world, upload_file

app_name = 'sales'

urlpatterns = [
    path('hello/', hello_world, name='hello'),
    path('upload/', upload_file, name='upload'),
]