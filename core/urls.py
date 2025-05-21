from django.urls import path
from . import views

urlpatterns = [
    path('disasters/', views.disaster_list, name='disaster_list'),
]
