from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<str:uuid1>/', views.get_url),
]
