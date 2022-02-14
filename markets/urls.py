from django.urls import path
from . import views

urlpatterns = [
    path('markets/', views.markets, name='markets')
]
