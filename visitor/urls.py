from django.urls import path
from visitor import views

urlpatterns = [
    path("stats/", views.stats, name="visitor-starts"),
    
]