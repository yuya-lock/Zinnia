from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import User
from .forms import PostCreateForm
from .models import Post
import os


class PostListView(LoginRequiredMixin, ListView):
    template_name = os.path.join('shares', 'post_list.html')
    model = Post
    queryset = Post.objects.order_by('-created_at')
    paginate_by = 3


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = os.path.join('shares', 'post_detail.html')
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = os.path.join('shares', 'post_create.html')
    form_class = PostCreateForm
    model = Post
    success_url = reverse_lazy('shares:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


def upload_create_model_form(request):
    post = None
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
    else:
        form = PostCreateForm()
    return render(request, 'shares/post_create.html', context={
        'form': form, 'post': post
    })


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = os.path.join('shares', 'post_update.html')
    form_class = PostCreateForm
    model = Post
    
    def get_success_url(self):
        return reverse_lazy('shares:post_detail', kwargs={'pk': self.object.id})


def upload_update_model_form(request):
    post = None
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
    else:
        form = PostCreateForm()
    return render(request, 'shares/post_update.html', context={
        'form': form, 'post': post
    })


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('shares', 'post_delete.html')
    model = Post
    success_url = reverse_lazy('shares:post_list')