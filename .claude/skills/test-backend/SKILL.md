---
name: test-backend
description: Run Django backend tests for the e-commerce project
argument-hint: "[app-name or test-path]"
---

Run the Django backend test suite.

## Steps

1. Navigate to the `backend/` directory
2. If `$ARGUMENTS` is provided, run tests for that specific app or test path:
   ```
   cd backend && python manage.py test $ARGUMENTS --verbosity=2
   ```
3. If no arguments, run the full test suite:
   ```
   cd backend && python manage.py test --verbosity=2
   ```
4. Report the results clearly — number of tests passed, failed, and any errors with file/line references
5. If tests fail, briefly analyze the failure and suggest what might need fixing
