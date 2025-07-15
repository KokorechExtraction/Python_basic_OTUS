import pytest
from store_app.models import Product, Category, Tag


@pytest.fixture
def category():
    return Category.objects.create(name="Тестовая категория")


@pytest.fixture
def product(category):
    return Product.objects.create(
        name="Тестовый продукт",
        description="Описание тестового продукта",
        price=69,
        category=category,
    )


@pytest.fixture
def product2(category):
    return Product.objects.create(
        name="Измененный тестовый продукт",
        description="Описание измененного тестового продукта",
        price=69,
        category=category,
    )


@pytest.fixture
def tag():
    return Tag.objects.create(name="Тестовый тэг")
