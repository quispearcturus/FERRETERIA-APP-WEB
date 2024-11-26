# ZeroPaul
from django.urls import path, include
from apps.sales.views.sale import SaleListView, SaleCreateUpdateView, ProductAutocompleteView
from apps.sales.views.pdf import SalePDFView


app_name = 'sales'

urlpatterns = [
    path('sale/', SaleListView.as_view(), name='sale_list'),
    path('sale/create/', SaleCreateUpdateView.as_view(), name='sale_create'),
    path('sale/<int:pk>/edit/', SaleCreateUpdateView.as_view(), name='sale_edit'),
    path('sale-product/', ProductAutocompleteView.as_view(), name='sale_auto_product'),
    path(
        route ='sale-pdf/<int:pk>/',
        view = SalePDFView.as_view(),
        name = 'sale_pdf'
    ),
]