from django.urls import path
from .views import register_user,get_product,get_products, create_product,update_product,delete_product,get_category,create_category,create_cart,add_to_cart,get_cart_items,create_order,get_orders,update_category,delete_category
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)




urlpatterns =[
    #AUTH
    path('register/',register_user),
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
 

    #PRODUCTS
    path('products/',get_product),
    path('product/<int:pk>',get_products),
    path('product/create/', create_product),
    path('product/update/<int:pk>',update_product),
    path('product/delete/<int:pk>',delete_product),


#CATEGORIES
path('category/',get_category),
path('categories/create/',create_category),
path('categories/update/<int:pk>/',update_category),
path('categories/delete/<int:pk>/',delete_category),

#CART
path('cart/create/', create_cart),
path('cart/add/', add_to_cart),
path('cart/items/', get_cart_items),

#OrDERS
path('orders/create/',create_order),
path('orders/',get_orders)
]