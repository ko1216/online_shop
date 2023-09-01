from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Category')
    description = models.TextField(max_length=400, verbose_name='Description')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    description = models.TextField(max_length=1000, verbose_name='Description')
    products_image = models.ImageField(upload_to='products_image', verbose_name='Product Image', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    price = models.FloatField(max_length=15, verbose_name='Price')
    created_at = models.DateTimeField(**NULLABLE, verbose_name='Created At')
    last_update = models.DateTimeField(**NULLABLE, verbose_name='Last Update')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('category', 'price',)
