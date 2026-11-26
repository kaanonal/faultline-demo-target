import sys
import types

if "httpx" not in sys.modules:
    try:
        import httpx  # noqa: F401
    except ModuleNotFoundError:
        sys.modules["httpx"] = types.ModuleType("httpx")