# Task 18: Admin Frontend Auth Guard / Protected Routes

## Priority: High
## Status: Pending
## Subagent: @react-frontend-builder

## Description
Create a protected route wrapper that redirects unauthenticated users to the login page.

## Requirements
- Create a `ProtectedRoute` component
- Check for valid JWT token before rendering protected pages
- Redirect to login page if not authenticated
- Attach JWT token to all API requests (axios interceptor or similar)
- Handle token expiry and refresh

## Design Patterns
- Container vs Presentational Components
