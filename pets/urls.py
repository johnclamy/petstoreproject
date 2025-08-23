from django.urls import path
from .views import create_review, edit_review, pet_list_page, pet_detail_page


urlpatterns = [
    path('', pet_list_page, name='pets.pet_list_page'),
    path('<int:id>/', pet_detail_page, name='pets.pet_detail_page'),
    path('<int:id>/review/create/', create_review, name='pets.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', edit_review, name='pets.edit_review'),
]
