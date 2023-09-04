from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'product_list': Product.objects.all(),
        'title': 'Главная ko1216-shop'
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contact.html', context)


def catalog(request):
    context = {
        'product_list': Product.objects.all(),
        'title': 'Каталог товаров'
    }
    return render(request, 'catalog/catalog.html', context)


def catalog_category(request, pk):
    category_product = Category.objects.get(pk=pk)
    context = {
        'product_list': Product.objects.filter(category=pk),
        'title': f'Категория {category_product.name}'
    }
    return render(request, 'catalog/categories.html', context)


def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product_list': Product.objects.filter(pk=pk),
        'title': f'Товар {product.name}'
    }
    return render(request, 'catalog/product.html', context)
