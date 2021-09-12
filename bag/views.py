from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    weight = None

    if "product_weight" in request.POST:
        weight = request.POST["product_weight"]
    bag = request.session.get("bag", {})

    if weight:
        if item_id in list(bag.keys()):
            if weight in bag[item_id]["items_by_weight"].keys():
                bag[item_id]["items_by_weight"][weight] = quantity
                messages.success(
                    request,
                    f'Updated weight {weight}kg {product.name} '
                    f'quantity to {bag[item_id]["items_by_weight"][weight]}'
                    ' to your bag',
                )
            else:
                bag[item_id]["items_by_weight"][weight] = quantity
                messages.success(
                    request,
                    f'Added weight {weight}kg {product.name}'
                    ' to your bag'
                )
        else:
            bag[item_id] = {"items_by_weight": {weight: quantity}}
            messages.success(
                request, f"Added weight {weight}kg {product.name} to your bag"
            )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] = quantity
            messages.success(
                request, f'Updated the quantity of {product.name}'
                'to {bag[item_id]}'
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)


def change_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    weight = None

    if "product_weight" in request.POST:
        weight = request.POST["product_weight"]
    bag = request.session.get("bag", {})

    if weight:
        if quantity > 0:
            bag[item_id]["items_by_weight"][weight] = quantity
            messages.success(
                request,
                f'Updated weight {weight}kg {product.name} quantity to '
                f'{bag[item_id]["items_by_weight"][weight]} to your bag',
            )

        else:
            del bag[item_id]["items_by_weight"][weight]
            if not bag[item_id]["weight"]:
                bag.pop(item_id)
                messages.success(
                    request, f'Removed weight {weight} {product.name}'
                             f'from your bag'
                )

    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
            messages.success(request, f"Removed {product.name} from your bag")

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):

    try:
        product = get_object_or_404(Product, pk=item_id)
        weight = None

        if "product_weight" in request.POST:
            weight = request.POST["product_weight"]
        bag = request.session.get("bag", {})

        if weight:
            del bag[item_id]["items_by_weight"][weight]
            if not bag[item_id]["items_by_weight"]:
                bag.pop(item_id)
                messages.success(
                    request, f'Removed weight {weight}kg'
                              f' {product.name} from your bag'
                )

        else:
            bag.pop(item_id)
            messages.success(request, f"Removed {product.name} from your bag")

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing {e}")
        return HttpResponse(status=500)
