from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexTemplateView.as_view(), name="index"),
    path("about/", views.AboutTemplateView.as_view(), name="about"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/add/", views.ProductCreateView.as_view(), name="add_product"),
    path(
        "products/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"
    ),
    path(
        "products/<int:pk>/edit/",
        views.ProductUpdateView.as_view(),
        name="edit_product",
    ),
    path(
        "products/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="delete_product",
    ),
    path("categories/", views.CategoriesView.as_view(), name="category_list"),
]
