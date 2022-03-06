from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

from .forms import RegistForm, UserLoginForm, UserUpdateForm
from .models import UserActivateTokens, User
import os


class HomeView(TemplateView):
    template_name = os.path.join('accounts', 'home.html')


class RegistUserView(CreateView):
    template_name = os.path.join('accounts', 'regist.html')
    form_class = RegistForm


def activate_user(request, token):
    user_activate_token = UserActivateTokens.objects.activate_user_by_token(token)
    return render(
        request, 'accounts/activate_user.html'
    )


class UserLoginView(LoginView):
    template_name = os.path.join('accounts', 'user_login.html')
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(604800)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = os.path.join('accounts', 'user_detail.html')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserUpdateView(UpdateView):
    template_name = os.path.join('accounts', 'user_update.html')
    
    form_class = UserUpdateForm
    model = User


def upload_model_form(request):
    user = None
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
    else:
        form = UserUpdateForm()
    return render(request, 'accounts/user_update.html', context={
        'form': form, 'user': user
    })