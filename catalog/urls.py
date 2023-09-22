from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, IndexListView, CatalogListView, CategoryListView, ProductListView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='ko1216-shop'),
    path('contact/', contact, name='contact'),
    path('catalog/', CatalogListView.as_view(), name='all_products'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='catalog_category'),
    path('product/<int:pk>', ProductListView.as_view(), name='product'),
    path('product/create', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
