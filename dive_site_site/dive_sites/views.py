from django.views.generic import ListView, DetailView
from .models import Dive

class DiveSiteListView(ListView):
    model = Dive
    template_name = 'home.html'

class DiveSiteDetailView(DetailView):
    model = Dive
    template_name = 'dive_site_details.html'


