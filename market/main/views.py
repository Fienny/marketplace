from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from .models import Product, Category, Seller


class ProductList(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_seller'] = not self.request.user.groups.filter(name='Sellers').exists()
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'product_view.html'
    context_object_name = 'product'
    queryset = Product.objects.all()


class ProductCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('main.add_product', 'main.change_product', 'main.delete_product')
    model = Product
    fields = ['name', 'description', 'images', 'tags', 'quantity', 'category']
    success_url = reverse_lazy('products')
    template_name = "product_create.html"

    def form_valid(self, form):
        form.instance.seller = Seller.objects.get(user=self.request.user.id)
        messages.success(self.request, "The product was created successfully.")
        messages.error(self.request, 'Please correct the following errors:')
        return super(ProductCreate, self).form_valid(form)


class ProductDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    permission_required = ('main.add_product', 'main.change_product', 'main.delete_product')
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products')


class ProductUpdate(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    permission_required = ('main.add_product', 'main.change_product', 'main.delete_product')
    model = Product
    fields = '__all__'
    template_name = 'product_update.html'
    success_url = reverse_lazy('products')


class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories')
    template_name = "category_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The category was created successfully.")
        messages.error(self.request, 'Please correct the following errors:')
        return super(CategoryCreate, self).form_valid(form)


class CreateSeller(LoginRequiredMixin, CreateView):
    model = Seller
    fields = ['name', 'num_of_goods']
    success_url = reverse_lazy('products')
    template_name = "seller_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "You have become seller!")
        messages.error(self.request, 'Please correct the following errors:')
        return super(CreateSeller, self).form_valid(form)


def category_view(request, category_pk):
    category = Category.objects.get(pk=category_pk)
    products = Product.objects.filter(category=category)

    return render(request, "category.html", {
        "products": products,
        "category": category,
    })
