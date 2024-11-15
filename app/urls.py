from django.urls import path
from app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('product/detail<int:id>/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('login/', views.login_view, name='login'),
    path('registration/', views.customerregistration, name='register'),
    path('checkout/', views.checkout, name='checkout'),
]
