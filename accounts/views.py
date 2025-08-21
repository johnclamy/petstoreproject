from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    template_data['page_title'] = 'Register with Petzy to purchase a pet | Regsiter page'

    if request.method == 'GET':
        template_data['form'] = UserCreationForm()

        return render(request, 'accounts/register.html', {'data': template_data })
