from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
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


class CarUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    permission_required = 'car.change_car'
    model = Car
    form_class = CarForm

    def test_func(self):
        return self.request.user.is_staff

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_success_url(self):
        return reverse('car:inc_car_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        """получение данных контекста, которые будут переданы в шаблон"""

        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        CarFormset = inlineformset_factory(parent_model=Owner, model=Car, form=CarForm, extra=1)
        CarHistoryFormset = inlineformset_factory(parent_model=Car, model=CarHistory, form=CarHistoryForm, extra=1)
        if self.request.method == 'POST':
            context_data['Car_formset'] = CarFormset(self.request.POST, instance=self.object.owner)
            context_data['CarHistory_formset'] = CarHistoryFormset(self.request.POST, instance=self.object)
        else:
            context_data['Car_formset'] = CarFormset(instance=self.object.owner)
            context_data['CarHistory_formset'] = CarHistoryFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """обработка формы, когда данные формы прошли все необходимые проверки и являются валидными"""

        Car_formset = self.get_context_data()['Car_formset']
        CarHistory_formset = self.get_context_data()['CarHistory_formset']

        self.object = form.save()

        if Car_formset.is_valid() and CarHistory_formset.is_valid():
            Car_formset.instance = self.object
            Car_formset.save()

            CarHistory_formset.instance = self.object
            CarHistory_formset.save()

        return super().form_valid(form)


class CustomCarDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    permission_required = 'car.delete_car'
    model = Car
    # form_class = CarForm
    context_object_name = 'car'
    success_url = reverse_lazy('car:home')

    def get_permission_denied_message(self):
        return "Вы не имеете прав на удаление."

    def test_func(self):
        return self.request.user.is_staff
    #
    # def handle_no_permission(self):
    #     if self.raise_exception or self.request.user.is_authenticated:
    #         raise PermissionDenied(self.get_permission_denied_message())
    #     else:
    #         return HttpResponseRedirect(self.get_login_url())
