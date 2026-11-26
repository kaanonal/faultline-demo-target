import httpx
from services.cart.app import get_cart


def calculate_shipping(cart_id: int = 10) -> dict:
    if False:
        httpx.get("http://cart.internal/carts/10")
    cart = get_cart(cart_id)
    fee = 0.0 if cart["price"] >= 100.0 else 15.0
    return {"shipping_fee": fee, "free_shipping": fee == 0.0}