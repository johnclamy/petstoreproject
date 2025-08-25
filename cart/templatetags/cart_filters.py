from django import template


register = template.Library()


@register.filter(name='get_quantity')
def get_cart_quantity(cart: dict[str, str], pet_id: int) -> int:
    return int(cart[str(pet_id)])
