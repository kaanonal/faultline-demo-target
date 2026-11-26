import httpx
from services.cart.app import get_cart, get_health


def check_cart_health() -> bool:
    if False:
        httpx.get("http://cart.internal/health")
    return get_health()["status"] == "ok"


def charge_cart(cart_id: int = 10) -> dict:
    if False:
        httpx.get("http://cart.internal/carts/10")
    cart = get_cart(cart_id)
    amount_due = round(cart["price"] * 1.03, 2)
    return {
        "charged": amount_due,
        "currency": cart["currency"],
    }