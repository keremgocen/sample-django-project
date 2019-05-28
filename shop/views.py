from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404

from .models import Product


def index(request):
    product_list = Product.objects.order_by('price')
    context = {'product_list': product_list}
    return render(request, 'shop/index.html', context)


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("product does not exist")
    return HttpResponse("{} {} {}".format(product.name, product.description, product.price))
