from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_wishlist'),
]