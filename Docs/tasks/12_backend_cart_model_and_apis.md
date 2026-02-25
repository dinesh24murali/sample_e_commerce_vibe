# Task 12: Backend Cart Model and APIs

## Priority: High
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create the Cart and CartItem models and API endpoints for cart management. Requires customer authentication.

## Requirements
- Cart model: linked to user, audit fields
- CartItem model: linked to cart, book, quantity, audit fields
- GET `/api/cart/` — get current user's cart with items
- POST `/api/cart/items/` — add item to cart
- PUT `/api/cart/items/<id>/` — update cart item quantity
- DELETE `/api/cart/items/<id>/` — remove item from cart
- All endpoints require customer authentication
- Write tests before implementation
- Add adequate logging

## Design Patterns
- Fat Models, Thin Views
- Service Layer
- Class-Based Views (CBVs)
