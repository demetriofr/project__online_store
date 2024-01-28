from django.urls import path

from catalog.views import contacts, ProductListView, CategoryListView, ProductCreateView, ProductUpdateView, \
    ProductDetailView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category'),
    # path('', product),
    path('contacts/', contacts),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
