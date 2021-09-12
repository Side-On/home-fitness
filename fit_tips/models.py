from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class FitTip(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="fit_tips")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fit_tip_title = models.CharField(max_length=100, null=False, blank=False)
    fit_tip = models.TextField(max_length=400, null=False, blank=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Fit tip left by {self.user} on {self.product}'
