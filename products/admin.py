from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ["product", "active", "stars", "body", ]
    extra = 0


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["title", "price", "active"]
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "product", "active", "stars", "body", ]
