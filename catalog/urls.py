from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contact, catalog, catalog_category, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='ko1216-shop'),
    path('contact/', contact, name='contact'),
    path('catalog/', catalog, name='catalog'),
    path('<int:pk>/catalog/categories/', catalog_category, name='catalog_category'),
    path('<int:pk>/catalog/products/', product, name='product')
]
