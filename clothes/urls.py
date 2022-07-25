from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('clients/', clients, name='clients'),
    path('clients/<int:id>/update/', editClient, name='edit'),
    path('clients/<int:id>/delete/', clientDelete, name='delete'),


]