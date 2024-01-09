from django.urls import path
from . import views

# Urls configuration for store app.
urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.update_item, name='update_item'),
    path('process_order/', views.process_order, name='process_order'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='user_login'),
    path('logout/', views.logout_user, name='user_logout'),
]