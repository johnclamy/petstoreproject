from django.urls import path
from .views import register_page, signin_page, user_logout, orders


urlpatterns = [
    path('register', register_page, name='accounts.register_page'),
    path('signin/', signin_page, name='accounts.signin_page'),
    path('logout/', user_logout, name='accounts.user_logout'),
    path('orders/', orders, name='accounts.orders'),
]
