# Django Backend — Coding Patterns

## Management Commands (Seed Scripts)

```python
# backend/apps/<app>/management/commands/seed_<name>.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seed description'

    def handle(self, *args, **options):
        # idempotent creation logic
        self.stdout.write(self.style.SUCCESS('Done'))
```

## Custom Permissions

```python
# apps/<app>/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminJWT(BasePermission):
    """Only Django staff users (JWT authenticated) can access."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
```

## Consistent Response Format

```python
# Success
return Response({"data": serializer.data}, status=status.HTTP_200_OK)
# List
return Response({"data": serializer.data, "count": queryset.count()}, status=status.HTTP_200_OK)
# Error
return Response({"error": "Not found", "details": {}}, status=status.HTTP_404_NOT_FOUND)
```

## Model Conventions

- All models get `created_at` and `updated_at` (use `auto_now_add` / `auto_now`)
- Use `related_name` on every ForeignKey
- Write meaningful `__str__` methods
- Add `Meta` with `ordering`, `verbose_name`, `verbose_name_plural`
- Use `BigAutoField` as primary key (set globally via `DEFAULT_AUTO_FIELD`)

## ViewSet Pattern

```python
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAdminJWT]

    def get_queryset(self):
        return Book.objects.select_related('category').filter(is_available=True)
```

## N+1 Prevention

Always use `select_related` for ForeignKey/OneToOne and `prefetch_related` for M2M / reverse FK in `get_queryset()`.

## Running Commands

Always prefix with the full venv path:
```bash
cd /home/dinesh/work_dump/my_projects/sample_e_commerce_vibe/backend
./venv/bin/python manage.py <command>
./venv/bin/pip install <package>
```
