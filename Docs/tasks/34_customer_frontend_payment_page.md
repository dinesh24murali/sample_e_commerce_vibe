# Task 34: Customer Frontend Payment Page (Razorpay)

## Priority: High
## Status: Pending
## Subagent: @react-frontend-builder

## Description
Create the payment page that integrates with Razorpay checkout.

## Requirements
- Call backend to create Razorpay order
- Open Razorpay checkout modal/widget with order details
- On payment success: call backend verify endpoint, redirect to success page
- On payment failure: redirect to failed page
- Handle loading state while creating payment
- Protected page (requires login)

## Design Patterns
- Container vs Presentational Components
