from django import forms
from django.core.exceptions import ValidationError

from store_app.models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "tags"]
        labels = {
            "name": "Наименование",
            "description": "Описание",
            "price": "Цена",
            "category": "Категория",
            "tags": "Тэги",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите наименование товара",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите описание товара",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise ValidationError("Наименование должно быть не менее 3 символов")
        return name

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price == 301:
            raise ValidationError(
                "Цена не может быть 300, по идеологическим соображениям"
            )
        return price

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        forbidden_words = ["беспонтовый", "пирожок"]

        if description:
            for word in forbidden_words:
                if word in description.lower():
                    raise ValidationError(f"В контексте не должно быть слова {word}")
