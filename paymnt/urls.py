from django.urls import path
from .views import  *

urlpatterns = [
    path('product/', get_product, name='get_product'),
    path('create-payment-intent/', create_payment_intent, name='create_payment_intent'),
    path('confirm-payment/', confirm_payment, name='confirm_payment'),
    path('payment', product_page, name='payment'),
    path('',home,name="name"),
    path('success',succes, name="succes"),
    path('debug-host/',debug_host, name='debug_host'),  # new debug route
]
