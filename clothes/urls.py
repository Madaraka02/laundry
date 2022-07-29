from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('clients/<int:id>/receipt/', receipt, name='receipt'),
    path('clients/', clients, name='clients'),
    path('clients/<int:id>/update/', editClient, name='edit'),
    path('clients/<int:id>/delete/', clientDelete, name='delete'),
    path('access/token/', getAccessToken, name='get_mpesa_access_token'),
    path('clients/<int:id>/online/lipa/', lipa_na_mpesa_online, name='lipa_na_mpesa'),

    #     # register, confirmation, validation and callback urls
    # path('payment/register', register_urls, name="register_mpesa_validation"),
    # path('payment/confirmation', confirmation, name="confirmation"),
    # path('payment/validation', validation, name="validation"),
    # path('payment/callback', call_back, name="call_back"),


]