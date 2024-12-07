from django import forms
from .models import Garden, Plot, Plant
class GardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ['name', 'location', 'user']
class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['name', 'dayssincewatered', 'garden']
        labels = {
            'dayssincewatered': 'Days Since Watered'
        }
class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'dayssinceplanted', 'daysuntilmature', 'description', 'plot'] 



