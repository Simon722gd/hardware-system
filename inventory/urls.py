from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    # Products
    path('products/', views.products_view, name='products'),
    path('products/list/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('low-stock/', views.low_stock_products, name='low_stock'),
    # Suppliers
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/update/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
    # Sales
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/create/', views.sale_create, name='sale_create'),
    path('sales/<int:pk>/receipt/', views.sale_receipt, name='sale_receipt'),
    path('payments/', views.payments, name='payments'),
    path('products/<int:pk>/detail/', views.product_detail, name='product_detail'),
    # Reports and Exports
    path('reports/', views.reports, name='reports'),
    path('export/sales-pdf/', views.export_sales_pdf, name='export_sales_pdf'),
    path('export/products-excel/', views.export_products_excel, name='export_products_excel'),
    # Search
    path('search/', views.search, name='search'),
    path('mpesa-payment/', views.mpesa_payment, name='mpesa_payment'),
    path('mpesa-token-test/', views.mpesa_token_test, name='mpesa_token_test'),
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),
    # Users
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),
]
