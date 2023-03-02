from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Cart:
    def __init__(self, request):
        self.request = request

        self.session = request.session

        cart = self.session.get("cart")

        if not cart:
            self.session["cart"] = {}
            cart = self.session["cart"]

        self.cart = cart

    def add(self, product, quantity=1, replace=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0}
        if replace:
            self.cart[product_id]["quantity"] = quantity
            messages.success(self.request, _("cart updated successfully !"))
        else:
            self.cart[product_id]["quantity"] += quantity
            messages.success(self.request, _("product added to cart successfully !"))

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.error(self.request, _("product removed from cart successfully !"))
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product_obj"] = product

        for item in cart.values():
            item["total_price"] = item["product_obj"].price * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())
        # return len(self.cart.keys())  # for number of products

    def clear(self):
        del self.session["cart"]
        self.save()

    def get_total_price(self):
        return sum([item["quantity"] * item["product_obj"].price for item in self.cart.values()])

