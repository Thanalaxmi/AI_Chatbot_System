try:
    from Backend.main import app
except Exception:
    # Fallback: import dynamically to surface errors when uvicorn imports this module
    import importlib
    mod = importlib.import_module("Backend.main")
    app = getattr(mod, "app")
