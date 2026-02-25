# Task 28: Customer Frontend Auth Guard / Protected Routes

## Priority: High
## Status: Pending
## Subagent: @react-frontend-builder

## Description
Create a protected route wrapper for customer pages that require login.

## Requirements
- Create a `ProtectedRoute` component
- Protected pages: cart, checkout, payment, accounts, order history, order details
- Public pages: home, book list, single book, login, signup
- Redirect to login if not authenticated
- Attach auth token to API requests
- Handle token expiry

## Design Patterns
- Container vs Presentational Components
