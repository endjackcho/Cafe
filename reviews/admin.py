from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    ordering = ("-created_at",)