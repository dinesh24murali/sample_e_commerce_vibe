# Task 03: Backend Book Model

## Priority: High
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create the Book model with all required fields and audit fields. Follow TDD — write tests first, then implement the model.

## Requirements
- Book model fields: `name`, `category` (FK to Category), `description`, `image_url`, `price`, `discount`, `tax`, `is_available`
- Add audit fields: `created_at`, `updated_at`, `created_by`, `updated_by`
- Write unit tests for the model before implementation
- Create and run migrations

## Design Patterns
- Fat Models, Thin Views
- Repository Pattern (via Managers)
