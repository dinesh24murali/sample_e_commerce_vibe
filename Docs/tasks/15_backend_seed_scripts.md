# Task 15: Backend Seed Scripts

## Priority: Medium
## Status: Pending
## Subagent: @django-backend-builder

## Description
Create Django management commands to seed the database with default data.

## Requirements
- Seed script to create a default admin user with a default username and password
- Seed script to create 2 sample categories
- Seed script to create 2 sample books (one per category)
- Scripts should be idempotent (safe to run multiple times)
- Can be a single management command or multiple

## Design Patterns
- Django Management Commands
