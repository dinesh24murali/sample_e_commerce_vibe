Can you break this @Docs/Initial_prd/prd.txt into multiple small tasks? Save each task into individual smaller markdown files under @Docs/tasks folder. I have additional requirements:
- Assign each task a priority and status field. The status field should tell whether the task is completed / pending / ready
- Assign each task a subagent that should pick and work on the task. Use the @react-frontend-builder for frontend tasks and @django-backend-builder for backend related tasks
- make the tasks as small as possible
- Name the files in the following format: <task-number>_<description>_.md . The task number should be incremental numbers