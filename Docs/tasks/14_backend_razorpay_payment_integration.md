# Task 14: Backend Razorpay Payment Integration

## Priority: High
## Status: Pending
## Subagent: @django-backend-builder

## Description
Integrate Razorpay payment gateway. Create endpoints to initiate payment and handle payment verification callback.

## Requirements
- POST `/api/payments/create/` — create a Razorpay order for a given order ID
- POST `/api/payments/verify/` — verify Razorpay payment signature and update order status
- Store Razorpay API keys in environment variables
- Update order status to paid/failed based on payment result
- All endpoints require customer authentication
- Write tests before implementation
- Add adequate logging

## Design Patterns
- Service Layer
- Class-Based Views (CBVs)
