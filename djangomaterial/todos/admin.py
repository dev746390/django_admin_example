from django.contrib.admin import ModelAdmin, register
from .models import Todo


@register(Todo)
class TodoAdmin(ModelAdmin):
    list_display = ('task', 'owner', 'created_at')
    list_filter = ['owner', 'created_at']
    icon_name = 'assignment_ind'
