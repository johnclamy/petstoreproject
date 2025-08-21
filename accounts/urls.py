from django.urls import path
from .views import register_page, signin_page, logout


urlpatterns = [
    path('register', register_page, name='accounts.register_page'),
    path('signin/', signin_page, name='accounts.signin_page'),
    path('logout/', logout, name='accounts.logout'),
]
