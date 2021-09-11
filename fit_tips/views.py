from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FitTipForm
from .models import FitTip
from django.contrib.auth.models import User
from products.models import Product


# Create your views here.

def all_fit_tips(request):

    fit_tips = FitTip.objects.all().order_by('-date')
    products = Product.objects.all()

    context = {
        'fit_tips': fit_tips,
        'products': products,
    }

    return render(request, 'fit_tips/fit_tips.html', context)


@login_required
def add_fit_tip(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Oops! Only signed in users can leave a fit tip')
        return redirect(reverse('home'))
    product = Product.objects.get(id=request.POST['products'])

    if request.user.is_authenticated:
        if request.method == "POST":
            fit_tip = FitTip.objects.create(fit_tip_title=request.POST.get('fit_tip_title'), fit_tip=request.POST.get('fit_tip'), user=request.user, product=product)
            messages.success(request, "You've left a fit tip! Thank you")
            return redirect('fit_tips')
        else:
            context = {
                'product': product,
            }
        return render(request, 'fit_tips/fit_tips.html', context)
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


@login_required
def delete_fit_tip(request, fit_tip_id):
    if request.user.is_authenticated:
        fit_tip = get_object_or_404(FitTip, pk=fit_tip_id)

        if request.user == fit_tip.user:
            fit_tip.delete()
            messages.success(request, 'Review has been deleted')
        return redirect('fit_tips')
    else:
        return redirect('account_login')
