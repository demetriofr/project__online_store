from django.urls import path

from catalog.views import home, contacts, product

urlpatterns = [
    path('', product),
    path('contacts/', contacts)
]
