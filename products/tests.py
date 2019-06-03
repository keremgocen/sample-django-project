from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from products.models import Product
from products.serializers import ProductSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_product(name="", description=""):
        if name != "" and description != "":
            Product.objects.create(name=name, description=description)

    def setUp(self):
        # add test data
        self.create_product("p1", "product 1")
        self.create_product("p2", "product 2")


class GetAllProductsTest(BaseViewTest):

    def test_get_all_products(self):
        """
        This test ensures that all products added in the setup method
        exist when we make a GET request to the products/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("products-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Product.objects.all()
        serialized = ProductSerializer(expected, many=True)
        self.assertEqual(response.data['results'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
