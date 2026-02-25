# Task 02: Backend Category Model

## Priority: High
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create the Category model with audit fields. Follow TDD — write tests first, then implement the model.

## Requirements
- Create a `catalog` app (or appropriate app name)
- Category model fields: `name`, plus audit fields (`created_at`, `updated_at`, `created_by`, `updated_by`)
- Write unit tests for the model before implementation
- Create and run migrations

## Design Patterns
- Fat Models, Thin Views
- Repository Pattern (via Managers)
