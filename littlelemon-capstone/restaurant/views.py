from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


# Static HTML page
def index(request):
    return render(request, "index.html", {})


# Menu API
class MenuItemsView(generics.ListCreateAPIView):
    """GET: list all menu items.  POST: create a menu item."""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """GET, PUT, PATCH and DELETE a single menu item."""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


# Table booking API
class BookingViewSet(viewsets.ModelViewSet):
    """Full CRUD for table bookings. Requires a token."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

