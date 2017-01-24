from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')

admin.site.register(Snippet, SnippetAdmin)