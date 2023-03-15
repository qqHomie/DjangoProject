from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from django.core.paginator import Paginator
import sys
sys.path.append('/Users/TUF F15/Documents/Study/3-course/Spring/Django/Project/store/users')
from users .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        'title': 'storeApp',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'storeProducts/index.html', context)


def products(request, category_id=None):
    if category_id:
        category = ProductCategory.objects.get(id = category_id)
        products = Product.objects.filter(category = category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title' : 'storeApp',
        'products' : products,
        'page_obj': page_obj,
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'storeProducts/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])