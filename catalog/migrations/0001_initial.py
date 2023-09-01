# Generated by Django 4.2.4 on 2023-09-01 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('products_image', models.ImageField(blank=True, null=True, upload_to='products_image', verbose_name='Product Image')),
                ('price', models.FloatField(max_length=15, verbose_name='Price')),
                ('created_at', models.DateTimeField()),
                ('last_updated', models.DateTimeField(auto_now_add=True, verbose_name='Last Updated')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('category', 'price'),
            },
        ),
    ]