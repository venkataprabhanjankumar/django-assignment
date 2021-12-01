from django.contrib.auth.decorators import login_required
from users.models import UserModel
from .forms import ProductsForm
from .models import Products
from django.shortcuts import render, redirect


@login_required(login_url='/login')
def list_products(request):
    user = UserModel.objects.get(username=request.user.username)
    products = Products.objects.filter(user=user)
    return render(request, 'products.html', {'products': products})


@login_required(login_url='/login')
def new_product(request):
    user = UserModel.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = user.username
            product.save()
            return redirect('/products/list')
    else:
        form = ProductsForm()
        return render(request, 'new_product.html', {'form': form})


@login_required(login_url='/login')
def edit_product(request, pid):
    instance = Products.objects.get(id=pid)
    if request.method == 'POST':
        form = ProductsForm(instance=instance, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/list')
    else:
        form = ProductsForm(instance=instance)
        return render(request, 'edit_product.html', {'form': form})


@login_required(login_url='/login')
def delete_product(request, pid):
    Products.objects.get(id=pid).delete()
    return redirect('/products/list')
