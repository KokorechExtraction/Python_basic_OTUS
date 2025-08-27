import pytest
from store_app.models import Product, Category


@pytest.mark.django_db
def test_category_create(category):
    assert Category.objects.count() == 1
    assert category.name == "Тестовая категория"
    assert str(category) == "Тестовая категория"


@pytest.mark.django_db
def test_product_create(product):
    assert Product.objects.count() == 1
    assert product.name == "Тестовый продукт"
    assert str(product) == "Тестовый продукт"
    assert product.price == 69


@pytest.mark.django_db
def test_product_update(product, product2):
    product.name = "Измененный тестовый продукт"
    product.description = "Описание измененного тестового продукта"
    product.save()
    assert product.name == product2.name
    assert product.description == product2.description


@pytest.mark.django_db
def test_product_update(product, product2):
    product.delete()
    assert Product.objects.count() == 1


@pytest.mark.django_db
def test_product_get(product):
    product_get = Product.objects.get(pk=product.pk)

    assert product_get.name == "Тестовый продукт"
