from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/generator/generate/list-items",
        views.generate_list_items,
        name="generate_list_items",
    ),
]
