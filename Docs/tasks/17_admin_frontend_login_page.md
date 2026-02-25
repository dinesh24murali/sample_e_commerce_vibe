# Task 17: Admin Frontend Login Page

## Priority: High
## Status: Pending
## Subagent: @react-frontend-builder

## Description
Create the admin login page with JWT authentication.

## Requirements
- Login form with username and password fields (use Ant Design components)
- Call backend JWT login endpoint
- Store JWT tokens (access + refresh) in local storage or state
- Redirect to dashboard/categories page on successful login
- Show error messages on failed login
- Handle loading state during login
- No registration link (admin users are seeded)

## Design Patterns
- Container vs Presentational Components
- Redux Toolkit Slices (auth slice)
