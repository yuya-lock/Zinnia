from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from .forms import RegistForm, UserLoginForm, UserUpdateForm, PasswordChangeForm
from .models import UserActivateTokens, User
from shares.models import Post
import os


class HomeView(TemplateView):
    template_name = os.path.join('accounts', 'home.html')


def regist(request):
    form = RegistForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            return redirect('accounts:user_login')
        except ValidationError as e:
            form.add_error('password', e)
    return render(
        request, 'accounts/regist.html', context={
            'form': form,
        } 
    )


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


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = os.path.join('accounts', 'user_detail.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_posts'] = Post.objects.filter_by_post(user=self.object)
        context['post_user_id'] = self.kwargs['pk']
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = os.path.join('accounts', 'user_update.html')
    form_class = UserUpdateForm
    model = User

    def get_success_url(self):
        return reverse_lazy('accounts:user_detail', kwargs={'pk': self.object.id})


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


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('accounts', 'user_delete.html')
    model = User
    success_url = reverse_lazy('accounts:regist')


def password_change(request):
    form = PasswordChangeForm(request.POST or None, instance=request.user)
    if form.is_valid():
        try:
            form.save()
            messages.success(request, 'パスワードを変更しました')
            update_session_auth_hash(request, request.user)
        except ValidationError as e:
            form.add_error('password', e)
    return render(
        request, 'accounts/password_change.html', context={
            'form': form,
        }
    )