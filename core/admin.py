from django.contrib import admin
from .models import Category, RentalProduct, Rental


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(RentalProduct)
class RentalProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'daily_rental_price', 'stock', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    list_editable = ('daily_rental_price', 'stock')
    ordering = ('name',)

    # Display inline related Rentals for RentalProduct in a tabular form
    inlines = []

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'rental_start_date', 'rental_end_date', 'total_price', 'created_at')
    list_filter = ('rental_start_date', 'rental_end_date', 'product')
    search_fields = ('customer_name', 'product__name')
    ordering = ('rental_start_date',)

    # Calculate total price dynamically based on rental days

