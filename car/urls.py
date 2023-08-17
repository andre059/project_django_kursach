from django.urls import path

from car.apps import CarConfig
from car.views import CarListView, CarDetailView

app_name = CarConfig.name


urlpatterns = [
    path('', CarListView.as_view(), name='base'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_view'),
]
