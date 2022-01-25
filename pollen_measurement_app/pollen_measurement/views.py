from django.shortcuts import render, redirect
from .models import PollenMeasurement
from .forms import PollenMeasurementForm
from django.utils import timezone

def pollen_measurement_list(request):
    pollenMeasurement = PollenMeasurement.objects.order_by('-measurement_time')
    context = {'pollen_measurement_list': pollenMeasurement}
    return render(request, "templates/pollen_measurement_list.html", context)

def pollen_measurement_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PollenMeasurementForm()
        else:
            pollenMeasurement = PollenMeasurement.objects.get(pk=id)
            form = PollenMeasurementForm(instance = pollenMeasurement)
        return render(request, "templates/pollen_measurement_form.html", {'form': form})
    else:
        if id == 0:
            form = PollenMeasurementForm(request.POST)
        else:
            pollenMeasurement = PollenMeasurement.objects.get(pk=id)
            form = PollenMeasurementForm(request.POST, instance = pollenMeasurement)
        if form.is_valid():
            form = form.save(commit=False)
            form.measurement_time = timezone.now()
            form.save()

        return redirect('/measurement/list')

def pollen_measurement_delete(request,id):
    pollenMeasurement = PollenMeasurement.objects.get(pk=id)
    pollenMeasurement.delete()
    return redirect('/measurement/list')
