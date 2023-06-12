from django.shortcuts import render
from users.forms import UserRegistrationForm


def index(request):
    return render(request, 'base.html')


def register(request):
    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def admin(request):
    return render(request, 'admin.html')


def user(request):
    return render(request, 'user.html')
