from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect


from .cart import Cart
from products.models import Product
from .forms import AddToCardProductForm


def cart_detail_view(request):

    cart = Cart(request)
    for item in cart:
        item["product_update_quantity_form"] = AddToCardProductForm(initial={
            "quantity": item["quantity"],
            "inplace": True,
        })

    return render(request, "cart/cart_detail.html", {
        "cart": cart,
    })


def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCardProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data["quantity"]
        replace = cleaned_data["inplace"]
        cart.add(product, quantity, replace)

    return redirect("cart:cart_detail")


def remove_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")

