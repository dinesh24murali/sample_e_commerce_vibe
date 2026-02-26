"""
Development settings for bookstore project.

Extends base settings with development-specific overrides.
"""

from .base import *  # noqa: F401, F403
from decouple import config

# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

DEBUG = True

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1",
    cast=lambda v: [s.strip() for s in v.split(",")],
)

# ---------------------------------------------------------------------------
# CORS — allow all localhost origins for development
# ---------------------------------------------------------------------------

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",   # Customer frontend (default CRA / Vite port)
    "http://localhost:3001",   # Admin panel (alternate port)
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://localhost:5173",   # Vite default
    "http://localhost:5174",   # Vite alternate
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# ---------------------------------------------------------------------------
# Logging — verbose for development
# ---------------------------------------------------------------------------

LOGGING["loggers"]["django.db.backends"]["level"] = "DEBUG"  # noqa: F405
LOGGING["root"]["level"] = "DEBUG"  # noqa: F405

# ---------------------------------------------------------------------------
# Development-only apps (e.g., django-extensions, debug toolbar)
# ---------------------------------------------------------------------------

# Uncomment to enable Django Debug Toolbar:
# INSTALLED_APPS += ["debug_toolbar"]
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
# INTERNAL_IPS = ["127.0.0.1"]
