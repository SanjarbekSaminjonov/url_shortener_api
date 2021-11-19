from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<str:uuid>/', views.get_long_url, name='get_link'),
]
