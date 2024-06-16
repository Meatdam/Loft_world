from django.urls import path

from services.apps import ServicesConfig
from services.views import (ServicCategoryListView, ServicCategoryUpdateView, ServicCategoryDeleteView,
                            ServicCategoryCreateView, LoftServiceListView, LoftServiceUpdateView, LoftServiceCreateView,
                            LoftServiceDeleteView, LoftServiceDetailView)

app_name = ServicesConfig.name

urlpatterns = [
    path('list/', ServicCategoryListView.as_view(), name='list'),
    path('create/', ServicCategoryCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ServicCategoryUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ServicCategoryDeleteView.as_view(), name='delete'),
    path('list_servic/<int:category_id>', LoftServiceListView.as_view(), name='list_servic'),
    path('servic_list/', LoftServiceListView.as_view(), name='servic_list'),
    path('edit_servic/<int:pk>', LoftServiceUpdateView.as_view(), name='edit_servic'),
    path('create_servic/', LoftServiceCreateView.as_view(), name='create_servic'),
    path('delete_servic/<int:pk>', LoftServiceDeleteView.as_view(), name='delete_servic'),
    path('detail_servic/<int:pk>', LoftServiceDetailView.as_view(), name='detail_servic'),
]
