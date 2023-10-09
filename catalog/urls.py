from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contact, IndexListView, CatalogListView, CategoryListView, ProductCreateView, \
    ProductUpdateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexListView.as_view()), name='ko1216-shop'),
    path('contact/', contact, name='contact'),
    path('catalog/', CatalogListView.as_view(), name='all_products'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='catalog_category'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/create', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
