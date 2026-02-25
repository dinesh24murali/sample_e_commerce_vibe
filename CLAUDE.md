# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

E-commerce platform for selling books. Three applications in a monorepo:

1. **Customer Frontend** — React SPA for browsing/purchasing books
2. **Admin Panel** — React SPA for managing categories and books
3. **Backend API** — Django server serving both frontends

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Customer Frontend | React 18+, Redux |
| Admin Frontend | React 18+, Redux, Ant Design |
| Backend | Django, PostgreSQL |
| Auth | JWT token-based (admin APIs require JWT) |
| Payments | Razorpay |

## Architecture

- Both frontends are SPAs that communicate with the Django backend via REST APIs
- Customer auth: email/password login
- Admin auth: JWT-only, no registration flow (admin users are seeded)
- Backend includes seed scripts for default admin user and sample data (2 categories, 2 books)

### Protected Routes (Customer App)

Cart, checkout, payment, accounts, order history, and order details pages require login. Home, book list, single book, login, and signup are public.

## Agent Usage

Use the `react-frontend-builder` agent (Sonnet model) for all React frontend work (both customer and admin apps). The PRD specifies which sub-agent to use for each ticket.

## Key Reference Documents

- `Docs/Initial_prd/prd.md` — Full product requirements document
- `.claude/agents/react-frontend-builder.md` — React agent configuration and coding standards

## Frontend Conventions (from react-frontend-builder agent)

- Functional components with hooks only (no class components)
- Naming: `handleClick` for handlers, `isLoading`/`hasError` for booleans, `on*` prefix for callback props
- Project structure follows: `src/{components,pages,hooks,services,utils,context,types,assets,styles}/`
- Components in `components/ui/` (base UI) and `components/layout/` (Header, Sidebar, Footer)
- Always handle loading, error, and empty states for async operations
