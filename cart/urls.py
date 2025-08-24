from django.urls import path
from .views import add


urlpatterns = [
    path('<int:id>/add/', add, name='cart.add'),
]
