from django.shortcuts import render
from .models import Item,Order
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import OrderForm

# from .forms import SchoolForm

# Create your views here.
def orders(request):
    data = Order.objects.all()
    params = {
        'data': data,
        'Item': Item
    }
    return render(request, 'order/index.html', params)

@login_required()
def items(request):
    data = Item.objects.all()
    params = {
        'data': data,
    }
    # if request.user.is_authenticated:
    #     return render(request, 'item/index.html', params)
    # else:
    #     return render(request, 'order/index.html', params)
    return render(request, 'item/index.html', params)
    

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def create_order(request):

    if (request.method == 'POST'):
        current_user=request.user
        item_id = request.POST['item_id']
        quantity = request.POST['quantity']
        obj = current_user.orders.create(item_id=item_id)
        
        # order = OrderForm(request.POST, instance=obj)
        # order.save()
        return redirect('orders')
    else:
        items=Item.objects.all().order_by('created_at')
        params = {
            'form': OrderForm(),
            'items': items
        }
        return render(request, 'order/create.html', params)