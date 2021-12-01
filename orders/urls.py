from django import urls
from django.urls import path
from. import views

urlpatterns = [
    path('add_to_cart', views.add_to_cart , name='add_to_cart'),
    path('cart', views.cart , name='cart'),
    path('delete/<int:orderdetails_id>', views.delete_from_cart , name='delete'),
]
