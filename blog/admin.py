from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'create_format_long', 'status']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)