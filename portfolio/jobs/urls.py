# jobs app URLS

from django.urls import path
from .views import HomeView, JobDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("jobs/<int:pk>", JobDetailView.as_view(), name="detail"),
]