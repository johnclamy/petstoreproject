from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
            return redirect('accounts.signin_page')
        else:
            template_data['form'] = form
            return render(request, 'accounts/register.html', {'data': template_data })
        

def signin_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    template_data['page_title'] = 'Sign in to Petzy and purchase a pet | Sign in page'

    if request.method == 'GET':
        return render(request, 'accounts/signin.html', {'data': template_data})

    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )

        if user is None:
            template_data['error'] = 'Incorrect username or password.'
            return render(request, 'accounts/signin.html', {'data': template_data})
        else:
            login(request, user)
            return redirect('default.home_page')


@login_required
def user_logout(request):
    logout(request)
    return redirect('default.home_page')


@login_required
def orders(request: HttpRequest) -> HttpResponse:
    template_data = {}
    template_data['page_title'] = 'Your orders breakdown | Orders page'
    template_data['orders'] = request.user.order_set.all()

    return render(request, 'accounts/orders.html', {'data': template_data})
