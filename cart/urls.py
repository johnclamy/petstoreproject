from django.urls import path
from .views import add, cart_home_page


urlpatterns = [
    path('', cart_home_page, name='cart.cart_home_page'),
    path('<int:id>/add/', add, name='cart.add'),
]
