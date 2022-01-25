from django.urls import path

from .views import pollen_measurement_form, pollen_measurement_delete, pollen_measurement_list

urlpatterns = [
    path('', pollen_measurement_form, name='pollen_measurement_insert'),
    path('<int:id>/', pollen_measurement_form, name='pollen_measurement_update'),
    path('delete/<int:id>/', pollen_measurement_delete, name='pollen_measurement_delete'),
    path('list/', pollen_measurement_list, name='pollen_measurement_list')
]
