from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import HallCreateForm
from .models import Hall
import os


class HallListView(LoginRequiredMixin, ListView):
    template_name = os.path.join('halls', 'hall_list.html')
    model = Hall
    paginate_by = 1


class HallDetailView(LoginRequiredMixin, DetailView):
    template_name = os.path.join('halls', 'hall_detail.html')
    model = Hall


class HallCreateView(LoginRequiredMixin, CreateView):
    template_name = os.path.join('halls', 'hall_create.html')
    form_class = HallCreateForm
    model = Hall
    success_url = reverse_lazy('halls:hall_list')


def upload_create_model_form(request):
    post = None
    if request.method == 'POST':
        form = HallCreateForm(request.POST, request.FILES)
        if form.is_valid():
            hall = form.save()
    else:
        form = HallCreateForm()
    return render(request, 'halls/hall_create.html', context={
        'form': form, 'hall': hall
    })


class HallUpdateView(LoginRequiredMixin, UpdateView):
    template_name = os.path.join('halls', 'hall_update.html')
    form_class = HallCreateForm
    model = Hall
    
    def success_url(self):
        return reverse_lazy('halls:hall_detail', kwargs={'pk': self.object.id})


def upload_update_model_form(request):
    post = None
    if request.method == 'POST':
        form = HallCreateForm(request.POST, request.FILES)
        if form.is_valid():
            hall = form.save()
    else:
        form = HallCreateForm()
    return render(request, 'halls/hall_update.html', context={
        'form': form, 'hall': hall
    })


class HallDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('halls', 'hall_delete.html')
    model = Hall
    success_url = reverse_lazy('halls:hall_list')