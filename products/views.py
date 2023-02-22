from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product
from .forms import CommentForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = "products/product_list.html"
    context_object_name = "products"


# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = "products/product_detail.html"
#     context_object_name = "product"

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all().order_by("-datetime_created")
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            form = CommentForm()
            return redirect("product_list")
    else:
        form = CommentForm()

    return render(request, "products/product_detail.html", {"product": product,
                                                            "comments": comments,
                                                            "form": form})
