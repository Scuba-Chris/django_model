from django.urls import path
from .views import DiveSiteListView, DiveSiteDetailView

urlpatterns = [
    path('dive/<int:pk>/', DiveSiteDetailView.as_view(), name='dive_site_details'),
    path('', DiveSiteListView.as_view(), name='home'),
]