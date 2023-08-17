from django.shortcuts import render
from django.views.generic import ListView, DetailView

from car.models import Car


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car
