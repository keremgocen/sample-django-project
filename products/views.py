from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


def index(request):
    product_list = Product.objects.order_by('price')
    context = {'product_list': product_list}
    return render(request, 'products/index.html', context)


class ProductsView(generics.ListAPIView):
    """
    API endpoint that lists all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("product does not exist")
    return HttpResponse("{} {} {}".format(product.name, product.description, product.price))
