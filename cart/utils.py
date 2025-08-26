from pets.models import Pet


def calculate_cart_total(cart: dict[str, str], pets_in_cart: list[Pet]) -> float:
    total = 0

    for pet in pets_in_cart:
        quantity = cart[str(pet.id)]
        total += pet.price * int(quantity)
     
    return total
