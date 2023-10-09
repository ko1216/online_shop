from django.conf import settings
from django.core.cache import cache


def get_cached_category(product):
    if settings.CACHE_ENABLED:
        category_key = f'category_{product.pk}'
        category = cache.get(category_key)
        if category is None:
            category = product.category
            cache.set(category_key, category)
    else:
        category = product.category
    return category


def get_cached_categories(categories_list):
    if settings.CACHE_ENABLED:
        categories_key = f'categories_list_{categories_list}'
        categories = cache.get(categories_key)
        if categories is None:
            categories = categories_list
            cache.set(categories_key, categories)
    else:
        categories = categories_list
    return categories
