from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user)
            return HttpResponse('sucessfully login')
        else:
            messages.success(
                request, ('There was an error logging .Pls Try again'))
            return redirect('home')
    else:

        return render(request, 'registration/login.html', {'messages': messages})


def logout_user(request):
    logout(request)
    messages.success(
        request, ('There was loggedout '))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('Register successfully'))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})
