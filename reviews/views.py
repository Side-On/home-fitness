from django.shortcuts import render, redirect, reverse, get_object_or_404
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
                review = form.save(commit=False)
                review.user = request.user
                review.title = request.POST['review_title']
                review.comment = request.POST['review_comment']
                review.product = product
                review.save()
                messages.success(request, "You've left a review! Thank you")
                return redirect('product_detail', product.id)
        else:
            form = UserReviewForm()
        return render(request, 'products/product_detail.html', {"form": form})
    else:
        messages.error(request, 'Oops! You need to be signed in to leave a review')
        return redirect('product_details', product_id)


@login_required
def edit_review(request, product_id, review_id):

    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        review = get_object_or_404(Review, product=product, pk=review_id)

        if request.user == review.user or request.user.is_superuser:
            if request.method == "POST":
                form = UserReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    messages.success(request, "You've edited this review")
                    return redirect('product_detail', product_id)
            else:
                form = UserReviewForm(instance=review)
            return render(request, 'reviews/edit_review.html', {'form': form})
        else:
            messages.error(request, "Sorry you don't have permission to edit this review")
            return redirect('product_detail', product_id)
    else:
        return redirect('account_login')


@login_required
def delete_review(request, product_id, review_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        review = get_object_or_404(Review, product=product, pk=review_id)
        
        if request.user == review.user:
            review.delete()
            messages.success(request, 'Review has been deleted')
        return redirect('product_detail', product_id)
    else:
        return redirect('account_login')
