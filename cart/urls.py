from django.urls import path
from .views import add, clear, cart_home_page, purchase


urlpatterns = [
    path('', cart_home_page, name='cart.cart_home_page'),
    path('<int:id>/add/', add, name='cart.add'),
    path('clear/', clear, name='cart.clear'),
    path('purchase/', purchase, name='cart.purchase'),
]
