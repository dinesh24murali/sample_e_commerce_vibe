# Django Backend Builder — Agent Memory

## Project Structure

- Repo root: `/home/dinesh/work_dump/my_projects/sample_e_commerce_vibe/`
- Backend root: `/home/dinesh/work_dump/my_projects/sample_e_commerce_vibe/backend/`
- Django project name: `bookstore`
- Virtual environment: `backend/venv/` — always use `./venv/bin/python` or `./venv/bin/pip`
- PRD: `Docs/Initial_prd/prd.md`

## Settings Splitting Pattern

- `backend/bookstore/settings/base.py` — shared config (DB, REST_FRAMEWORK, JWT, CORS lists, LOGGING skeleton)
- `backend/bookstore/settings/development.py` — DEBUG=True, CORS localhost origins, verbose logging
- `backend/bookstore/settings/production.py` — DEBUG=False, security hardening, file logging
- `manage.py` defaults to `bookstore.settings.development`
- `wsgi.py` / `asgi.py` default to `bookstore.settings.production`
- Run commands: `DJANGO_SETTINGS_MODULE=bookstore.settings.development ./venv/bin/python manage.py <cmd>`

## Environment Variables

- Uses `python-decouple` — reads from `backend/.env`
- `.env.example` exists; `.env` is gitignored (real secrets never committed)
- Required vars: `SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- Optional: `JWT_ACCESS_TOKEN_LIFETIME_MINUTES`, `JWT_REFRESH_TOKEN_LIFETIME_DAYS`, `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`

## Key Packages (requirements.txt)

Django==6.0.2, djangorestframework==3.16.1, djangorestframework_simplejwt==5.5.1,
django-cors-headers==4.9.0, psycopg2-binary==2.9.11, python-decouple==3.8,
gunicorn==25.1.0, Pillow==12.1.1

## REST Framework Defaults (base.py)

- Authentication: JWTAuthentication
- Permissions: IsAuthenticated
- Pagination: PageNumberPagination, PAGE_SIZE=20
- Renderer: JSONRenderer only

## App Organization Convention

- Local apps go under `backend/apps/<appname>/` and register as `"apps.<appname>"` in INSTALLED_APPS
- Apps planned: accounts, catalog, orders, payments

## URL Convention

- All APIs versioned under `/api/v1/`
- Django admin at `/admin/`
- App URLs included in `bookstore/urls.py` as: `path("api/v1/<domain>/", include("apps.<domain>.urls"))`

## Database

- PostgreSQL via psycopg2-binary
- Config fully in environment variables (no hardcoded credentials)

## PRD Key Points

- Customer auth: email + password login
- Admin auth: JWT only, no registration (admins seeded via management command)
- Seed scripts needed: default admin user + 2 categories + 2 books
- Book fields: name, category, description, image_url, price, discount, tax, is_available
- Payment gateway: Razorpay (server-side signature validation required)
- All admin APIs require JWT; customer public pages do not require auth

## See Also

- `patterns.md` — coding patterns and conventions
