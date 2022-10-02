from django.urls import path
from .views import CategoryListCreateView, ProductListCreateView, UserRegisterView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
]

urlpatterns += [
    path('register/', UserRegisterView.as_view(), name='user-register'),
]
