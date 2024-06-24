from django.shortcuts import redirect, render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.views.generic import CreateView, FormView, DetailView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, UserUpdateForm
from cars.models import Car
from .models import Order


# Create your views here.
class UserCreateView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("profile")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please provide valid information!")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Register"
        return context


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "register.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f"'{username}' logged in successfully")
            return redirect("home")
        else:
            messages.error(self.request, f"'{username}' user not found!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password!")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    messages.info(request, "Logout successfully!")
    return redirect("login")


@login_required(login_url="login")
def user_profile(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "profile.html", context)


@login_required(login_url="login")
def buy_car(request, car_id):
    car = Car.objects.get(pk=car_id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        order = Order.objects.create(buyer=request.user, car=car)
    else:
        messages.warning(request, "Sorry, this car is not available at this moment!")
    return redirect("car_details", id=car_id)


def update_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'"{username}" updated successfully  !!!')
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password!")
    else:
        form = UserUpdateForm(instance=request.user)

    context = {"form": form, "type": "Update Profile"}
    return render(request, "register.html", context)


class UpdatePassword(PasswordChangeView):
    template_name = "register.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "Password changed successfully!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Change Password"
        return context
