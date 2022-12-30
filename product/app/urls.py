from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product_add',views.product_add,name='product_add'),
]