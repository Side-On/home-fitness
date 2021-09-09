from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FitTipForm
from .models import FitTip
from django.contrib.auth.models import User
from products.models import Product


# Create your views here.

def all_fit_tips(request):

    fit_tips = FitTip.objects.all()
    products = Product.objects.all()

    context = {
        'fit_tips': fit_tips,
        'products': products,
    }

    return render(request, 'fit_tips/fit_tips.html', context)


@login_required
def add_fit_tip(request, product_id):

    if not request.user.is_authenticated:
        messages.error(request, 'Oops! Only signed in users can leave a fit tip')
        return redirect(reverse('home'))
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        if request.method == "POST":
            form = FitTipForm(instance=product)
            if form.is_valid():
                fit_tip = form.save(commit=False)
                fit_tip.user = request.user
                fit_tip.title = request.POST['fit_tip_title']
                fit_tip.comment = request.POST['fit_tip']
                fit_tip.product = product
                fit_tip.save()
                messages.success(request, "You've left a fit tip! Thank you")
                return redirect('fit_tips', product.id)
        else:
            context = {
                'form': form,
                'product': product,
            }
        return render(request, 'fits_tips/fit_tips.html', context)
    else:
        messages.error(request, 'Oops! You need to be signed in to leave a fit tip')
        return redirect('account_login')



@login_required
def edit_fit_tip(request, fit_tip_id):

    if request.user.is_authenticated:
        fit_tip = FitTip.objects.get(id=fit_tip_id)

        if request.user == fit_tip.user or request.user.is_superuser:
            if request.method == "POST":
                form = FitTipForm(request.POST, instance=fit_tip)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    messages.success(request, "You've edited this fit tip")
                    return redirect('fit_tips')
            else:
                form = FitTipForm(instance=fit_tip)
            return render(request, 'fit_tips/edit_fit_tip.html', {'form': form})
        else:
            messages.error(request, "Sorry you don't have permission to edit this fit tip")
            return redirect('fit_tips')
    else:
        return redirect('account_login')

