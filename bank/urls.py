from django.urls import path
from . import views

urlpatterns = [
    path('details/<ifsc_code>/',views.details,name="details"),
    path('branches/<city>&<bank>/',views.branches,name='branches'),
]