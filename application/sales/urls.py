from django.urls import path
from .views import upload_file

app_name = 'sales'

urlpatterns = [
    path('upload/', upload_file, name='upload'),
]