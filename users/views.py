from django.shortcuts import render
from .forms import CustomUserCreationForm
from .models import User, Seller, Buyer
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError

def signupuser(request):
    if request.method == 'GET':
        return render(request, './signupuser.html', {
            'form':CustomUserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user_object = User.objects.create_user(
                    username = request.POST['username'],
                    phone = request.POST['phone'],
                    fio = request.POST['fio'],
                    password = request.POST['password1'],
                    account_type = request.POST['account_type'])
                user_object.save()
                login(request, user_object)
                if user_object.account_type == 's':
                    model = Seller(user = user_object)
                    model.save()
                else:
                    model = Buyer(user = user_object)
                    model.save()
                return redirect('home')
            except IntegrityError:
                return render(request, './signupuser.html', {'form':CustomUserCreationForm(), 'error': 'Это имя пользователя занято, пожалуйста попробуйте другое.'})
        else:
            return render(request, './signupuser.html', {
            'form':CustomUserCreationForm(),
            'error':'Пароли не совпадают'
        })

def loginuser(request):
        if request.method == 'GET':
            return render(request, './loginuser.html', {
            'form':AuthenticationForm()
            })
        else:
            user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
            if user is None:
                return render(request, './loginuser.html', {
            'form':AuthenticationForm(),
            'error':'Неверный логин или пароль'
            })
            else:
                login(request, user)
                return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        