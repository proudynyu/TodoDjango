from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
	fields = ['title']

admin.site.register(Todo, TodoAdmin)