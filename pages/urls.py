from django.urls import path

from products import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
]
