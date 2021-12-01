from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_products, name='list_products'),
    path('new', views.new_product, name='new_product'),
    path('product/edit/<int:pid>', views.edit_product),
    path('product/delete/<int:pid>', views.delete_product)
]
