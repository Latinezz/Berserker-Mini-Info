from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})

def primary(request):
    return render(request, 'main/primary.html')


def about(request):
    return render(request, 'main/about.html')

def design(request):
    return render(request,'main/design.html')


def korzina(request):
    return render(request,'main/korzina.html')

def otryad(request):
    return render(request,'main/otryad.html')


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signap.html', {'form': form})


def gif(request):
    return render(request,'main/gif.html')
