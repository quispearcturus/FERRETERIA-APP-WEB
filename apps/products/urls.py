# ZeroPaul
from django.urls import path, include
from apps.products.views.product import ProductCountView, ProductListView, ProductDetailView, ProductCreateUpdateView

app_name = 'products'

urlpatterns = [
    # path('example/', ExampleView.as_view(), name='example'),
    path('', ProductCountView.as_view(), name='product_count'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    
    path('product/create/', ProductCreateUpdateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductCreateUpdateView.as_view(), name='product_edit'),
]