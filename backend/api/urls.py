from django.urls import path
from .views import home


urlpatterns = [
    path("", home, name="home"),
    path("products/", include("products.urls")),
]