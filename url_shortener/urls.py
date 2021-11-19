from django.urls import path
from . import views

urlpatterns = [
    path('<str:uuid1>/', views.get_url),
]
