from django.urls import path
from . import views
# from main_app.views import 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    
]