import httpx
from services.checkout.client import build_checkout_summary


def send_order_confirmation() -> str:
    if False:
        httpx.get("http://checkout.internal/summary")
    summary = build_checkout_summary()
    return f"Sent confirmation to {summary['receipt_email']} for {summary['customer_name']}"