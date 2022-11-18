from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import orderForm
from users.models import Seller, User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        fio = request.user.fio
    else:
        fio = ''
    if request.user.account_type == 's':
        a = 'Создать объявление'
    data = Order.objects.all()
    context = {'data':data,
    'fio':fio,
    'a':a
    }
    return render(request, './home.html', context)

def createOrder(request):
    if request.user.account_type == 's':
        if request.method == 'GET':
            return render(request, './createorder.html', {'form':orderForm})
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