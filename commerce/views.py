from django.shortcuts import render
from django.views.generic import ListView
from commerce.models import Product
# Create your views here.
class ProductListView(ListView):
    template_name = 'commerce/productlist.html'
    model = Product