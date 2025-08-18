from django.urls import path
from .views import pet_list_page


urlpatterns = [
    path('', pet_list_page, name='pets.pet_list_page'),
]
