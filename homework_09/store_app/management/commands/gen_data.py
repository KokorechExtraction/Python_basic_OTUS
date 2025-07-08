from django.core.management.base import BaseCommand
from store_app.models import Product, Category, Author, Comment, Tag
from faker import Faker
import random


class Command(BaseCommand):
    help = "Генерация тестовых данных Product, Category, Author, Comment, Tag"

    def handle(self, *args, **kwargs):
        self.stdout.write("Начинается генерация данных")

        fake = Faker()

        authors = []
        for _ in range(8):
            author_name = fake.name()
            author = Author.objects.create(name=author_name)
            authors.append(author)

        tags = []
        for _ in range(10):
            tag_name = fake.sentence(nb_words=1)
            tag = Tag.objects.create(
                name=tag_name,
            )
            tags.append(tag)

        categories = []
        for _ in range(8):
            category_name = fake.sentence(nb_words=1)
            category_description = fake.text(max_nb_chars=200)
            category = Category.objects.create(
                name=category_name,
                description=category_description,
            )
            categories.append(category)

        products = []
        for _ in range(10):
            product_name = fake.sentence(nb_words=2)
            product_description = fake.text(max_nb_chars=50)
            product_category = random.choice(categories)
            product_price = random.randint(1, 299)
            product_tag = random.choice(tags)
            product = Product.objects.create(
                name=product_name,
                description=product_description,
                price=product_price,
                category=product_category,
            )
            products.append(product)

        for product in products:
            product.tags.add(random.choice(tags))
            product.tags.add(random.choice(tags))
            product.tags.add(random.choice(tags))

        comments = []
        for _ in range(20):
            comment_text = fake.text(max_nb_chars=100)
            comment_author = random.choice(authors)
            comment_product = random.choice(products)
            comment = Comment.objects.create(
                text=comment_text,
                product=comment_product,
                author=comment_author,
            )
            comments.append(comment)

        self.stdout.write(f"Создано {len(comments)} комментариев")
