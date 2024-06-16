from django.urls import path

from loft.apps import LoftConfig
from loft.views import IndexListView, CategoryCreateView, CategoryUbdateView, CategoryDeleteView, ProductListView, \
    ProductCreateView, ProductDeleteView, ProductUpdateView, ProductDetailView

app_name = LoftConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('category', CategoryCreateView.as_view(), name='category'),
    path('product/<int:category_id>/', ProductListView.as_view(), name='product'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('edit/<int:pk>/', CategoryUbdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
]
