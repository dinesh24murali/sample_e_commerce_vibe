# Task 04: Backend Custom User Model

## Priority: High
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create a custom User model (or extend the default) to support customer authentication with email and password. Include audit fields.

## Requirements
- Support email/password login for customers
- Differentiate between admin users and customer users (e.g., `is_staff` or a role field)
- Add audit fields: `created_at`, `updated_at`
- Write unit tests before implementation
- Create and run migrations

## Design Patterns
- Fat Models, Thin Views
