# Task 11: Backend Customer Book List & Detail APIs

## Priority: Medium
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create public API endpoints for customers to browse books with category filtering and view single book details.

## Requirements
- GET `/api/books/` — list all available books (public, no auth required)
- Support filtering by `category` query parameter
- GET `/api/books/<id>/` — get single book details (public)
- Only return books where `is_available=True`
- Write tests before implementation
- Add adequate logging

## Design Patterns
- Class-Based Views (CBVs)
- Repository Pattern (via Managers)
