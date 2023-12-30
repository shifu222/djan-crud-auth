from django.contrib import admin
from .models import Task

# Register your models here.
class task_admin(admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(Task,task_admin)