from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Job


# Create your views here.
class HomeView(ListView):
    model = Job
    context_object_name = "jobs"
    template_name = "jobs/home.html"


class JobDetailView(DetailView):
    model = Job
    context_object_name = "job"
    template_name = "jobs/detail.html"
