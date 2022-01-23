from django import forms
from .models import PollenMeasurement

class PollenMeasurementForm(forms.ModelForm):
    class Meta:
        model = PollenMeasurement
        fields = ['pollen_type', 'pollen_count', 'measurement_location']
