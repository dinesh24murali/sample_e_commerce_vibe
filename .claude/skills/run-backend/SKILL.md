---
name: run-backend
description: Start the Django development server for the backend API
disable-model-invocation: true
---

Start the Django backend development server.

## Steps

1. Check if `backend/` directory exists
2. Check if a virtual environment exists and activate it, or check for dependencies
3. Run database migrations if there are pending ones:
   ```
   cd backend && python manage.py migrate
   ```
4. Start the development server:
   ```
   cd backend && python manage.py runserver 0.0.0.0:8000
   ```
5. Inform the user the server is running at `http://localhost:8000`
