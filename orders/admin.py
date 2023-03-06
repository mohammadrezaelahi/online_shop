from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    fields = ["order", "product", "quantity", "price", ]
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "is_paid", "first_name", "last_name", "datetime_created"]
    inlines = [
        OrderItemsInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price", ]
