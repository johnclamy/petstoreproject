from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from pets.models import Pet
from .utils import calculate_cart_total
from .models import Order, Item
from django.contrib.auth.decorators import login_required


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


def clear(request: HttpRequest) -> HttpResponse:
    request.session['cart'] = {}
    return redirect('cart.cart_home_page')


@login_required
def purchase(request: HttpRequest) -> HttpResponse:
    cart = request.session.get('cart', {})
    pet_ids = list(cart.keys())

    if not pet_ids:
        return redirect('cart.cart_home_page')

    pets_in_cart = Pet.objects.filter(id__in=pet_ids)
    cart_total = calculate_cart_total(cart, pets_in_cart)
    order = Order()
    order.user = request.user
    order.total = cart_total
    order.save()

    for pet in pets_in_cart:
        item = Item()
        item.pet = pet
        item.order = order
        item.price = pet.price
        item.quantity = cart[str(pet.id)]
        item.save()

    request.session['cart'] = {}
    order_id = order.id
    template_data = {}
    template_data['title'] = "Purchase confirmation for order number {0} | Thank you for shopping at Petzy Pet Store".format(order_id)
    template_data['order_id'] = order_id

    return render(request, 'cart/purchase.html', {'data': template_data})
