from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from pets.models import Pet
from .utils import calculate_cart_total


def cart_home_page(request: HttpRequest) -> HttpResponse:
    template_data = {}
    pets_in_cart = []
    cart_total = 0
    cart = request.session.get('cart', {})
    pet_ids = list(cart.keys())

    if pet_ids:
        pets_in_cart = Pet.objects.filter(id__in=pet_ids)
        cart_total = calculate_cart_total(cart, pets_in_cart)

    template_data['page_title'] = 'Your Cart current selection | Petzy Pet Store'
    template_data['pets_in_cart'] = pets_in_cart
    template_data['cart_total'] = cart_total

    return render(request, 'cart/index.html', {'data': template_data})


def add(request: HttpRequest, id: int) -> HttpResponse:
    get_object_or_404(Pet, id=id)
    cart = request.session.get('cart', {})
    
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart

    return redirect('cart.cart_home_page')
