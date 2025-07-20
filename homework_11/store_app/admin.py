import random

from django.contrib import admin
from .models import Product, Category, Comment, Tag, Author, AuthorProfile


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "category",
        "tag_list",
    )
    ordering = ("price",)
    list_filter = (
        "price",
        "category",
    )
    search_fields = (
        "name",
        "description",
    )
    search_help_text = "ГООООООООООЛ"

    fields = (
        "name",
        "description",
        "price",
        "category",
        "tags",
    )
    readonly_fields = ("price",)

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    tag_list.short_description = "Тэги"

    @admin.action(description="ГОООООООООЛ")
    def random_price_changing(self, request, queryset):
        for product in queryset:
            product.price = random.randint(0, 299)
            product.save()

    actions = (random_price_changing,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "author", "product")
    list_filter = ("author",)
    search_fields = ("text",)

    fieldsets = (
        ("Основная информация", {"fields": ("text", "author")}),
        (
            "Дополнительная информация",
            {"fields": ("product",), "classes": ("collapse",)},
        ),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_field = ("name",)
