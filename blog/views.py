from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog
