from django.urls import path
from . import views

urlpatterns = [
    path('upcycle/', views.upcycle, name='upcycle')
]
