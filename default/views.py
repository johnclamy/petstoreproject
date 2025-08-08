from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    template_data['page_title'] = 'Welcome to Petzy Pet Store where you can find the pup of your dreams! | Home'

    return render(request, 'default/index.html', {'data': template_data})


def about_us_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    template_data['page_title'] = 'Find out all about our company and how we got here! | About Us'

    return render(request, 'default/about-us.html', {'data': template_data})
