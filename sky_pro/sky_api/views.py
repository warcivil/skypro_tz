from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from .forms import ProductForm
from .models import Product
import django.views.generic


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    form_class = ProductForm