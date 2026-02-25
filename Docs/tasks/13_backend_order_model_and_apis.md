# Task 13: Backend Order Model and APIs

## Priority: High
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create Order and OrderItem models and API endpoints for placing orders and viewing order history.

## Requirements
- Order model: linked to user, total amount, status (pending/paid/failed), payment_id, audit fields
- OrderItem model: linked to order, book, quantity, price at purchase, audit fields
- POST `/api/orders/` — create order from cart (checkout)
- GET `/api/orders/` — list user's order history
- GET `/api/orders/<id>/` — get order details
- All endpoints require customer authentication
- Write tests before implementation
- Add adequate logging

## Design Patterns
- Fat Models, Thin Views
- Service Layer
- Class-Based Views (CBVs)
