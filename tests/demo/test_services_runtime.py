import unittest

import tests.demo  # noqa: F401 — httpx fallback'i yükler
from services.audit.client import ping_cart_dependency
from services.checkout.client import build_checkout_summary
from services.notifications.client import send_order_confirmation
from services.payment.client import charge_cart, check_cart_health
from services.shipping.client import calculate_shipping


class AuthDownstreamRuntimeTests(unittest.TestCase):
    def test_checkout_build_summary(self):
        summary = build_checkout_summary()
        self.assertEqual(summary["customer_name"], "Ada Lovelace")
        self.assertEqual(summary["receipt_email"], "ada@faultline.dev")

    def test_notifications_send_confirmation(self):
        message = send_order_confirmation()
        self.assertIn("ada@faultline.dev", message)


class CartDownstreamRuntimeTests(unittest.TestCase):
    # Yüzeysel test (price alanına hiç değmez — Coverage Reflection tuzağı)
    def test_payment_shallow_health(self):
        self.assertTrue(check_cart_health())

    # Derin kontrat testleri (price ve currency alanlarını tüketir)
    def test_payment_charge_cart(self):
        result = charge_cart(10)
        self.assertEqual(result["charged"], 148.32)
        self.assertEqual(result["currency"], "USD")

    def test_shipping_calculate_fee(self):
        result = calculate_shipping(10)
        self.assertTrue(result["free_shipping"])
        self.assertEqual(result["shipping_fee"], 0.0)

    def test_audit_health_isolated(self):
        self.assertEqual(ping_cart_dependency(), "ok")