import pytest
from store_app.forms import ProductModelForm


@pytest.mark.django_db
def test_product_modelform_valid():
    form_data = {"name": "New shit", "description": "Some kind of shit", "price": 69}
    form = ProductModelForm(data=form_data)

    assert form.is_valid()
