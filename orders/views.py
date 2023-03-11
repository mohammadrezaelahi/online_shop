from django.shortcuts import render

from .forms import OrderForm


def order_create_view(request):
    order_form = OrderForm()

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

    return render(request, "orders/order_create.html", {
        "form": order_form,
    })
