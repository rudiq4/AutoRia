from django.views import View
from .models import UserAccount
from registration.forms import RegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

User = get_user_model()


class RegistrationView(View):
    template = 'registration/registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user.set_password(password)
            password_check = form.cleaned_data['password_check']
            # phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            new_user.save()
            UserAccount.objects.create(user=User.objects.get(username=new_user.username),
                                       email=new_user.email)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(self.request, self.template, context)


class LoginView(View):
    template = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
                return HttpResponseRedirect('/')
        context = {'form': form}
        return render(self.request, self.template, context)


def logout_view(request):
    logout(request)
    return redirect("/")


class AccountView(View):
    template = 'registration/account.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs.get('user')
        this_user = UserAccount.objects.get(user=User.objects.get(username=user))
        context = {'this_user': this_user}
        return render(self.request, self.template, context)
