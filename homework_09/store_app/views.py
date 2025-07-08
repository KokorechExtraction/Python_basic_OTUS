from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Comment
from .forms import ProductModelForm


def index(request):
    return render(request, "store_app/index.html")


def about(request):
    return render(request, "store_app/about.html")


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product)
    tags = product.tags.all()

    context = {
        "product": product,
        "title": product.name,
        "comments": comments,
        "tags": tags,
    }
    return render(request, "store_app/product_detail.html", context=context)


def product_list(request):
    products = Product.objects.all()
    context = {"products": products, "title": "Список всех постов"}
    return render(request, "store_app/product_list.html", context=context)


def add_product(request):
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductModelForm()

    context = {"form": form, "title": "Добавить продукт"}
    return render(request, "store_app/add_product.html", context=context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductModelForm(instance=product)

    context = {"form": form, "title": "Редактировать продукт"}
    return render(request, "store_app/edit_product.html", context=context)


def categories_list(request):
    categories = Category.objects.all()
    context = {"categories": categories, "title": "Список всех категорий"}
    return render(request, "store_app/categories_list.html", context=context)
