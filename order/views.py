from threading import Thread

import schedule
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from car.models import Car
from order.cervices import schedule_email, start_scheduling
from order.models import Order


class OrderCreateView(CreateView):
    model = Order
    fields = ('car', 'name', 'email', 'message',)

    def get_success_url(self):
        return reverse('car:car_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['car'] = get_object_or_404(Car, pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        obj = form.save()

        schedule.every().day.at("14:06").do(schedule_email, obj)

        t = Thread(target=start_scheduling)
        t.start()

        return super().form_valid(form)

