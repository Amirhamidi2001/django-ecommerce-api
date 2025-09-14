from django.contrib import admin
from .models import Brand, Category, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Brand model.
    """

    list_display = ("name", "slug", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Category model.
    """

    list_display = ("name", "slug", "parent", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_filter = ("parent",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Product model.
    """

    list_display = (
        "name",
        "slug",
        "category",
        "brand",
        "price",
        "stock",
        "is_active",
        "created_at",
        "updated_at",
    )
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("category", "brand", "is_active")
    search_fields = ("name", "description")
    ordering = ("name",)
    list_editable = ("price", "stock", "is_active")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "image",
                    "category",
                    "brand",
                    "price",
                    "stock",
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )
