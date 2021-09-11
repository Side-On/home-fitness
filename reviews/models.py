from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=254, null=False, blank=False)
    review_comment = models.TextField(max_length=800, null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review made by {self.user} about the {self.product.name}'
