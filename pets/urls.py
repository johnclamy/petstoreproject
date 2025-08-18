from django.urls import path
from .views import pet_list_page, pet_detail_page


urlpatterns = [
    path('', pet_list_page, name='pets.pet_list_page'),
    path('<int:id>/', pet_detail_page, name='pets.pet_detail_page'),
]
