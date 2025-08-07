from django.urls import path
from .views import about_us_page, home_page


urlpatterns = [
    path('', home_page, name='default.home_page'),
    path('about-us/', about_us_page, name='default.about_us_page'),
]
