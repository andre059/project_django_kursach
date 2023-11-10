from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from car.forms import CarForm, OwnerForm, CarHistoryForm
from car.models import Car, Owner, CarHistory


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_success_url(self):
        return reverse('car:inc_car_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        """получение данных контекста, которые будут переданы в шаблон"""

        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        OwnerFormset = inlineformset_factory(Car, Owner, form=OwnerForm, extra=1)
        CarHistoryFormset = inlineformset_factory(Car, CarHistory, form=CarHistoryForm, extra=1)
        if self.request.method == 'POST':
            context_data['Owner_formset'] = OwnerFormset(self.request.POST, instance=self.object)
            context_data['CarHistory_formset'] = CarHistoryFormset(self.request.POST, instance=self.object)
        else:
            context_data['Owner_formset'] = OwnerFormset(instance=self.object)
            context_data['CarHistory_formset'] = CarHistoryFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """обработка формы, когда данные формы прошли все необходимые проверки и являются валидными"""

        Owner_formset = self.get_context_data()['Owner_formset']
        CarHistory_formset = self.get_context_data()['CarHistory_formset']

        self.object = form.save()

        if Owner_formset.is_valid() and CarHistory_formset.is_valid():
            Owner_formset.instance = self.object
            Owner_formset.save()

            CarHistory_formset.instance = self.object
            CarHistory_formset.save()

        return super().form_valid(form)


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('car:home')

    def test_func(self):
        return self.request.user.is_superuser and self.request.user.is_staff
