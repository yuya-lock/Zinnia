from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import HallCreateForm, ReviewCreateForm
from .models import Hall, Review
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


class ReviewListView(LoginRequiredMixin, ListView):
    template_name = os.path.join('halls', 'review_list.html')
    model = Review
    paginate_by = 20

    def get_queryset(self):
        query = super().get_queryset()
        query = Review.objects.filter(hall=self.kwargs['pk'])
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hall'] = get_object_or_404(Hall, pk=self.kwargs['pk'])
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = os.path.join('halls', 'review_create.html')
    form_class = ReviewCreateForm
    model = Review

    def get_success_url(self):
        return reverse_lazy('halls:review_list', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        hall_pk = self.kwargs['pk']
        hall = get_object_or_404(Hall, pk=hall_pk)
        review.hall = hall
        review.save()
        return super(ReviewCreateView, self).form_valid(form)


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('halls', 'review_delete.html')
    model = Review
    
    def success_url(self):
        return reverse_lazy('halls:review_list', kwargs={'pk': self.kwargs['pk']})
