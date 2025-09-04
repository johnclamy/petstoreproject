from django.urls import path
from .views import post_list_page, post_detail_page


app_name = 'blog'


urlpatterns = [
    path('post/', post_list_page, name='post_list_page'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail_page, name='post_detail_page'),
]
