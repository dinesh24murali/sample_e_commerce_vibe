---
name: run-customer
description: Start the customer frontend React development server
disable-model-invocation: true
---

Start the customer frontend React development server.

## Steps

1. Check if `customer/` directory exists
2. Check if `node_modules/` exists; if not, install dependencies:
   ```
   cd customer && npm install
   ```
3. Start the development server:
   ```
   cd customer && npm start
   ```
4. Inform the user the app is running (typically at `http://localhost:3000`)
