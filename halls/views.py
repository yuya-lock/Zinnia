from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Hall
import os


class HallListView(LoginRequiredMixin, ListView):
    template_name = os.path.join('halls', 'hall_list.html')
    model = Hall
