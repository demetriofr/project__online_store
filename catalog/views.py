from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product, Category


# Create your views here.


# FBV
# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Каталог'
#     }
#     return render(request, 'catalog/base.html', context)


# FBV
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


# CBV
# class Contacts():
#     pass

# CBV
class ProductListView(ListView):
    model = Product


# FBV
# def product(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Товары'
#     }
#
#     return render(request, 'catalog/product_list.html', context)


# FBV
class CategoryListView(ListView):
    model = Category
