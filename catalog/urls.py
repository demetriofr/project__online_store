from django.urls import path

from catalog.views import contacts, ProductListView, CategoryListView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category'),
    # path('', product),
    path('contacts/', contacts)
]
