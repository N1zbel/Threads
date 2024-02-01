from django.contrib import admin
from .models import UserProfile, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)


admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
