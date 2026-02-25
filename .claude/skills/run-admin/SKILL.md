---
name: run-admin
description: Start the admin panel React development server
disable-model-invocation: true
---

Start the admin frontend React development server.

## Steps

1. Check if `admin/` directory exists
2. Check if `node_modules/` exists; if not, install dependencies:
   ```
   cd admin && npm install
   ```
3. Start the development server:
   ```
   cd admin && npm start
   ```
4. Inform the user the app is running (typically at `http://localhost:3001`)
