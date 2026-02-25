# Task 22: Admin Frontend Book Create/Edit Form

## Priority: High
## Status: Pending
## Subagent: @react-frontend-builder

## Description
Create the book create and edit form page using Ant Design form components.

## Requirements
- Form fields: name, category (dropdown from API), description (textarea), image URL, price, discount, tax, is_available (toggle)
- Reuse form for both create and edit modes
- On create: POST to backend, redirect to book list on success
- On edit: pre-fill form with existing data, PUT to backend on submit
- Show validation errors
- Handle loading state during submission

## Design Patterns
- Container vs Presentational Components
- Redux Toolkit Slices
