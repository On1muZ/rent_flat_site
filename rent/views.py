from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Comment
from .forms import orderForm
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

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

@login_required(login_url='loginuser')
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
    if request.method == 'GET':
        a = ''
        if request.user.is_authenticated:
            if request.user.account_type == 's':
                a = 'Создать объявление'
        order = get_object_or_404(Order, pk = order_id)
        comments = Comment.objects.filter(post = order).order_by('-date_time')
        return render(request, './vieworder.html', {'order':order,
        'a':a,
        'comments':comments
        })
    else:
        a = ''
        if request.user.is_authenticated:
            if request.user.account_type == 's':
                a = 'Создать объявление'
        order = get_object_or_404(Order, pk = order_id)
        comment = Comment(post = order, author = request.user, text = request.POST['text'])
        comment.save()
        comments = Comment.objects.filter(post = order).order_by('-date_time')
        return HttpResponseRedirect(request.path_info)

@login_required(login_url='loginuser')
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

@login_required(login_url='loginuser')
def isarendated(request, user_id, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk = order_id)
        user = get_object_or_404(User, pk = user_id)
        if user == request.user:
            order = Order.objects.filter(id = order_id).update(is_arendated = True)
            return redirect('home')
        else:
            return redirect('home')

@login_required(login_url='loginuser')
def isnotarendated(request, user_id, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk = order_id)
        user = get_object_or_404(User, pk = user_id)
        if user == request.user:
            order = Order.objects.filter(id = order_id).update(is_arendated = False)
            return redirect('home')
        else:
            return redirect('home')

@login_required(login_url='loginuser')
def deleteorder(request, user_id, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk = order_id)
        user = get_object_or_404(User, pk = user_id)
        if user == order.author or request.user.is_staff:
            order = Order.objects.get(id = order_id)
            order.delete()
            return redirect('home')
        else:
            return redirect('home')

def deletecomment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk = comment_id)
        comment.delete()
        return redirect('home')
    else:
        return redirect('home')

