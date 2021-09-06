from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserReviewForm
from .models import Review
from django.contrib.auth.models import User
from products.models import Product


# Create your views here.

@login_required
def add_review(request, product_id):
    product = Product.objects.get(id=product_id)
    if not request.user.is_authenticated:
        messages.error(request, 'Oops! Only signed in users can leave a review')
    return redirect(reverse('home'))

    if request.user.is_authenticated:
        if request.method == "POST":
            form = UserReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                review.user = request.user
                review.title = request.POST['title']
                review.comment = request.POST['comment']
                review.product = product
                review.save()
                messages.success(request, "You've left a review! Thank you")
                return redirect('product_details', product_id)
        else:
            form = UserReviewForm()

    else: 
        messages.error(request, 'Oops! You need to be signed in to leave a review')
        return redirect('product_details', product_id)