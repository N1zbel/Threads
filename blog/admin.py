from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Comment, Post, UserProfile


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author_link", "created_at")  # Отображаем ссылку на автора
    list_filter = ("created_at",)  # Добавляем фильтр по дате создания

    def author_link(self, obj):
        author_url = reverse("admin:blog_userprofile_change", args=[obj.author.pk])
        return format_html('<a href="{}">{}</a>', author_url, obj.author.user.username)

    author_link.short_description = "Author"  # Задаем название колонки


admin.site.register(UserProfile)
admin.site.register(
    Post, PostAdmin
)  # Регистрируем модель Post с кастомной административной панелью
admin.site.register(Comment)
