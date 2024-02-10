from django.contrib import admin
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount', 'category']
    list_editable = ['quantity', 'price', 'discount', 'category']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'quantity', 'category']
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]