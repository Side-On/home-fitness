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


@login_required
def edit_fit_tip(request, product_id, fit_tip_id):

    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        fit_tip = get_object_or_404(FitTip, product=product, pk=fit_tip_id)

        if request.user == fit_tip.user or request.user.is_superuser:
            if request.method == "POST":
                form = FitTipForm(request.POST, instance=fit_tip)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    messages.success(request, "You've edited this tip")
                    return redirect('product_detail', product_id)
            else:
                form = FitTipForm(instance=fit_tip)
            return render(request, 'fit_tips/edit_fit_tip.html', {'form': form})
        else:
            messages.error(request, "Sorry you don't have permission to edit this fit tip")
            return redirect('product_detail', product_id)
    else:
        return redirect('account_login')

@login_required
def delete_fit_tip(request, product_id, fit_tip_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        fit_tip = get_object_or_404(FitTip, product=product, pk=fit_tip_id)
        
        if request.user == fit_tip.user:
            fit_tip.delete()
            messages.success(request, 'Fit tip has been deleted')
        return redirect('product_detail', product_id)
    else:
        return redirect('account_login')
