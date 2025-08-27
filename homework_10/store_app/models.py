from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )

    tags = models.ManyToManyField("Tag", related_name="products")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    bio = models.TextField()
    website = models.URLField(blank=True, null=True)
    author = models.OneToOneField(
        "Author", on_delete=models.CASCADE, related_name="profile"
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, related_name="comments"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="product"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
