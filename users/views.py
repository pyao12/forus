from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


def home(request):
    if request.user.is_authenticated:
        return redirect("users:profile")
    return render(request, "users/home.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("users:profile")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "登录成功。")
        return redirect("users:profile")
    return render(request, "users/login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("users:profile")

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "注册成功，已自动登录。")
        return redirect("users:profile")
    return render(request, "users/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "users/profile.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "你已退出登录。")
    return redirect("users:login")
