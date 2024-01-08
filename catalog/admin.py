from django.contrib import admin

from catalog.models import Product, Category

# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_one', 'category',)
    list_filter = ('category',)
    search_fields = ('name__icontains', 'description__icontains',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
