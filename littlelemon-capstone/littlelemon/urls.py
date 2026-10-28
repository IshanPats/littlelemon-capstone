from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from restaurant import views

router = routers.DefaultRouter()
router.register(r"tables", views.BookingViewSet, basename="tables")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("restaurant/booking/", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
