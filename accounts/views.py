from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import AccountsForm, Errors


def register_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    template_data['page_title'] = 'Register with Petzy to purchase a pet | Regsiter page'

    if request.method == 'GET':
        template_data['form'] = AccountsForm()
        return render(request, 'accounts/register.html', {'data': template_data })

    elif request.method == 'POST':
        form = AccountsForm(request.POST, error_class=Errors)

        if form.is_valid():
            form.save()
            return redirect('default.home_page')
        else:
            template_data['form'] = form
            return render(request, 'accounts/register.html', {'data': template_data })
