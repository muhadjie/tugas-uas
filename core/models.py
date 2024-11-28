from django.db import models

class Category(models.Model):
    # Nama kategori alat penyewaan gunung, misalnya: Tenda, Tas Carrier, Peralatan Masak
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class RentalProduct(models.Model):
    # Informasi dasar alat penyewaan gunung
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='rental_products', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    daily_rental_price = models.DecimalField(max_digits=10, decimal_places=2)  # Harga sewa per hari
    stock = models.PositiveIntegerField()  # Jumlah stok barang
    image = models.ImageField(upload_to='rental_product_images/', blank=True, null=True)  # Gambar produk
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rental Product"
        verbose_name_plural = "Rental Products"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.category.name}"

class Rental(models.Model):
    # Informasi penyewaan
    product = models.ForeignKey(RentalProduct, related_name='rentals', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=15)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rental"
        verbose_name_plural = "Rentals"
        ordering = ['rental_start_date']

    def __str__(self):
        return f"Rental: {self.product.name} by {self.customer_name}"
