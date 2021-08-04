from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Item(models.Model):

    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=25, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
