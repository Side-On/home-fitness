from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FitTipForm
from .models import FitTip
from django.contrib.auth.models import User
from products.models import Product


# Create your views here.

@login_required
def add_fit_tip(request, product_id):
    product = Product.objects.get(id=product_id)
    if not request.user.is_authenticated:
        messages.error(request, 'Oops! Only signed in users can leave a tip!')
        return redirect(reverse('home'))

    if request.user.is_authenticated:
        if request.method == "POST":
            form = FitTipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.user = request.user
                tip.title = request.POST['fit_tip_title']
                tip.comment = request.POST['fit_tip']
                tip.product = product
                tip.save()
                messages.success(request, "You've left a tip! Thank you")
                return redirect('product_detail', product.id)
        else:
            form = FitTipForm()
        return render(request, 'products/product_detail.html', {"form": form})
    else:
        messages.error(request, 'Oops! You need to be signed in to leave a tip')
        return redirect('product_details', product_id)
