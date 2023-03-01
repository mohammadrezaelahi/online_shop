from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        # product_id = int(self.kwargs["pk"])
        # product = get_object_or_404(Product, pk=product_id)
        # fee = product.price + ((product.price * 10) / 100)
        # context["fee"] = fee
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs["product_id"])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product
        messages.success(self.request, _("comment added successfully ."))
        return super().form_valid(form)

# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     fee = product.price + ((product.price*10) / 100)
#     comments = product.comments.all().filter(active=True).order_by("-datetime_created")
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.product = product
#             new_comment.author = request.user
#             new_comment.save()
#             form = CommentForm()
#             return redirect("product_list")
#     else:
#         form = CommentForm()
#
#     return render(request, "products/product_detail.html", {"product": product,
#                                                             "comments": comments,
#                                                             "form": form,
#                                                             "fee": fee})
