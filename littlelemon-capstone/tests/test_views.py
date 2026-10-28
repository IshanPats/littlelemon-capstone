from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import TestCase

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        Menu.objects.create(title="Greek Salad", price=12.50, inventory=20)
        Menu.objects.create(title="Bruschetta", price=7.99, inventory=30)
        Menu.objects.create(title="Lemon Dessert", price=5.00, inventory=15)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_requires_token(self):
        response = APIClient().get("/restaurant/menu/")
        self.assertEqual(response.status_code, 401)
