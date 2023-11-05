from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from car.forms import CarForm
from car.models import Car


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    permission_required = ['car.add_car']
    success_url = reverse_lazy('car:home')


class CarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    permission_required = ['car.change_car']
    template_name = 'car/car_form_with_formset.html'
