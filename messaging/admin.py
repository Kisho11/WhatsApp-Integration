from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'status')
    list_filter = ('status', 'timestamp')
    search_fields = ('sender', 'receiver', 'content')
