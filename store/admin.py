from django.contrib import admin
from .models import Category, Product, Order, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Número de formularios vacíos adicionales que se mostrarán
# Configuración para el modelo Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

# Configuración para el modelo Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'category', 'image')
    list_filter = ('available', 'category')
    search_fields = ('name', 'description', 'category__name')
    ordering = ('name',)
    inlines = [ProductImageInline]
    

# Configuración para el modelo Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'customer_name', 'status', 'order_date')
    list_filter = ('status', 'order_date', 'product')
    search_fields = ('customer_name', 'customer_address', 'customer_phone', 'product__name')
    ordering = ('-order_date',)
    readonly_fields = ('order_date',)  # Ejemplo: Hacer que el campo order_date sea de solo lectura

# Registro de los modelos con sus configuraciones
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Order, OrderAdmin)
