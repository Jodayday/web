from django.urls import path
from .views import DownloadsView

app_name = 'downloads'
urlpatterns = [
    path('', DownloadsView.as_view(), name='list'),
]
