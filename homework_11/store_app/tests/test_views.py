import pytest
from django.urls import reverse


def test_index_view(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200
    assert "<h1>{{ title }}</h1>" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_product_list_view(client, category, product):
    url = reverse("product_list")
    response = client.get(url)

    assert response.status_code == 200

    assert product.name.encode("utf-8") in response.content
    assert category.name.encode("utf-8") in response.content
