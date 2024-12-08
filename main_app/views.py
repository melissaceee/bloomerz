from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Garden, Plot, Plant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('garden-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



class Home(LoginView):
    template_name = 'home.html'
    
def garden_index(request):
    gardens = Garden.objects.filter(user=request.user)
    plots = []
    for garden in gardens:
        plots.extend(garden.plot_set.all())
    return render(request, 'gardens/index.html', {'gardens': gardens, 'plots': plots})

def plant_index(request):
    garden = Garden.objects.filter(user=request.user)[:1].get()
    plots = Plot.objects.filter(garden=garden)
    plants = []
    for plot in plots:
        plants.extend(plot.plant_set.all())
    return render(request, 'plants/index.html', {'plants': plants})

def plot_index(request):
    garden = Garden.objects.filter(user=request.user)[:1].get()
    plots = garden.plot_set.all()
    return render(request, 'plots/index.html', { 'plots': plots})

class garden_detail(DetailView):
    model = Garden
    template_name = 'gardens/detail.html'

class GardenCreate(CreateView):
    model = Garden
    fields = '__all__'
    template_name = 'gardens/create.html'

class GardenUpdate(UpdateView):
    model = Garden
    fields = ['name', 'location']
    template_name = 'gardens/update.html'

class GardenDelete(DeleteView):
    model = Garden
    template_name = 'gardens/delete.html'
    success_url = '/gardens/'



class CreatePlot(CreateView):
    model = Plot
    fields = '__all__'
    template_name = 'plots/create.html'

class PlotDetail(DetailView):
    model = Plot
    template_name = 'plots/detail.html'

class UpdatePlot(UpdateView):
    model = Plot
    fields = ['name', 'dayssincewatered']
    template_name = 'plots/update.html'

class DeletePlot(DeleteView):
    model = Plot
    template_name = 'plots/delete.html'
    success_url = '/gardens/'


    
class CreatePlant(CreateView):
    model = Plant
    fields = '__all__'
    template_name = 'plants/create.html'

class PlantDetail(DetailView):
    model = Plant
    template_name = 'plants/detail.html'

class UpdatePlant(UpdateView):
    model = Plant
    fields = ['name', 'dayssinceplanted', 'daysuntilmature', 'description']
    template_name = 'plants/update.html'

class DeletePlant(DeleteView):
    model = Plant
    template_name = 'plants/delete.html'
    success_url = '/gardens/'


