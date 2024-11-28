from django.urls import path
from . import views

app_name = 'shop'  # Namespace untuk aplikasi shop

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  
    path('clear-cart/', views.clear_cart, name='clear_cart'),
]
