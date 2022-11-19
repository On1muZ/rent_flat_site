from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import orderForm
from users.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        a = ''
        fio = request.user.fio
        if request.user.account_type == 's':
            a = 'Создать объявление'
    else:
        fio = ''
        a = ''
    data = Order.objects.all()
    context = {'data':data,
    'fio':fio,
    'a':a
    }
    return render(request, './home.html', context)

def createOrder(request):
    a = ''
    if request.user.account_type == 's':
        if request.method == 'GET':
            return render(request, './createorder.html', {'form':orderForm,
            'a':a
            })
        else:
            author = User.objects.get(username = request.user)
            model = Order(
                title = request.POST['title'],
                adress = request.POST['adress'],
                desc = request.POST['desc'],
                price = request.POST['price'],
                author = author,
                img_outside = request.FILES.get('img_outside'),
                img_inside = request.FILES.get('img_inside')
            )
            model.save()
            return redirect('home')
    else:
        return redirect('home')

def vieworder(request, order_id):
    a = ''
    order = get_object_or_404(Order, pk = order_id)
    return render(request, './vieworder.html', {'order':order,
    'a':a
    })

def myorders(request, user_id):
    if request.user.account_type == 's':
        a = 'Создать объявление'
        user = get_object_or_404(User, pk = user_id)
        if user.id != request.user.id:
            return redirect('home')
        else:
            orders = Order.objects.filter(author = user)
            return render(request, './myorders.html', {'orders':orders,
            'a':a})
    else:
        return redirect('home')
    
def isarendated(request, user_id, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk = order_id)
        user = get_object_or_404(User, pk = user_id)
        if user == request.user:
            order = Order.objects.filter(id = order_id).update(is_arendated = True)
            return redirect('home')
        else:
            return redirect('home')

def isnotarendated(request, user_id, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk = order_id)
        user = get_object_or_404(User, pk = user_id)
        if user == request.user:
            order = Order.objects.filter(id = order_id).update(is_arendated = False)
            return redirect('home')
        else:
            return redirect('home')