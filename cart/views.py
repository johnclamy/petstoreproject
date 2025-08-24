from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from pets.models import Pet


def add(request: HttpRequest, id: int) -> HttpResponse:
    get_object_or_404(Pet, id=id)
    cart = request.session.get('cart', {})
    
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart

    return redirect('default.home_page')
