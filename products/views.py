from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm
from reviews.models import Review
from fit_tips.models import FitTip


# Create your views here.


def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    page_type = 'default'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey == 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:

            category_string = request.GET['category']
            if category_string == 'treadmills,rowing_machines,bikes':
                page_type = 'cardio'

            if category_string == 'bars,dumbells,kettlebells':
                page_type = 'weights'

            if category_string == 'protein_bars,gels':
                page_type = 'diet'

            if category_string == 'yoga_mats,skipping_ropes':
                page_type = 'accessories'

            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter your search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                                                   description__icontains=query
                                                   ) | Q(
                                                         brand__icontains=query
                                                         ) | Q(
                                                               category__name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'page_type': page_type,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id).order_by('-date')

    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, '
                       'you can only do that if you are an admin')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Succesfully added the product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add the product. '
                           'Please check that the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you can only do '
                       'that if you are an admin')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update the product.'
                           ' Please make sure that the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you can only do that'
                       ' if you are an admin')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
