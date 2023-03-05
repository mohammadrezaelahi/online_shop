from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=100)
    description = RichTextField(verbose_name=_("description"))
    short_description = models.CharField(verbose_name=_("short description"), max_length=400)
    price = models.PositiveIntegerField(verbose_name=_("price"))
    active = models.BooleanField(verbose_name=_("active"), default=True)
    image = models.ImageField(verbose_name=_("product image"), upload_to="product/product_cover/", blank=True)

    datetime_created = models.DateTimeField(verbose_name=_("date created"), default=timezone.now)
    datetime_modified = models.DateTimeField(verbose_name=_("date modified"), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ("1", _("very bad")),
        ("2", _("bad")),
        ("3", _("normal")),
        ("4", _("good")),
        ("5", _("very good")),
    ]
    author = models.ForeignKey(
        get_user_model(),
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name=_("comment author")
    )
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(verbose_name=_("comment text"))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_("what is your score?"))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def __str__(self):
        return f"{self.author} : {self.product}"

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
