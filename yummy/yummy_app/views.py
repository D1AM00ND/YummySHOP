from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import Registration, BuyForm
from .models import *


def home(request):
    types = TypeOfProduct.objects.all()

    context = {}
    for type in types:
        products = Product.objects.filter(type=type)
        context[type] = products[0:3]

    return render(request, 'home.html', {'context': context, 'categories': types})


def details(request, id):
    types = TypeOfProduct.objects.all()

    product = Product.objects.get(id=id)
    return render(request, 'details.html', {"product": product, 'categories': types})


def category(request, id):
    types = TypeOfProduct.objects.all()

    products = Product.objects.filter(type=id)
    type = products[0].type.type
    return render(request, 'category.html', {"products": products, "type": type, 'categories': types})


def profile(request):
    types = TypeOfProduct.objects.all()

    return render(request, 'profile.html', {'categories': types})


def aboutus(request):
    types = TypeOfProduct.objects.all()

    return render(request, 'aboutus.html', {'categories': types})


def search(request):
    types = TypeOfProduct.objects.all()

    products = Product.objects.filter(name__icontains=request.POST.get("name"))
    if products:
        return render(request, 'search.html', {"products": products, "query": request.POST.get("name")})
    else:
        return render(request, 'nofind.html', {'categories': types})


def registration(request):
    types = TypeOfProduct.objects.all()

    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Registration()
    return render(request, 'registration/registration.html', {"form": form, 'categories': types})





def cart(request):
    types = TypeOfProduct.objects.all()

    context = []

    if 'cart' in request.session.keys():
        for item in request.session['cart']:
            item_id = item.get('id')
            product = Product.objects.get(id=item_id)
            context.append(product)
    else:
        return render(request, 'cart/empty.html', {'categories': types})

    if len(context) == 0:
        return render(request, 'cart/empty.html', {'categories': types})
    else:
        total_sum = get_total_price(request, context)
        return render(request, 'cart/cart.html', {"cart": context, "total_sum": total_sum, 'categories': types})


def add(request, id):
    if request.method == 'POST':
        if not request.session.get('cart'):
            request.session['cart'] = []
        else:
            request.session['cart'] = list(request.session['cart'])

        added_data = {
            'id': id,
        }

        request.session['cart'].append(added_data)
        request.session.modified = True

    return redirect("/")


def remove(request, id):
    if request.method == 'POST':
        for item in request.session['cart']:
            if item['id'] == id:
                item.clear()
                break

        clear_remains(request)

    return redirect("/cart/")


def remove_all(request):
    for item in request.session['cart']:
        item.clear()

    clear_remains(request)

    return redirect('/cart/')


def clear_remains(request):
    while {} in request.session['cart']:
        request.session['cart'].remove({})

    if not request.session['cart']:
        del request.session['cart']

    request.session.modified = True


def get_total_price(request, context):
    total_sum = 0

    for item in context:
        total_sum += item.price

    return total_sum


def buy(request):
    types = TypeOfProduct.objects.all()

    if request.method == "POST":
        form = BuyForm(request.POST)
        if form.is_valid():
            return redirect('thanks')
    else:
        form = BuyForm()

    return render(request, 'buy.html', {'categories': types, 'form': form})


def thanks(request):
    types = TypeOfProduct.objects.all()

    remove_all(request)
    return render(request, 'thanks.html', {'categories': types})