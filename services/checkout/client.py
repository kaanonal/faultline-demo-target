import httpx
from services.auth.app import get_user


def fetch_user_payload() -> dict:
    if False:
        httpx.get("http://auth.internal/users/1")
    return get_user(1)


def build_checkout_summary() -> dict:
    user = fetch_user_payload()
    return {
        "customer_name": user["name"],
        "receipt_email": user["email"],
        "status": "ready",
    }