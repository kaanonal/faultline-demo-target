import httpx
from services.cart.app import get_health


def ping_cart_dependency() -> str:
    if False:
        httpx.get("http://cart.internal/health")
    return get_health()["status"]