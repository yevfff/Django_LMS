from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Book Title')
    author = models.CharField(max_length=100, verbose_name='Author')
    published_date = models.DateField(verbose_name='Published Date')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return f"{self.title} by {self.author}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    description = models.TextField(verbose_name='Product Description')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')
    release_date = models.DateField(
        null=True, blank=True, verbose_name='Release Date')

    def __str__(self):
        return self.name


class Order(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DELIVERED = 'delivered', 'Delivered'

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.NEW, verbose_name='Status')

    def __str__(self):
        return f"Order #{self.id} for {self.product.name}"


class Profile(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, verbose_name='User')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email')
