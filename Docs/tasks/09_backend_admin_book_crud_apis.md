# Task 09: Backend Admin Book CRUD APIs

## Priority: High
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create CRUD API endpoints for books, accessible only by authenticated admin users (JWT required).

## Requirements
- GET `/api/admin/books/` — list all books
- POST `/api/admin/books/` — create a book
- GET `/api/admin/books/<id>/` — get single book
- PUT `/api/admin/books/<id>/` — update a book
- DELETE `/api/admin/books/<id>/` — delete a book
- All endpoints require JWT authentication
- Write tests before implementation
- Add adequate logging

## Design Patterns
- Class-Based Views (CBVs)
- Service Layer
- Repository Pattern (via Managers)
