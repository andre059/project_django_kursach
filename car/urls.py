from django.urls import path

from car.apps import CarConfig
from car.views import CarListView, CarDetailView, CarCreateView, CarDeleteView, CarUpdateView

app_name = CarConfig.name


urlpatterns = [
    path('', CarListView.as_view(), name='home'),
    path('<int:pk>/', CarDetailView.as_view(), name='inc_car_detail'),
    path('create/', CarCreateView.as_view(), name='create_car'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='update'),
]
