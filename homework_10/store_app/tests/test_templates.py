import pytest
from django.urls import reverse
from bs4 import BeautifulSoup

from tests_and_shit.session_2025_01.lesson_17.http_server import response


@pytest.mark.django_db
def test_product_template(client, category, product):
    url = reverse("product_list")
    response = client.get(url)

    assert response.status_code == 200

    soup = BeautifulSoup(response.content, "html.parser")

    assert soup.h3.text == "Тестовый продукт"

    titles = [h3.get_text() for h3 in soup.find_all("h3")]

    assert "Тестовый продукт" in titles

    assert soup.find("h1", text="Список товаров")
