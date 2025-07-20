from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib import messages
from .models import Product, Category, Comment
from .forms import ProductModelForm
from .tasks import logging_new_product


class IndexTemplateView(TemplateView):
    template_name = "store_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        context["description"] = "Главная страница сайта с информацией о товарах."
        return context


class AboutTemplateView(TemplateView):
    template_name = "store_app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Страница о нас"
        context["description"] = "Страница сайта с информацией о компаниях."
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "store_app/product_detail.html"
    context_object_name = "product"

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.views = getattr(product, "view", 0) + 1
        product.save(update_fields=["views"])
        return super().get(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = "store_app/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.GET.get("price")

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        return queryset


class ProductCreateView(CreateView):
    model = Product
    template_name = "store_app/add_product.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно создан")
        logging_new_product.delay()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "store_app/edit_product.html"
    form_class = ProductModelForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        messages.success(self.request, "Товар успешно обновлен")
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "store_app/delete_product.html"
    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление продукта"
        context["description"] = "Вы уверены, что хотите удалить этот продукт?"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Товар успешно удален")
        return super().form_valid(form)


class CategoriesView(ListView):
    model = Category
    template_name = "store_app/categories_list.html"
    context_object_name = "categories"
