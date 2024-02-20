from django.urls import path
from . import views

app_name = 'object_detection'
urlpatterns = [
    path('detect/', views.detect_objects, name='detect_objects'),
]