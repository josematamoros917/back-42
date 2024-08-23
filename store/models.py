from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return f'Image for {self.product.name}'

class Order(models.Model):
    
    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    customer_phone = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='PENDING')
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id} - {self.product.name}'

    def total_price(self):
        return self.quantity * self.product.price