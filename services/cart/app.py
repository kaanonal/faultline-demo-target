def _calculate_tax(subtotal: float) -> float:
    return round(subtotal * 0.20, 2)


def get_cart(cart_id: int) -> dict:
    base_price = 120.0
    return {
        "id": cart_id,
        "item": "Mechanical Keyboard",
        "price": base_price + _calculate_tax(base_price),
        "currency": "USD",
    }


def get_health() -> dict:
    return {"status": "ok"}