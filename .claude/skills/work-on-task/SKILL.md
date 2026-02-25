---
name: work-on-task
description: Pick up a task from Docs/tasks/ and work on it using the appropriate subagent
argument-hint: "[task-number]"
---

Work on task number `$ARGUMENTS` from the project task board.

## Steps

1. **Read the task file**: Read `Docs/tasks/` and find the file starting with the task number provided (e.g., `01`, `02`). If no task number is given, list all task files and show their status so the user can pick one.

2. **Validate the task**: Check that the task status is `Pending` or `Ready`. If it's already `Completed`, inform the user.

3. **Update status**: Change the task status from `Pending` to `In Progress` in the task markdown file before starting work.

4. **Delegate to the correct subagent**:
   - If the task specifies `@django-backend-builder`, use the `django-backend-builder` agent via the Task tool
   - If the task specifies `@react-frontend-builder`, use the `react-frontend-builder` agent via the Task tool
   - Pass the full task description and requirements to the subagent

5. **After completion**: Update the task status to `Completed` in the markdown file.

6. **Report**: Summarize what was done and any files created/modified.
