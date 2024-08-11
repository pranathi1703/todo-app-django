from django.contrib import admin
from .models import todo  # Note: Use capitalized 'Todo' for class names

@admin.register(todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('todo_name', 'user', 'status', 'created_at', 'updated_at', 'due_date')
    search_fields = ('todo_name', 'user__username')
    list_filter = ('status', 'created_at', 'updated_at', 'due_date')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:  # If the object is being created
            obj.user = request.user
        super().save_model(request, obj, form, change)
