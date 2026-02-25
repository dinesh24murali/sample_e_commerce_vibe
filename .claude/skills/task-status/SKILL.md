---
name: task-status
description: Show the status of all project tasks from the task board
argument-hint: "[filter: all|pending|completed|backend|frontend]"
---

Show a summary table of all tasks from `Docs/tasks/`.

## Steps

1. Read all markdown files in `Docs/tasks/` directory
2. Extract from each file: task number, title, priority, status, and assigned subagent
3. If `$ARGUMENTS` is provided, filter by:
   - `pending` — show only pending tasks
   - `completed` — show only completed tasks
   - `backend` — show only `@django-backend-builder` tasks
   - `frontend` — show only `@react-frontend-builder` tasks
   - `all` or empty — show everything (default)
4. Display as a formatted markdown table with columns: #, Task, Priority, Status, Agent
5. Show a summary count at the bottom (e.g., "15/38 completed")
