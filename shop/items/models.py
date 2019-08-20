from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=150)
    pid = models.ForeignKey('Category', null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.TextField(max_length=150)
    price = models.FloatField()
    available = models.BooleanField()

    def __str__(self):
        return self.name
