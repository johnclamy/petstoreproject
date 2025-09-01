from django.urls import path
from .views import post_list_page, post_detail_page


app_name = 'blog'


urlpatterns = [
    path('', post_list_page, name='blog.post.post_list_page'),
    path('<int:id>/', post_detail_page, name='blog.post.post_detail_page'),
]
