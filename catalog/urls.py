from django.urls import path

from catalog.views import contacts, product

urlpatterns = [
    path('', product),
    path('contacts/', contacts)
]
