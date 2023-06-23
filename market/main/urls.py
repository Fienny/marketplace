from django.urls import path

from .views import (ProductList, ProductCreate, CategoryList, CategoryCreate, CreateSeller, ProductUpdate,
                    ProductDelete, ProductView, category_view)

urlpatterns = [
    path('catalog', ProductList.as_view(), name='products'),
    path('catalog/create', ProductCreate.as_view()),
    path('catalog/<int:pk>', ProductView.as_view(), name="product"),
    path('catalog/<int:pk>/update', ProductUpdate.as_view(), name="update_product"),
    path('catalog/<int:pk>/delete', ProductDelete.as_view()),
    path('catalog/categories', CategoryList.as_view(), name='categories'),
    path('catalog/category/<category_pk>', category_view, name="category"),
    path('catalog/categories/create', CategoryCreate.as_view()),
    path('catalog/become_seller', CreateSeller.as_view(), name='become_seller'),
]
